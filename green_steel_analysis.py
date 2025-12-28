import pandas as pd
import itertools
from typing import Dict, Any, List, Optional

# ---------------- Export Market Presets ----------------

EXPORT_MARKET_PRESETS = {
    "Domestic": {
        "carbon_price_export": 0.0,
        "free_allowance_factor": 0.0
    },
    "EU (CBAM)": {
        "carbon_price_export": 6500.0,  # ₹/tCO₂
        "free_allowance_factor": 0.0
    },
    "South Korea": {
        "carbon_price_export": 650.0,   # ₹/tCO₂
        "free_allowance_factor": 0.3
    },
    "Japan": {
        "carbon_price_export": 180.0,   # ₹/tCO₂
        "free_allowance_factor": 0.8
    }
}

# ---------------- Core Logic (Extracted from Streamlit App) ----------------

def segment_multiplier(allocation_method: str, customer_segment: str) -> float:
    """Calculate combined allocation and segment multiplier."""
    alloc = 1.15 if allocation_method == "physical" else 1.0
    seg = {
        "automotive": 1.20,
        "construction": 1.05,
        "other": 1.00
    }.get(customer_segment.lower(), 1.0)
    return alloc * seg

# ---------------- Domestic Premium ----------------

def compute_domestic_premium(
    product_type: str,
    baseline_emission: float,
    product_emission: float,
    abatement_cost_per_tco2: float,
    project_lifetime_years: float,
    verification_cost_per_year: float,
    annual_steel_production_tonnes: float,
    willingness_to_pay_multiplier: float,
    customer_segment: str,
    allocation_method: str,
) -> Dict[str, Any]:
    """Compute domestic green steel premium."""
    
    # Step 1: CO2 Savings Calculation
    co2_savings = max(0.0, baseline_emission - product_emission)

    # Step 2: Amortized Cost Components
    amortized_abatement = (
        abatement_cost_per_tco2 * co2_savings / project_lifetime_years
        if project_lifetime_years > 0 else 0
    )

    amortized_verification = (
        verification_cost_per_year / annual_steel_production_tonnes
        if annual_steel_production_tonnes > 0 else 0
    )

    # Step 3: Base Premium Calculation
    base_premium = amortized_abatement + amortized_verification

    # Step 4: Apply Multipliers
    multiplier = willingness_to_pay_multiplier * segment_multiplier(
        allocation_method, customer_segment
    )

    # Step 5: Final Domestic Premium
    domestic_premium = base_premium * multiplier

    return {
        "product_type": product_type,
        "co2_savings": co2_savings,
        "amortized_abatement": amortized_abatement,
        "amortized_verification": amortized_verification,
        "base_premium": base_premium,
        "multiplier": multiplier,
        "domestic_premium": domestic_premium
    }

# ---------------- Export Premium ----------------

def compute_export_premium(
    domestic_premium: float,
    co2_savings: float,
    carbon_price_export: float,
    free_allowance_factor: float,
    volume: float
) -> Dict[str, Any]:
    """Compute export premium including carbon cost avoided."""
    
    # Export carbon cost avoided: ΔE × P_carbon × (1 - free_allowance)
    export_carbon_component = (
        co2_savings * carbon_price_export * (1 - free_allowance_factor)
    )
    
    # Final export premium = domestic + carbon component
    export_premium_per_t = domestic_premium + export_carbon_component

    return {
        "export_carbon_component": export_carbon_component,
        "export_premium_per_t": export_premium_per_t,
        "total_export_premium": export_premium_per_t * volume
    }

# ---------------- Combined Premium Calculation ----------------

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
    export_market: str = "Domestic",
    carbon_price_export: Optional[float] = None,
    free_allowance_factor: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Compute green steel premium for domestic or export markets.
    
    For export markets, uses preset carbon prices and free allowance factors
    unless explicitly provided.
    """
    
    # Compute domestic premium first
    dom = compute_domestic_premium(
        product_type=product_type,
        baseline_emission=baseline_emission,
        product_emission=product_emission,
        abatement_cost_per_tco2=abatement_cost_per_tco2,
        project_lifetime_years=project_lifetime_years,
        verification_cost_per_year=verification_cost_per_year,
        annual_steel_production_tonnes=annual_steel_production_tonnes,
        willingness_to_pay_multiplier=willingness_to_pay_multiplier,
        customer_segment=customer_segment,
        allocation_method=allocation_method,
    )
    
    # Get export market parameters (use presets if not explicitly provided)
    market_preset = EXPORT_MARKET_PRESETS.get(export_market, EXPORT_MARKET_PRESETS["Domestic"])
    
    if carbon_price_export is None:
        carbon_price_export = market_preset["carbon_price_export"]
    if free_allowance_factor is None:
        free_allowance_factor = market_preset["free_allowance_factor"]
    
    # Compute export premium
    exp = compute_export_premium(
        domestic_premium=dom["domestic_premium"],
        co2_savings=dom["co2_savings"],
        carbon_price_export=carbon_price_export,
        free_allowance_factor=free_allowance_factor,
        volume=volume_tonnes
    )
    
    # Calculate premium per tCO2
    co2_savings = dom["co2_savings"]
    final_premium_per_t = exp["export_premium_per_t"] if export_market != "Domestic" else dom["domestic_premium"]
    
    premium_per_tco2 = None
    if co2_savings > 0:
        premium_per_tco2 = final_premium_per_t / co2_savings

    total_premium = final_premium_per_t * volume_tonnes

    breakdown = {
        "product_type": product_type,
        "co2_savings_per_t": round(co2_savings, 6),
        "amortized_abatement_per_t": round(dom["amortized_abatement"], 2),
        "amortized_verification_per_t": round(dom["amortized_verification"], 2),
        "base_premium_per_t": round(dom["base_premium"], 2),
        "willingness_to_pay_multiplier": round(willingness_to_pay_multiplier, 3),
        "segment_allocation_multiplier": round(dom["multiplier"] / willingness_to_pay_multiplier, 3),
        "total_multiplier": round(dom["multiplier"], 3),
        "domestic_premium_per_t": round(dom["domestic_premium"], 2),
        "export_market": export_market,
        "carbon_price_export": round(carbon_price_export, 2),
        "free_allowance_factor": round(free_allowance_factor, 3),
        "export_carbon_component": round(exp["export_carbon_component"], 2),
    }

    return {
        "premium_per_tonne_steel": round(final_premium_per_t, 2),
        "premium_per_tCO2": (round(premium_per_tco2, 2) if premium_per_tco2 is not None else None),
        "total_premium_for_volume": round(total_premium, 2),
        "volume_tonnes": volume_tonnes,
        "breakdown": breakdown,
    }

# ---------------- Scenario Analysis ----------------

def run_grid_search(include_export: bool = True):
    """
    Run grid search across multiple parameter combinations.
    
    Args:
        include_export: If True, includes export market scenarios (EU, Korea, Japan).
                       If False, only runs domestic scenarios.
    """
    # Define ranges for parameters
    scenarios = {
        "product_type": ["HRC", "GI", "TMT", "Other"],
        "baseline_emission": [2.36],
        "product_emission": [0.0, 0.6, 1.2, 1.8],  # Zero to reduced carbon
        "abatement_cost_per_tco2": [3000, 5000, 7000],  # Low, Mid, High cost
        "project_lifetime_years": [10],
        "verification_cost_per_year": [20_000_000],
        "annual_steel_production_tonnes": [100_000],
        "willingness_to_pay_multiplier": [1.0, 1.1, 1.2],  # 0%, 10%, 20% markup
        "customer_segment": ["automotive", "construction", "other"],
        "allocation_method": ["physical", "certificate"],
        "volume_tonnes": [1000],
    }
    
    # Add export markets if requested
    if include_export:
        scenarios["export_market"] = ["Domestic", "EU (CBAM)", "South Korea", "Japan"]
    else:
        scenarios["export_market"] = ["Domestic"]

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
        row["premium_per_tonne_steel"] = output["premium_per_tonne_steel"]
        row["premium_per_tCO2"] = output["premium_per_tCO2"]
        row["total_premium_for_volume"] = output["total_premium_for_volume"]
        
        # Add breakdown metrics
        row.update(output['breakdown'])
        
        results.append(row)

    df = pd.DataFrame(results)
    return df


def print_summary(df: pd.DataFrame):
    """Print summary statistics from the analysis."""
    
    print("\n" + "="*60)
    print("SUMMARY STATISTICS")
    print("="*60)
    
    # Overall stats
    print(f"\nTotal scenarios analyzed: {len(df)}")
    print(f"Premium range: ₹{df['premium_per_tonne_steel'].min():,.0f} - ₹{df['premium_per_tonne_steel'].max():,.0f} per tonne")
    
    # By export market
    print("\n--- Premium by Export Market ---")
    market_stats = df.groupby('export_market')['premium_per_tonne_steel'].agg(['mean', 'min', 'max'])
    print(market_stats.round(0))
    
    # By product type
    print("\n--- Premium by Product Type ---")
    product_stats = df.groupby('product_type')['premium_per_tonne_steel'].agg(['mean', 'min', 'max'])
    print(product_stats.round(0))
    
    # By customer segment
    print("\n--- Premium by Customer Segment ---")
    segment_stats = df.groupby('customer_segment')['premium_per_tonne_steel'].agg(['mean', 'min', 'max'])
    print(segment_stats.round(0))
    
    # Max premium scenario
    max_idx = df['premium_per_tonne_steel'].idxmax()
    print("\n--- Highest Premium Scenario ---")
    print(df.loc[max_idx, ['product_type', 'product_emission', 'export_market', 
                           'customer_segment', 'premium_per_tonne_steel', 'premium_per_tCO2']])
    
    # Min premium scenario (excluding zero CO2 savings)
    df_nonzero = df[df['co2_savings_per_t'] > 0]
    if not df_nonzero.empty:
        min_idx = df_nonzero['premium_per_tonne_steel'].idxmin()
        print("\n--- Lowest Premium Scenario (with CO2 savings) ---")
        print(df_nonzero.loc[min_idx, ['product_type', 'product_emission', 'export_market',
                                        'customer_segment', 'premium_per_tonne_steel', 'premium_per_tCO2']])


if __name__ == "__main__":
    # Run full grid search including export markets
    df_results = run_grid_search(include_export=True)
    
    # Save to CSV
    output_file = "green_steel_scenarios.csv"
    df_results.to_csv(output_file, index=False)
    
    print(f"\nAnalysis complete. Results saved to {output_file}")
    
    # Print summary
    print_summary(df_results)
    
    # Show sample results
    print("\n" + "="*60)
    print("SAMPLE RESULTS")
    print("="*60)
    
    # Sample: EU CBAM scenarios for HRC
    print("\n--- EU CBAM Export Scenarios (HRC, Automotive) ---")
    eu_hrc = df_results[
        (df_results['export_market'] == 'EU (CBAM)') & 
        (df_results['product_type'] == 'HRC') &
        (df_results['customer_segment'] == 'automotive')
    ][['product_emission', 'abatement_cost_per_tco2', 'domestic_premium_per_t', 
       'export_carbon_component', 'premium_per_tonne_steel']].head(10)
    print(eu_hrc.to_string(index=False))
    
    # Compare domestic vs export for same base scenario
    print("\n--- Domestic vs Export Comparison (HRC, emission=0.6, abatement=5000) ---")
    comparison = df_results[
        (df_results['product_type'] == 'HRC') &
        (df_results['product_emission'] == 0.6) &
        (df_results['abatement_cost_per_tco2'] == 5000) &
        (df_results['customer_segment'] == 'automotive') &
        (df_results['allocation_method'] == 'physical')
    ][['export_market', 'domestic_premium_per_t', 'carbon_price_export', 
       'export_carbon_component', 'premium_per_tonne_steel']]
    print(comparison.to_string(index=False))
