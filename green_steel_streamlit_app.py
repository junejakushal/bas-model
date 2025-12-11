# green_steel_streamlit_app.py
# Streamlit webapp MVP for Green Steel Premium Calculator
# Single-file app. To run locally: `pip install streamlit pandas` then `streamlit run green_steel_streamlit_app.py`

import streamlit as st
import pandas as pd
import json
from typing import Dict, Any

st.set_page_config(page_title="Green Steel Premium Calculator", layout="wide")

# ---------------- Core model (same as MVP shared earlier) ----------------

def segment_multiplier(allocation_method: str, customer_segment: str) -> float:
    base = 1.0
    if allocation_method == "physical":
        base *= 1.15
    elif allocation_method == "certificate":
        base *= 1.0

    seg = customer_segment.lower()
    if seg == "automotive":
        base *= 1.2
    elif seg == "construction":
        base *= 1.05
    else:
        base *= 1.0
    return base


def compute_green_premium(
    product_type: str,
    baseline_emission: float,
    product_emission: float,
    abatement_cost_per_tco2: float,
    verification_cost_per_tonne: float,
    margin_and_wtp_multiplier: float,
    customer_segment: str = "other",
    volume_tonnes: float = 1.0,
    allocation_method: str = "physical",
) -> Dict[str, Any]:

    co2_savings_per_t = max(0.0, baseline_emission - product_emission)

    if co2_savings_per_t <= 0:
        abatement_component_per_t = 0.0
        verification_component_per_t = verification_cost_per_tonne
    else:
        abatement_component_per_t = co2_savings_per_t * abatement_cost_per_tco2
        verification_component_per_t = verification_cost_per_tonne

    base_cost_stack_per_t = abatement_component_per_t + verification_component_per_t
    seg_mult = segment_multiplier(allocation_method, customer_segment)
    premium_per_t = base_cost_stack_per_t * margin_and_wtp_multiplier * seg_mult

    premium_per_tco2 = None
    if co2_savings_per_t > 0:
        premium_per_tco2 = premium_per_t / co2_savings_per_t

    total_premium = premium_per_t * volume_tonnes

    breakdown = {
        "product_type": product_type,
        "co2_savings_per_t": round(co2_savings_per_t, 6),
        "abatement_component_per_t": round(abatement_component_per_t, 2),
        "verification_component_per_t": round(verification_component_per_t, 2),
        "base_cost_stack_per_t": round(base_cost_stack_per_t, 2),
        "margin_and_wtp_multiplier": round(margin_and_wtp_multiplier, 3),
        "segment_multiplier": round(seg_mult, 3),
    }

    return {
        "premium_per_tonne_steel": round(premium_per_t, 2),
        "premium_per_tCO2": (round(premium_per_tco2, 2) if premium_per_tco2 is not None else None),
        "total_premium_for_volume": round(total_premium, 2),
        "volume_tonnes": volume_tonnes,
        "breakdown": breakdown,
    }

# ---------------- Streamlit UI ----------------

st.title("Green Steel Premium Calculator")
st.markdown(
    "Interactive tool to calculate a `green steel premium` per tonne and for a given volume."
)

with st.expander("Example: default values (click to load)", expanded=False):
    st.write(
        "Defaults: \nbaseline 2.0 tCO2/t, \ndelta 1.2 tCO2/t (product = 0.8 tCO2/t), \nabatement cost 5000 ₹/tCO2, \nverification 200 ₹/t, \nmargin & WTP 20%, \nautomotive, \nphysical allocation."
    )

# Layout: inputs on left, outputs on right
col1, col2 = st.columns([1, 1])

with col1:
    st.header("Inputs")
    product_type = st.selectbox("Product type", ["HRC", "GI", "Other"])
    baseline_emission = st.number_input("Baseline emission (tCO2 / t_steel)", min_value=0.0, value=2.0, step=0.1)
    delta_emission = st.number_input("Delta (emission reduction, tCO2 / t_steel)", min_value=0.0, value=1.2, step=0.1)
    product_emission = baseline_emission - delta_emission
    st.info(f"Calculated product emission: {product_emission:.2f} tCO2 / t_steel")
    
    abatement_cost_per_tco2 = st.number_input("Abatement cost (₹ / tCO2)", min_value=0.0, value=5000.0, step=100.0)
    verification_cost_per_tonne = st.number_input("Verification & admin cost (₹ / t_steel)", min_value=0.0, value=200.0, step=10.0)
    margin_and_wtp_percentage = st.slider("Margin & WTP (%)", min_value=0.0, max_value=100.0, value=20.0, step=0.1)
    margin_and_wtp_multiplier = 1.0 + (margin_and_wtp_percentage / 100.0)

    customer_segment = st.selectbox("Customer segment", ["automotive", "construction", "other"])
    allocation_method = st.selectbox("Allocation method", ["physical", "certificate"])

    volume_tonnes = st.number_input("Volume (tonnes)", min_value=1.0, value=1000.0, step=1.0)

    if st.button("Compute premium"):
        result = compute_green_premium(
            product_type=product_type,
            baseline_emission=baseline_emission,
            product_emission=product_emission,
            abatement_cost_per_tco2=abatement_cost_per_tco2,
            verification_cost_per_tonne=verification_cost_per_tonne,
            margin_and_wtp_multiplier=margin_and_wtp_multiplier,
            customer_segment=customer_segment,
            volume_tonnes=volume_tonnes,
            allocation_method=allocation_method,
        )
        st.session_state['last_result'] = result

# show last computed result or a default compute
if 'last_result' not in st.session_state:
    # run a default compute so the right column isn't empty
    st.session_state['last_result'] = compute_green_premium(
        product_type=product_type,
        baseline_emission=baseline_emission,
        product_emission=product_emission,
        abatement_cost_per_tco2=abatement_cost_per_tco2,
        verification_cost_per_tonne=verification_cost_per_tonne,
        margin_and_wtp_multiplier=margin_and_wtp_multiplier,
        customer_segment=customer_segment,
        volume_tonnes=volume_tonnes,
        allocation_method=allocation_method,
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
    st.subheader("Sensitivity Analysis: Abatement Cost")
    sweep = []
    for ac in [abatement_cost_per_tco2 * 0.8, abatement_cost_per_tco2, abatement_cost_per_tco2 * 1.2]:
        r = compute_green_premium(
            product_type=product_type,
            baseline_emission=baseline_emission,
            product_emission=product_emission,
            abatement_cost_per_tco2=ac,
            verification_cost_per_tonne=verification_cost_per_tonne,
            margin_and_wtp_multiplier=margin_and_wtp_multiplier,
            customer_segment=customer_segment,
            volume_tonnes=volume_tonnes,
            allocation_method=allocation_method,
        )
        sweep.append({
            'abatement_cost_per_tCO2': round(ac, 2),
            'premium_per_tonne': round(r['premium_per_tonne_steel'], 2),
            'premium_per_tCO2': round(r['premium_per_tCO2'], 2) if r['premium_per_tCO2'] is not None else None,
            'total_for_volume': round(r['total_premium_for_volume'], 2),
        })
        sweep_df = pd.DataFrame(sweep)
        st.table(sweep_df)

st.markdown("---")
# st.caption("Built from the green steel premium model. Tweak inputs to match your commercial data and use the download button to export scenarios.")

