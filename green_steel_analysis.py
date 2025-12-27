import pandas as pd
import itertools
from typing import Dict, Any, List

# ---------------- Core Logic (Extracted from Streamlit App) ----------------

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
    seg_alloc_mult = segment_multiplier(allocation_method, customer_segment)
    total_multiplier = willingness_to_pay_multiplier * seg_alloc_mult

    # Step 5: Final Premium Calculation
    calculated_premium_per_t = base_premium_per_t * total_multiplier
    
    # Apply floor and ceiling
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

# ---------------- Scenario Analysis ----------------

def run_grid_search():
    # Define ranges for parameters
    # You can modify these lists to test different scenarios
    scenarios = {
        "product_type": ["HRC"],
        "baseline_emission": [2.36],
        "product_emission": [0.0, 0.8, 1.6], # Zero carbon, Low carbon, Reduced carbon
        "abatement_cost_per_tco2": [3000, 5000, 7000], # Low, Mid, High cost scenarios
        "project_lifetime_years": [10],
        "verification_cost_per_year": [20000000],
        "annual_steel_production_tonnes": [100000],
        "willingness_to_pay_multiplier": [1.0, 1.1, 1.2], # 0%, 10%, 20% markup
        "customer_segment": ["automotive", "construction", "other"],
        "allocation_method": ["physical", "certificate"],
        "volume_tonnes": [1000],
        "floor_premium_per_t": [0],
        "ceiling_premium_per_t": [float('inf')]
    }

    # Generate all combinations
    keys, values = zip(*scenarios.items())
    combinations = [dict(zip(keys, v)) for v in itertools.product(*values)]

    print(f"Running analysis on {len(combinations)} scenarios...")

    results = []
    for scenario in combinations:
        # Run model
        output = compute_green_premium(**scenario)
        
        # Flatten result for DataFrame
        row = scenario.copy()
        row.update(output)
        # Flatten breakdown if needed, or just keep top level metrics
        # Let's add key breakdown metrics
        row.update(output['breakdown'])
        del row['breakdown'] # Remove nested dict
        
        results.append(row)

    df = pd.DataFrame(results)
    return df

if __name__ == "__main__":
    df_results = run_grid_search()
    
    # Save to CSV
    output_file = "green_steel_scenarios.csv"
    df_results.to_csv(output_file, index=False)
    
    print(f"Analysis complete. Results saved to {output_file}")
    print("\nSample results (head):")
    print(df_results[["product_emission", "abatement_cost_per_tco2", "customer_segment", "premium_per_tonne_steel", "premium_per_tCO2"]].head())
    
    # Example: Find max premium scenario
    max_prem = df_results.loc[df_results['premium_per_tonne_steel'].idxmax()]
    print("\nScenario with Highest Premium per Tonne Steel:")
    print(max_prem[["product_emission", "abatement_cost_per_tco2", "customer_segment", "premium_per_tonne_steel", "premium_per_tCO2"]])

    # Example: Find min premium scenario (Steel)
    min_prem_steel = df_results.loc[df_results['premium_per_tonne_steel'].idxmin()]
    print("\nScenario with Lowest Premium per Tonne Steel:")
    print(min_prem_steel[["product_emission", "abatement_cost_per_tco2", "customer_segment", "premium_per_tonne_steel", "premium_per_tCO2"]])

    # Example: Find min premium scenario (CO2)
    # Filter for rows where premium_per_tCO2 is not null (savings > 0)
    df_co2 = df_results.dropna(subset=['premium_per_tCO2'])
    if not df_co2.empty:
        min_prem_co2 = df_co2.loc[df_co2['premium_per_tCO2'].idxmin()]
        print("\nScenario with Lowest Premium per Tonne CO2:")
        print(min_prem_co2[["product_emission", "abatement_cost_per_tco2", "customer_segment", "premium_per_tonne_steel", "premium_per_tCO2"]])
