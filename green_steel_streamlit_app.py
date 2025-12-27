import streamlit as st
import pandas as pd
from typing import Dict, Any

st.set_page_config(page_title="Green Steel Premium Calculator", layout="wide")

# ---------------- Core model ----------------

def segment_multiplier(allocation_method: str, customer_segment: str) -> float:
    # Allocation Factor
    alloc_factor = 1.0
    if allocation_method == "physical":
        alloc_factor = 1.15
    elif allocation_method == "certificate":
        alloc_factor = 1.0
    
    # Segment Factor
    seg_factor = 1.0
    seg = customer_segment.lower()
    if seg == "automotive":
        seg_factor = 1.2
    elif seg == "construction":
        seg_factor = 1.05
    else:
        seg_factor = 1.0
        
    return alloc_factor * seg_factor

def compute_green_premium(
    product_type: str,
    baseline_emission: float,
    product_emission: float,
    abatement_cost_per_tco2: float,
    project_lifetime_years: float,
    verification_cost_per_year: float,
    annual_steel_production_tonnes: float,
    willingness_to_pay_multiplier: float,
    customer_segment: str = "other",
    volume_tonnes: float = 1.0,
    allocation_method: str = "physical",
    floor_premium_per_t: float = 0.0,
    ceiling_premium_per_t: float = float('inf'),
) -> Dict[str, Any]:

    # Step 1: CO2 Savings Calculation
    co2_savings_per_t = max(0.0, baseline_emission - product_emission)

    # Step 2: Amortized Cost Components
    # Annualized Abatement Cost per Tonne
    if project_lifetime_years > 0:
        amortized_abatement_per_t = (abatement_cost_per_tco2 * co2_savings_per_t) / project_lifetime_years
    else:
        amortized_abatement_per_t = 0.0

    # Annualized Verification Cost per Tonne
    if annual_steel_production_tonnes > 0:
        amortized_verification_per_t = verification_cost_per_year / annual_steel_production_tonnes
    else:
        amortized_verification_per_t = 0.0

    # Step 3: Base Premium Calculation
    base_premium_per_t = amortized_abatement_per_t + amortized_verification_per_t

    # Step 4: Segment & Allocation Multipliers
    # Note: The README says Total Multiplier = WTP * Allocation * Segment
    # segment_multiplier function returns Allocation * Segment
    seg_alloc_mult = segment_multiplier(allocation_method, customer_segment)
    total_multiplier = willingness_to_pay_multiplier * seg_alloc_mult

    # Step 5: Final Premium Calculation
    calculated_premium_per_t = base_premium_per_t * total_multiplier
    
    # Apply floor and ceiling
    # min(max(Calculated Premium, floor), ceiling)
    final_premium_per_t = min(max(calculated_premium_per_t, floor_premium_per_t), ceiling_premium_per_t)

    # Step 6: Derived Metrics
    premium_per_tco2 = None
    if co2_savings_per_t > 0:
        premium_per_tco2 = final_premium_per_t / co2_savings_per_t

    total_premium = final_premium_per_t * volume_tonnes

    breakdown = {
        "product_type": product_type,
        "co2_savings_per_t": round(co2_savings_per_t, 6),
        "amortized_abatement_per_t": round(amortized_abatement_per_t, 2),
        "amortized_verification_per_t": round(amortized_verification_per_t, 2),
        "base_premium_per_t": round(base_premium_per_t, 2),
        "willingness_to_pay_multiplier": round(willingness_to_pay_multiplier, 3),
        "segment_allocation_multiplier": round(seg_alloc_mult, 3),
        "total_multiplier": round(total_multiplier, 3),
        "calculated_premium_before_constraints": round(calculated_premium_per_t, 2)
    }

    return {
        "premium_per_tonne_steel": round(final_premium_per_t, 2),
        "premium_per_tCO2": (round(premium_per_tco2, 2) if premium_per_tco2 is not None else None),
        "total_premium_for_volume": round(total_premium, 2),
        "volume_tonnes": volume_tonnes,
        "breakdown": breakdown,
    }

# ---------------- Streamlit UI ----------------

st.title("Green Steel Premium Calculator")
st.markdown(
    "Interactive tool to calculate a `green steel premium` per tonne and for a given volume, based on amortized abatement and verification costs."
)

with st.expander("Example: default values (click to load)", expanded=False):
    st.write(
        "Defaults based on README example: \nAbatement ₹5000/tCO₂, Intensity 2.36 (Savings), Lifetime 10y, Verification ₹20,000,000/yr, Output 100k t/yr. \nMarket Inputs: WTP 1.1x, Segment: Automotive (1.2x), Allocation: Physical (1.15x)."
    )

# Layout: inputs on left, outputs on right
col1, col2 = st.columns([1, 1])

with col1:
    st.header("Inputs")
    
    st.subheader("Primary Emissions Parameters")
    product_type = st.selectbox("Product type", ["HRC", "GI", "Other"])
    baseline_emission = st.number_input("Baseline emission (tCO2 / t_steel)", min_value=0.0, value=2.36, step=0.01, format="%.2f")
    # Option to input product emission directly or via delta
    input_mode = st.radio("Input Product Emission via:", ["Direct Value", "Delta (Reduction)"])
    if input_mode == "Direct Value":
        product_emission = st.number_input("Product emission (tCO2 / t_steel)", min_value=0.0, value=0.0, step=0.01, format="%.2f")
    else:
        delta_emission = st.number_input("Delta (emission reduction, tCO2 / t_steel)", min_value=0.0, value=2.36, step=0.01, format="%.2f")
        product_emission = max(0.0, baseline_emission - delta_emission)
        st.info(f"Calculated product emission: {product_emission:.2f} tCO2 / t_steel")

    st.subheader("Project & Cost Parameters")
    abatement_cost_per_tco2 = st.number_input("Abatement cost (₹ / tCO2)", min_value=0.0, value=5000.0, step=100.0)
    project_lifetime_years = st.number_input("Project lifetime (years)", min_value=1.0, value=10.0, step=1.0)
    verification_cost_per_year = st.number_input("Verification & admin cost (₹ / year)", min_value=0.0, value=20000000.0, step=100000.0, format="%.0f")
    annual_steel_production_tonnes = st.number_input("Annual steel production (tonnes / year)", min_value=1.0, value=100000.0, step=1000.0)

    st.subheader("Market Adjustment Parameters")
    # WTP Multiplier
    wtp_input_val = st.number_input("Willingness-to-Pay Multiplier (e.g. 1.1 for 10% markup)", min_value=0.0, value=1.1, step=0.05)
    willingness_to_pay_multiplier = wtp_input_val

    customer_segment = st.selectbox("Customer segment", ["automotive", "construction", "other"])
    allocation_method = st.selectbox("Allocation method", ["physical", "certificate"])

    st.subheader("Volume & Constraints")
    volume_tonnes = st.number_input("Volume (tonnes)", min_value=1.0, value=1000.0, step=1.0)
    floor_premium_per_t = st.number_input("Floor premium (₹ / t)", min_value=0.0, value=0.0, step=10.0)
    ceiling_premium_per_t = st.number_input("Ceiling premium (₹ / t) (0 for no ceiling)", min_value=0.0, value=0.0, step=10.0)
    
    # Handle 0 ceiling as infinity
    actual_ceiling = float('inf') if ceiling_premium_per_t <= 0 else ceiling_premium_per_t

    if st.button("Compute premium"):
        result = compute_green_premium(
            product_type=product_type,
            baseline_emission=baseline_emission,
            product_emission=product_emission,
            abatement_cost_per_tco2=abatement_cost_per_tco2,
            project_lifetime_years=project_lifetime_years,
            verification_cost_per_year=verification_cost_per_year,
            annual_steel_production_tonnes=annual_steel_production_tonnes,
            willingness_to_pay_multiplier=willingness_to_pay_multiplier,
            customer_segment=customer_segment,
            volume_tonnes=volume_tonnes,
            allocation_method=allocation_method,
            floor_premium_per_t=floor_premium_per_t,
            ceiling_premium_per_t=actual_ceiling,
        )
        st.session_state['last_result'] = result

# show last computed result or a default compute
if 'last_result' not in st.session_state:
    # run a default compute so the right column isn't empty
    actual_ceiling = float('inf') if ceiling_premium_per_t <= 0 else ceiling_premium_per_t
    st.session_state['last_result'] = compute_green_premium(
        product_type=product_type,
        baseline_emission=baseline_emission,
        product_emission=product_emission,
        abatement_cost_per_tco2=abatement_cost_per_tco2,
        project_lifetime_years=project_lifetime_years,
        verification_cost_per_year=verification_cost_per_year,
        annual_steel_production_tonnes=annual_steel_production_tonnes,
        willingness_to_pay_multiplier=willingness_to_pay_multiplier,
        customer_segment=customer_segment,
        volume_tonnes=volume_tonnes,
        allocation_method=allocation_method,
        floor_premium_per_t=floor_premium_per_t,
        ceiling_premium_per_t=actual_ceiling,
    )

with col2:
    st.header("Result")
    res = st.session_state['last_result']

    st.metric(label="Premium per tonne (₹)", value=f"{res['premium_per_tonne_steel']:,}")
    if res['premium_per_tCO2'] is not None:
        st.metric(label="Premium per tCO2 saved (₹)", value=f"{res['premium_per_tCO2']:,}")
    st.metric(label="Total premium for volume (₹)", value=f"{res['total_premium_for_volume']:,}")

    st.subheader("Breakdown")
    bd = res['breakdown']
    bd_df = pd.DataFrame.from_dict(bd, orient='index', columns=['value'])
    bd_df = bd_df.reset_index().rename(columns={'index': 'component'})
    st.table(bd_df)

    # CSV of sensitivity scenarios (low/med/high abatement cost)
    st.subheader("Sensitivity Analysis: Abatement Cost sweep")
    sweep = []
    multipliers = [0.8, 1.0, 1.2]
    for idx, multiplier in enumerate(multipliers):
        ac = abatement_cost_per_tco2 * multiplier
        actual_ceiling = float('inf') if ceiling_premium_per_t <= 0 else ceiling_premium_per_t
        r = compute_green_premium(
            product_type=product_type,
            baseline_emission=baseline_emission,
            product_emission=product_emission,
            abatement_cost_per_tco2=ac,
            project_lifetime_years=project_lifetime_years,
            verification_cost_per_year=verification_cost_per_year,
            annual_steel_production_tonnes=annual_steel_production_tonnes,
            willingness_to_pay_multiplier=willingness_to_pay_multiplier,
            customer_segment=customer_segment,
            volume_tonnes=volume_tonnes,
            allocation_method=allocation_method,
            floor_premium_per_t=floor_premium_per_t,
            ceiling_premium_per_t=actual_ceiling,
        )
        sweep.append({
            'abatement_cost_per_tCO2': ac,
            'premium_per_tonne': r['premium_per_tonne_steel'],
            'premium_per_tCO2': r['premium_per_tCO2'],
            'total_for_volume': r['total_premium_for_volume'],
        })
    sweep_df = pd.DataFrame(sweep)
    st.table(sweep_df)

st.markdown("---")

