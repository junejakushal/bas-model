# green_steel_streamlit_app.py
# Streamlit webapp for Green Steel Premium Calculator
# Updated to include regional carbon pricing scenarios based on industry analysis.
# To run locally: `pip install streamlit pandas` then `streamlit run green_steel_streamlit_app.py`

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Green Steel Premium Calculator", layout="wide")

# ---------------- Constants & Defaults (with Citations) ----------------

# Currency conversion rates (approximate, for display)
USD_TO_INR = 87.0  # [Source: chatgpt_carbon_pricing.md]
EUR_TO_USD = 1.1   # [Source: chatgpt_carbon_pricing.md]

# Defaults
# Europe
DEFAULT_EU_ETS_PRICE_USD = 70.0  # ~€65/tCO2 [Source: chatgpt_carbon_pricing.md]
DEFAULT_EU_BENCHMARK_BF_BOF = 1.3 # ~1.3 tCO2/t [Source: Steel Carbon Pricing Algorithm Update.md]
DEFAULT_EU_EAF_BENCHMARK = 0.283 # [Source: Steel Carbon Pricing Algorithm Update.md]

# Korea & Japan
DEFAULT_KOREA_ETS_PRICE_USD = 7.0 # ~$7/tCO2 (rising to $29-44 by 2030) [Source: chatgpt_carbon_pricing.md]
DEFAULT_JAPAN_TAX_USD = 2.0      # ~$2/tCO2 [Source: chatgpt_carbon_pricing.md]
DEFAULT_JAPAN_GX_PRICE_USD = 3.0 # Voluntary/Low [Source: chatgpt_carbon_pricing.md]

# China
DEFAULT_CHINA_ETS_PRICE_USD = 13.0 # ~$13/tCO2 (~CNY 96) [Source: chatgpt_carbon_pricing.md]

# India
DEFAULT_INDIA_DOMESTIC_PRICE_USD = 0.0 # [Source: chatgpt_carbon_pricing.md]

# ---------------- Core Algorithms (from Carbon_Pricing_Algorithms.md) ----------------

def calculate_europe_cost(
    scope1_emissions: float,
    scope2_emissions: float,
    ets_price: float,
    free_allowances: float,
    elec_carbon_cost: float,
    is_importer: bool,
    embedded_emissions: float = 0.0,
    origin_carbon_price: float = 0.0
) -> dict:
    """
    Scenario 1: The Case of Europe
    Logic:
    - Domestic: (Scope 1 - Free) * Price + Scope 2 * ElecCost
    - Importer: (Embedded * Price) - (Origin Price * Embedded)
    """
    if is_importer:
        # CBAM Logic
        # Cost = (Embedded Emissions * EU ETS Price) - (Carbon Price Paid at Origin)
        # Assuming Origin Price applies to the full embedded amount for simplicity of the 'deduction' logic
        cbam_cost = (embedded_emissions * ets_price) - (embedded_emissions * origin_carbon_price)
        total_cost = max(0.0, cbam_cost)
        breakdown = {
            "Type": "Importer (CBAM)",
            "Embedded Emissions": embedded_emissions,
            "EU ETS Price": ets_price,
            "Origin Credit": origin_carbon_price,
            "Total Cost ($/t steel)": total_cost
        }
    else:
        # Domestic Producer Logic
        # Scope 1 Cost: (Scope 1 Emissions - Free Allowances) * EU ETS Price
        net_scope1 = max(0.0, scope1_emissions - free_allowances)
        cost_scope1 = net_scope1 * ets_price
        
        # Scope 2 Cost: Scope 2 Emissions * (Pass-through Carbon Cost in Electricity)
        cost_scope2 = scope2_emissions * elec_carbon_cost
        
        total_cost = cost_scope1 + cost_scope2
        breakdown = {
            "Type": "Domestic EU Producer",
            "Scope 1 Emissions": scope1_emissions,
            "Free Allowances": free_allowances,
            "Net Scope 1": net_scope1,
            "Cost Scope 1": cost_scope1,
            "Scope 2 Emissions": scope2_emissions,
            "Elec Carbon Cost": elec_carbon_cost,
            "Cost Scope 2": cost_scope2,
            "Total Cost ($/t steel)": total_cost
        }
    
    return breakdown

def calculate_korea_cost(
    total_emissions: float,
    free_allowances: float,
    kau_price: float,
    offset_limit_percent: float,
    offset_price: float
) -> dict:
    """
    Scenario 2a: South Korea (K-ETS)
    Logic:
    - Deficit = Total Emissions - Free Allowances
    - If Deficit > 0:
        - Use Offsets up to Limit % of Total Obligation (or Deficit? Usually obligation, but simplified here)
        - Buy remaining KAUs
    """
    deficit = total_emissions - free_allowances
    
    if deficit > 0:
        # Simplified: Offset limit usually applies to total compliance obligation (Total Emissions)
        max_offsets = total_emissions * (offset_limit_percent / 100.0)
        # But we only need to cover the deficit
        offsets_used = min(deficit, max_offsets)
        kaus_to_buy = deficit - offsets_used
        
        cost_offsets = offsets_used * offset_price
        cost_kaus = kaus_to_buy * kau_price
        total_cost = cost_offsets + cost_kaus
        revenue = 0.0
    else:
        # Surplus
        surplus = abs(deficit)
        revenue = surplus * kau_price
        total_cost = -revenue # Negative cost represents revenue
        offsets_used = 0.0
        kaus_to_buy = 0.0
        cost_offsets = 0.0
        cost_kaus = 0.0

    return {
        "Total Emissions": total_emissions,
        "Free Allowances": free_allowances,
        "Deficit/Surplus": deficit,
        "Offsets Used": offsets_used,
        "KAUs Bought": kaus_to_buy,
        "Cost Offsets": cost_offsets,
        "Cost KAUs": cost_kaus,
        "Total Cost ($/t steel)": total_cost
    }

def calculate_japan_cost(
    fuel_emissions: float,
    carbon_tax: float,
    gx_participation: bool,
    gx_price: float,
    emissions_vs_target: float
) -> dict:
    """
    Scenario 2b: Japan
    Logic:
    - Tax = Fuel Emissions * Tax Rate
    - GX-ETS: If participating, (Actual - Target) * Price
    """
    tax_cost = fuel_emissions * carbon_tax
    
    gx_cost = 0.0
    if gx_participation:
        # emissions_vs_target: Positive means exceeded target (pay), Negative means beat target (sell/credit)
        gx_cost = emissions_vs_target * gx_price
    
    total_cost = tax_cost + gx_cost
    
    return {
        "Fuel Emissions": fuel_emissions,
        "Carbon Tax Rate": carbon_tax,
        "Tax Cost": tax_cost,
        "GX Participation": gx_participation,
        "GX Cost/Revenue": gx_cost,
        "Total Cost ($/t steel)": total_cost
    }

def calculate_china_cost(
    production_output: float,
    actual_emissions: float,
    benchmark_intensity: float,
    ets_price: float,
    ccer_price: float,
    ccer_limit_percent: float = 5.0
) -> dict:
    """
    Scenario 3: China
    Logic:
    - Free Allocation = Production * Benchmark
    - Gap = Actual - Free Allocation
    - If Gap > 0 (Deficit):
        - Use CCERs up to 5% of compliance obligation (Actual Emissions)
        - Buy Allowances for remainder
    """
    free_allocation = production_output * benchmark_intensity
    gap = actual_emissions - free_allocation
    
    if gap > 0:
        # Deficit
        max_ccer = actual_emissions * (ccer_limit_percent / 100.0)
        ccer_used = min(gap, max_ccer)
        allowances_needed = gap - ccer_used
        
        cost_ccer = ccer_used * ccer_price
        cost_allowances = allowances_needed * ets_price
        total_cost = cost_ccer + cost_allowances
    else:
        # Surplus
        surplus = abs(gap)
        total_cost = -(surplus * ets_price) # Revenue
        ccer_used = 0.0
        allowances_needed = 0.0
        cost_ccer = 0.0
        cost_allowances = 0.0

    return {
        "Production": production_output,
        "Benchmark": benchmark_intensity,
        "Free Allocation": free_allocation,
        "Actual Emissions": actual_emissions,
        "Gap": gap,
        "CCERs Used": ccer_used,
        "Allowances Bought": allowances_needed,
        "Total Cost ($)": total_cost,
        "Cost per Tonne ($/t)": total_cost / production_output if production_output > 0 else 0
    }

def calculate_india_cost(
    qty_domestic: float,
    qty_export_eu: float,
    emission_intensity: float,
    eu_ets_price: float,
    domestic_price: float
) -> dict:
    """
    Scenario 4: India
    Logic:
    - Domestic: Qty * Domestic Price (currently ~0)
    - Export EU: Qty * Emission Intensity * (EU Price - Domestic Price)
    """
    domestic_cost = qty_domestic * emission_intensity * domestic_price
    
    # CBAM Liability
    # Cost = E_int * (P_EU - P_dom)
    cbam_rate = max(0.0, eu_ets_price - domestic_price)
    export_cost = qty_export_eu * emission_intensity * cbam_rate
    
    total_cost = domestic_cost + export_cost
    total_qty = qty_domestic + qty_export_eu
    weighted_avg = total_cost / total_qty if total_qty > 0 else 0.0
    
    # Convert to INR
    total_cost_inr = total_cost * USD_TO_INR
    weighted_avg_inr = weighted_avg * USD_TO_INR
    
    return {
        "Domestic Qty": qty_domestic,
        "Export Qty": qty_export_eu,
        "Domestic Cost ($)": total_cost,
        "Export (CBAM) Cost ($)": export_cost,
        "Total Cost ($)": total_cost,
        "Weighted Avg Cost ($/t)": weighted_avg,
        "Total Cost (INR)": total_cost_inr,
        "Weighted Avg Cost (INR/t)": weighted_avg_inr
    }

def calculate_green_premium_algo(
    delta_e: float,
    p_region: float,
    p_cbam: float,
    segment_multiplier: float,
    allocation_multiplier: float,
    wtp_multiplier: float,
    p_credit: float,
    project_life: float,
    annual_production: float,
    abatement_cost: float = 0.0,
    verification_cost: float = 0.0,
    upfront_capex: float = 0.0,
    interest_rate: float = 0.0
) -> dict:
    """
    Scenario 5: Proposed Algorithm for Green Premium
    Formula: Premium_per_tonne = Delta_E * [ (P_region + P_CBAM) * f_ind - P_credit ]
    
    Updated to include Cost-Plus logic with CAPEX amortization.
    f_ind (Industry Factor) is derived from Segment * Allocation * WTP.
    """
    # Calculate Industry Factor (f_ind)
    f_ind = segment_multiplier * allocation_multiplier * wtp_multiplier
    
    # --- Value-Based Approach (Regulatory/Market Value) ---
    # Effective Carbon Value
    effective_carbon_value = (p_region + p_cbam) * f_ind - p_credit
    premium_per_tonne_value = delta_e * effective_carbon_value
    
    # --- Cost-Plus Approach (Production Cost) ---
    # 1. Amortize CAPEX
    capex_per_tonne = 0.0
    if upfront_capex > 0 and project_life > 0:
        if interest_rate > 0:
            r = interest_rate / 100.0
            # Capital Recovery Factor (CRF)
            crf = (r * (1 + r)**project_life) / ((1 + r)**project_life - 1)
            annual_capex = upfront_capex * crf
        else:
            annual_capex = upfront_capex / project_life
        
        capex_per_tonne = annual_capex / annual_production

    # Base Cost = (Savings * Abatement Cost) + Verification Cost + Amortized CAPEX
    base_cost = (delta_e * abatement_cost) + verification_cost + capex_per_tonne
    
    # Apply Multipliers
    premium_per_tonne_cost = base_cost * f_ind
    
    # Lifecycle Calculation
    lifecycle_premium_value = premium_per_tonne_value * annual_production * project_life
    lifecycle_premium_cost = premium_per_tonne_cost * annual_production * project_life
    
    return {
        "Delta E (tCO2/t)": delta_e,
        "Industry Factor (f_ind)": f_ind,
        "Effective Carbon Value ($/tCO2)": effective_carbon_value,
        "Premium per Tonne (Value-Based) ($)": premium_per_tonne_value,
        "Lifecycle Premium (Value-Based) ($)": lifecycle_premium_value,
        "Amortized CAPEX ($/t)": capex_per_tonne,
        "Base Cost (Abatement+Verif+CAPEX) ($)": base_cost,
        "Premium per Tonne (Cost-Plus) ($)": premium_per_tonne_cost,
        "Lifecycle Premium (Cost-Plus) ($)": lifecycle_premium_cost
    }

# ---------------- Streamlit UI ----------------

st.title("Global Steel Carbon Pricing & Green Premium Calculator")
st.markdown("""
This tool implements the carbon pricing algorithms for major steel-producing regions and calculates the required Green Premium.
Based on analysis from:
- *Carbon Pricing in the Steel Sector*
- *Steel Carbon Pricing Algorithm Update*
""")

# Sidebar for Scenario Selection
scenario = st.sidebar.selectbox(
    "Select Scenario / Region",
    ["1. Europe (EU ETS & CBAM)", "2. Japan & South Korea", "3. China (National ETS)", "4. India (Export Focus)", "5. Green Premium Calculator"]
)

st.header(f"Scenario: {scenario}")

if "Europe" in scenario:
    st.subheader("EU ETS & CBAM Calculator")
    st.info("Calculates carbon costs for EU producers (ETS) or Importers (CBAM).")
    
    col1, col2 = st.columns(2)
    with col1:
        is_importer = st.checkbox("Is Importer (CBAM)?", value=False)
        ets_price = st.number_input("EU ETS Price ($/tCO2)", value=DEFAULT_EU_ETS_PRICE_USD)
        
        if is_importer:
            embedded_emissions = st.number_input("Embedded Emissions (tCO2/t steel)", value=2.0)
            origin_price = st.number_input("Carbon Price Paid at Origin ($/tCO2)", value=0.0)
            # Placeholders for unused domestic inputs
            scope1 = 0.0
            scope2 = 0.0
            free_alloc = 0.0
            elec_cost = 0.0
        else:
            scope1 = st.number_input("Scope 1 Emissions (tCO2/t steel)", value=2.0)
            scope2 = st.number_input("Scope 2 Emissions (tCO2/t steel)", value=0.2)
            free_alloc = st.number_input("Free Allowances (tCO2/t steel)", value=DEFAULT_EU_BENCHMARK_BF_BOF, help="Based on product benchmark")
            elec_cost = st.number_input("Indirect Carbon Cost in Electricity ($/tCO2)", value=0.0, help="Pass-through cost")
            # Placeholders
            embedded_emissions = 0.0
            origin_price = 0.0

    if st.button("Calculate Europe Cost"):
        res = calculate_europe_cost(scope1, scope2, ets_price, free_alloc, elec_cost, is_importer, embedded_emissions, origin_price)
        st.write("### Results")
        # Convert to string to avoid Arrow mixed-type errors
        st.table(pd.DataFrame.from_dict(res, orient='index', columns=['Value']).astype(str))

elif "Japan" in scenario:
    st.subheader("East Asia Carbon Pricing")
    sub_region = st.radio("Select Country", ["South Korea", "Japan"])
    
    if sub_region == "South Korea":
        col1, col2 = st.columns(2)
        with col1:
            total_emissions = st.number_input("Total Emissions (tCO2)", value=100000.0)
            free_alloc = st.number_input("Free Allowances (KAUs)", value=90000.0, help="Allocations are shrinking in Phase 4")
            kau_price = st.number_input("K-ETS Price ($/tCO2)", value=DEFAULT_KOREA_ETS_PRICE_USD)
            offset_limit = st.number_input("Offset Limit (%)", value=5.0)
            offset_price = st.number_input("Offset Credit Price ($/tCO2)", value=5.0)
        
        if st.button("Calculate K-ETS Cost"):
            res = calculate_korea_cost(total_emissions, free_alloc, kau_price, offset_limit, offset_price)
            st.write("### Results")
            st.table(pd.DataFrame.from_dict(res, orient='index', columns=['Value']))
            
    else: # Japan
        col1, col2 = st.columns(2)
        with col1:
            fuel_emissions = st.number_input("Fuel Emissions (Scope 1) (tCO2/t)", value=1.8)
            tax_rate = st.number_input("Carbon Tax Rate ($/tCO2)", value=DEFAULT_JAPAN_TAX_USD)
            participate_gx = st.checkbox("Participate in GX-ETS?", value=True)
            gx_price = st.number_input("GX-ETS / J-Credit Price ($/tCO2)", value=DEFAULT_JAPAN_GX_PRICE_USD)
            emissions_vs_target = st.number_input("Emissions vs Target (tCO2/t)", value=0.1, help="Positive = Exceeded Target (Pay), Negative = Beat Target (Sell)")
        
        if st.button("Calculate Japan Cost"):
            res = calculate_japan_cost(fuel_emissions, tax_rate, participate_gx, gx_price, emissions_vs_target)
            st.write("### Results")
            st.table(pd.DataFrame.from_dict(res, orient='index', columns=['Value']))

elif "China" in scenario:
    st.subheader("China National ETS")
    col1, col2 = st.columns(2)
    with col1:
        production = st.number_input("Annual Production (tonnes)", value=1000000.0)
        actual_emissions = st.number_input("Actual Emissions (tCO2)", value=2000000.0)
        benchmark = st.number_input("Benchmark Intensity (tCO2/t product)", value=1.9)
        ets_price = st.number_input("ETS Price ($/tCO2)", value=DEFAULT_CHINA_ETS_PRICE_USD)
        ccer_price = st.number_input("CCER Price ($/tCO2)", value=5.0)
    
    if st.button("Calculate China ETS Cost"):
        res = calculate_china_cost(production, actual_emissions, benchmark, ets_price, ccer_price)
        st.write("### Results")
        st.table(pd.DataFrame.from_dict(res, orient='index', columns=['Value']))

elif "India" in scenario:
    st.subheader("India (Domestic & Export)")
    st.info("Calculates weighted average cost. Results displayed in USD and INR.")
    col1, col2 = st.columns(2)
    with col1:
        qty_dom = st.number_input("Domestic Sales Volume (tonnes)", value=800000.0)
        qty_exp = st.number_input("Export to EU Volume (tonnes)", value=200000.0)
        intensity = st.number_input("Emission Intensity (tCO2/t steel)", value=2.5)
        eu_price = st.number_input("EU ETS Price ($/tCO2)", value=DEFAULT_EU_ETS_PRICE_USD)
        dom_price = st.number_input("Domestic Carbon Price ($/tCO2)", value=DEFAULT_INDIA_DOMESTIC_PRICE_USD)
    
    if st.button("Calculate Weighted Cost"):
        res = calculate_india_cost(qty_dom, qty_exp, intensity, eu_price, dom_price)
        st.write("### Results")
        # Format INR values
        df = pd.DataFrame.from_dict(res, orient='index', columns=['Value'])
        st.table(df)

elif "Green Premium" in scenario:
    st.subheader("Proposed Green Premium Algorithm")
    st.markdown("Formula: `Premium = Delta_E * [ (P_region + P_CBAM) * f_ind - P_credit ]`")
    st.markdown("Includes **Cost-Plus** comparison based on Abatement Costs.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Product & Emissions")
        product_type = st.selectbox("Product Type", ["HRC", "GI", "Other"])
        e_conv = st.number_input("Conventional Emissions (tCO2/t)", value=2.2)
        e_green = st.number_input("Green Steel Emissions (tCO2/t)", value=0.5)
        delta_e = e_conv - e_green
        st.info(f"Delta E (Savings): {delta_e:.2f} tCO2/t")
        
        st.markdown("#### Market Factors")
        segment = st.selectbox("Customer Segment", ["Automotive", "Construction", "Other"])
        allocation = st.selectbox("Allocation Method", ["Physical", "Certificate"])
        wtp_pct = st.slider("Customer Willingness to Pay (CWTP) Markup (%)", 0, 50, 20)
        wtp_multiplier = 1.0 + (wtp_pct / 100.0)
        
        # Multipliers Logic
        seg_mult = 1.2 if segment == "Automotive" else (1.05 if segment == "Construction" else 1.0)
        alloc_mult = 1.15 if allocation == "Physical" else 1.0
        
        st.markdown(f"**Combined Industry Factor (f_ind):** {seg_mult * alloc_mult * wtp_multiplier:.2f}")

    with col2:
        st.markdown("#### Regulatory & Cost Inputs")
        p_region = st.number_input("Regional Carbon Price Avoided ($/tCO2)", value=DEFAULT_EU_ETS_PRICE_USD)
        p_cbam = st.number_input("Avoided CBAM / Border Tax ($/tCO2)", value=0.0)
        p_credit = st.number_input("Carbon Credit Revenue ($/tCO2)", value=0.0)
        
        abatement_cost = st.number_input("Abatement Cost (OPEX) ($/tCO2)", value=60.0, help="Operational cost to reduce 1 ton of CO2")
        verification_cost = st.number_input("Verification Cost ($/t steel)", value=2.5)
        
        st.markdown("#### Project Finance (Amortization)")
        upfront_capex = st.number_input("Upfront Green CAPEX ($)", value=0.0, help="Total investment for green transition")
        interest_rate = st.number_input("Cost of Capital (Interest Rate %)", value=8.0)
        
        life = st.number_input("Project Life (years)", value=15.0)
        prod = st.number_input("Annual Production (tonnes)", value=100000.0)

    if st.button("Calculate Green Premium"):
        res = calculate_green_premium_algo(
            delta_e, p_region, p_cbam, seg_mult, alloc_mult, wtp_multiplier, 
            p_credit, life, prod, abatement_cost, verification_cost,
            upfront_capex, interest_rate
        )
        st.write("### Results")
        
        c1, c2 = st.columns(2)
        c1.metric("Value-Based Premium ($/t)", f"${res['Premium per Tonne (Value-Based) ($)']:.2f}")
        c2.metric("Cost-Plus Premium ($/t)", f"${res['Premium per Tonne (Cost-Plus) ($)']:.2f}")
        
        st.table(pd.DataFrame.from_dict(res, orient='index', columns=['Value']))

st.markdown("---")
st.caption("Note: All default values are based on 2024-2025 estimates from industry reports. Actual values may vary by market conditions.")
