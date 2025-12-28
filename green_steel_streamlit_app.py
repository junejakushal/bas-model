import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Green Steel Premium Calculator (Product-wise)",
    layout="wide"
)

# ---------------- Multipliers ----------------

def segment_multiplier(allocation_method, customer_segment):
    alloc = 1.15 if allocation_method == "physical" else 1.0
    seg = {
        "automotive": 1.20,
        "construction": 1.05,
        "other": 1.00
    }.get(customer_segment, 1.0)
    return alloc * seg

# ---------------- Domestic Premium ----------------

def compute_domestic_premium(
    product_type,
    baseline_emission,
    product_emission,
    abatement_cost_per_tco2,
    project_lifetime_years,
    verification_cost_per_year,
    annual_steel_production_tonnes,
    willingness_to_pay_multiplier,
    customer_segment,
    allocation_method,
):
    co2_savings = max(0.0, baseline_emission - product_emission)

    amortized_abatement = (
        abatement_cost_per_tco2 * co2_savings / project_lifetime_years
        if project_lifetime_years > 0 else 0
    )

    amortized_verification = (
        verification_cost_per_year / annual_steel_production_tonnes
        if annual_steel_production_tonnes > 0 else 0
    )

    base_premium = amortized_abatement + amortized_verification

    multiplier = willingness_to_pay_multiplier * segment_multiplier(
        allocation_method, customer_segment
    )

    domestic_premium = base_premium * multiplier

    return {
        "product_type": product_type,
        "co2_savings": co2_savings,
        "base_premium": base_premium,
        "multiplier": multiplier,
        "domestic_premium": domestic_premium
    }

# ---------------- Export Premium ----------------

def compute_export_premium(
    domestic_premium,
    co2_savings,
    carbon_price_export,
    free_allowance_factor,
    volume
):
    export_carbon_component = (
        co2_savings * carbon_price_export * (1 - free_allowance_factor)
    )
    export_premium = domestic_premium + export_carbon_component

    return {
        "export_carbon_component": export_carbon_component,
        "export_premium_per_t": export_premium,
        "total_export_premium": export_premium * volume
    }

# ---------------- UI ----------------

st.title("Green Steel Premium Calculator")
st.caption("Product-wise | Domestic + Export (CBAM / ETS)")

col1, col2 = st.columns(2)

with col1:
    st.header("Inputs")

    product_type = st.selectbox(
        "Product Type",
        ["HRC", "GI", "TMT", "Other"]
    )

    baseline_emission = st.number_input(
        "Baseline emission (tCO₂/t)",
        value=2.36
    )

    product_emission = st.number_input(
        "Green steel emission (tCO₂/t)",
        value=0.6
    )

    abatement_cost_per_tco2 = st.number_input(
        "Abatement cost (₹/tCO₂)",
        value=5000.0
    )

    project_lifetime_years = st.number_input(
        "Project lifetime (years)",
        value=10
    )

    verification_cost_per_year = st.number_input(
        "Verification cost (₹/year)",
        value=20_000_000
    )

    annual_steel_production_tonnes = st.number_input(
        "Annual production (t/year)",
        value=100_000
    )

    willingness_to_pay_multiplier = st.number_input(
        "WTP multiplier",
        value=1.1
    )

    customer_segment = st.selectbox(
        "Customer segment",
        ["automotive", "construction", "other"]
    )

    allocation_method = st.selectbox(
        "Allocation method",
        ["physical", "certificate"]
    )

    market_type = st.radio(
        "Market",
        ["Domestic", "Export"]
    )

    volume = st.number_input(
        "Order volume (t)",
        value=1000
    )

    carbon_price_export = 0.0
    free_allowance_factor = 0.0

    if market_type == "Export":
        export_market = st.selectbox(
            "Export market",
            ["EU (CBAM)", "South Korea", "Japan"]
        )

        if export_market == "EU (CBAM)":
            carbon_price_export = st.number_input(
                "EU ETS price (₹/tCO₂)",
                value=6500.0
            )
            free_allowance_factor = 0.0

        elif export_market == "South Korea":
            carbon_price_export = st.number_input(
                "K-ETS price (₹/tCO₂)",
                value=650.0
            )
            free_allowance_factor = 0.3

        elif export_market == "Japan":
            carbon_price_export = st.number_input(
                "Japan carbon price (₹/tCO₂)",
                value=180.0
            )
            free_allowance_factor = 0.8

with col2:
    st.header("Results")

    dom = compute_domestic_premium(
        product_type,
        baseline_emission,
        product_emission,
        abatement_cost_per_tco2,
        project_lifetime_years,
        verification_cost_per_year,
        annual_steel_production_tonnes,
        willingness_to_pay_multiplier,
        customer_segment,
        allocation_method,
    )

    st.metric(
        f"{product_type} – Domestic premium (₹/t)",
        f"{dom['domestic_premium']:,.0f}"
    )

    st.metric(
        "CO₂ savings (tCO₂/t)",
        f"{dom['co2_savings']:.2f}"
    )

    if market_type == "Export":
        exp = compute_export_premium(
            dom["domestic_premium"],
            dom["co2_savings"],
            carbon_price_export,
            free_allowance_factor,
            volume
        )

        st.metric(
            "Export carbon component (₹/t)",
            f"{exp['export_carbon_component']:,.0f}"
        )

        st.metric(
            f"{product_type} – Export premium (₹/t)",
            f"{exp['export_premium_per_t']:,.0f}"
        )

        st.metric(
            "Total premium (₹)",
            f"{exp['total_export_premium']:,.0f}"
        )

    st.subheader("Breakdown")
    st.table(pd.DataFrame.from_dict(dom, orient="index", columns=["Value"]))
