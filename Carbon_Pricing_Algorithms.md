# Carbon Pricing Algorithms for the Steel Sector

Based on the industry report and analysis, this document outlines carbon pricing algorithms for five specific scenarios.

## 1. The Case of Europe

### Explanation
In Europe, steel producers operate under the **EU Emissions Trading System (EU ETS)**. They must surrender allowances for their **Scope 1** (direct) emissions. **Scope 2** (indirect electricity) costs are passed through in power prices. Historically, producers received **Free Allowances** to prevent carbon leakage, but these are being phased out (ending by roughly 2030-2034).

For imports into the EU, the **Carbon Border Adjustment Mechanism (CBAM)** applies. Importers must pay the difference between the EU ETS price and any carbon price paid in the country of origin.

**Algorithm Logic:**
1.  Calculate **Scope 1 Cost**: (Scope 1 Emissions - Free Allowances) × EU ETS Price.
2.  Calculate **Scope 2 Cost**: Scope 2 Emissions × (Pass-through Carbon Cost in Electricity).
3.  **Total Domestic Cost** = Scope 1 Cost + Scope 2 Cost.
4.  **CBAM (for imports):** (Embedded Emissions × EU ETS Price) - (Carbon Price Paid at Origin).

### Inputs and Outputs
*   **Inputs:**
    *   $E_{scope1}$: Scope 1 Emissions (tCO2/t Steel)
    *   $E_{scope2}$: Scope 2 Emissions (tCO2/t Steel)
    *   $P_{ETS}$: EU ETS Allowance Price (€/tCO2)
    *   $A_{free}$: Free Allowances allocated (tCO2/t Steel)
    *   $P_{elec\_carbon}$: Carbon cost component in electricity price (€/tCO2)
*   **Output:**
    *   $C_{total}$: Total Carbon Cost per Tonne of Steel (€/t)

### Flowchart

```mermaid
flowchart TD
    A[Start] --> B{Is Producer in EU?}
    B -- Yes --> C[Get Scope 1 Emissions E1]
    C --> D[Get Free Allowances A_free]
    D --> E["Calculate Net Scope 1: max{0, E1 - $$A_{free}$$}"]
    E --> F[Cost Scope 1 = Net Scope 1 * P_ETS]
    F --> G[Get Scope 2 Emissions E2]
    G --> H[Cost Scope 2 = E2 * P_elec_carbon]
    H --> I[Total Cost = Cost Scope 1 + Cost Scope 2]
    B -- No (Importer) --> J[Calculate Embedded Emissions E_emb]
    J --> K[Calculate EU Carbon Cost = E_emb * P_ETS]
    K --> L[Subtract Carbon Price Paid at Origin]
    L --> M[Pay CBAM Certificate Cost]
    I --> N[End]
    M --> N
```

---

## 2. The Case of Japan and South Korea

### Explanation
This region has a split approach:
*   **South Korea (K-ETS):** A mandatory Cap-and-Trade system covering Scope 1 and indirect Scope 2. Producers receive free allowances (KAUs) but allocations are shrinking (Phase 4). They can use limited offsets (KOCs).
*   **Japan:** Currently relies on a low **Carbon Tax** (Tax for Climate Change Mitigation) and a voluntary **GX-ETS** (transitioning to mandatory). Producers may use **J-Credits** to offset emissions. Incentives exist for "Green Steel" in the auto sector.

### Inputs and Outputs
*   **Inputs (Korea):**
    *   $E_{total}$: Total Emissions (Scope 1 + 2)
    *   $A_{free}$: Free Allowances (KAUs)
    *   $P_{KAU}$: K-ETS Price (KRW/tCO2)
    *   $L_{offset}$: Max Offset Limit (%)
*   **Inputs (Japan):**
    *   $E_{fuel}$: Emissions from Fuel (Scope 1)
    *   $T_{carbon}$: Carbon Tax Rate (¥/tCO2)
    *   $P_{GX}$: GX-ETS / J-Credit Price (if participating)
*   **Output:**
    *   $C_{total}$: Total Carbon Cost per Tonne of Steel

### Flowchart

```mermaid
flowchart TD
    A[Start] --> B{Country?}
    
    %% South Korea Path
    B -- South Korea --> C[Calculate Total Emissions E_tot]
    C --> D[Subtract Free Allowances A_free]
    D --> E{Deficit > 0?}
    E -- Yes --> F[Check Offset Limit L_offset]
    F --> G[Buy Offsets KOC up to Limit]
    G --> H[Buy Remaining KAUs at Market Price]
    E -- No --> I[Sell Surplus KAUs]
    H --> J[Total Cost = Cost of KAUs + Cost of Offsets]
    I --> J
    
    %% Japan Path
    B -- Japan --> K[Calculate Fuel Emissions E_fuel]
    K --> L[Apply Carbon Tax: E_fuel * T_carbon]
    L --> M{Participating in GX-ETS?}
    M -- Yes --> N[Compare Emissions vs Target]
    N --> O{Exceeds Target?}
    O -- Yes --> P[Buy J-Credits / Allowances]
    O -- No --> Q[Sell Excess Credits]
    P --> R[Total Cost = Tax + Credit Cost]
    Q --> R
    M -- No --> S[Total Cost = Tax Only]
    S --> R
    
    J --> T[End]
    R --> T
```

---

## 3. The Case of China

### Explanation
China operates a **National ETS** that is expanding to cover steel. Currently, it is an intensity-based system where allowances are **freely allocated** based on benchmarks (e.g., tCO2 per tonne of product).
*   If a plant is more efficient than the benchmark, it earns surplus allowances.
*   If less efficient, it must buy allowances.
*   **CCERs (China Certified Emission Reductions)** can be used to offset a small percentage (approx. 5%) of compliance obligations.

### Inputs and Outputs
*   **Inputs:**
    *   $Q_{prod}$: Production Output (tonnes)
    *   $E_{actual}$: Actual Emissions (tCO2)
    *   $B_{mark}$: Benchmark Intensity (tCO2/t product)
    *   $P_{ETS}$: China ETS Price (CNY/tCO2)
    *   $P_{CCER}$: CCER Offset Price
*   **Output:**
    *   $C_{compliance}$: Net Compliance Cost (or Revenue)

### Flowchart

```mermaid
flowchart TD
    A[Start] --> B[Measure Actual Emissions E_actual]
    B --> C[Determine Benchmark B_mark]
    C --> D[Calculate Free Allocation: A_free = Q_prod * B_mark]
    D --> E[Calculate Balance: Gap = E_actual - A_free]
    E --> F{"Gap > 0? \n(Deficit)"}
    F -- Yes --> G[Can use CCERs?]
    G -- Yes --> H[Buy CCERs up to 5% Limit]
    H --> I[Buy ETS Allowances for Remainder]
    G -- No --> J[Buy ETS Allowances for Full Gap]
    F -- No \n(Surplus) --> K[Sell Surplus Allowances]
    I --> L[Calculate Net Cost]
    J --> L
    K --> L
    L --> M[End]
```

---

## 4. The Case of India

### Explanation
India currently has **no explicit national carbon tax** or mandatory ETS for steel (though the **CCTS** is in development). The primary carbon-related cost driver is the **EU CBAM** for exports.
*   **Domestic Sales:** Implicit carbon price is effectively zero (legacy coal cess removed).
*   **Exports to EU:** Must pay the EU CBAM charge, which is the EU ETS price minus any domestic carbon price paid (currently 0).

### Inputs and Outputs
*   **Inputs:**
    *   $Q_{dom}$: Quantity sold domestically
    *   $Q_{exp}$: Quantity exported to EU
    *   $E_{int}$: Emission Intensity (tCO2/t Steel)
    *   $P_{EU}$: EU ETS Price
    *   $P_{dom}$: Domestic Carbon Price (currently ~0)
*   **Output:**
    *   $C_{weighted}$: Weighted Average Carbon Cost per Tonne

### Flowchart


```mermaid
flowchart TD
    A["Start"] --> B["Identify Market Destination"]
    B --> C{"Domestic Market?"}
    C -- Yes --> D["Carbon Cost = 0 \n(Pending CCTS implementation)"]
    C -- "No (Export to EU)" --> E["Calculate Embedded Emissions E_int"]
    E --> F["Identify EU ETS Price P_EU"]
    F --> G["Identify Domestic Price P_dom \n(Currently 0)"]
    G --> H["Calculate CBAM Liability: \nCost = E_int * (P_EU - P_dom)"]
    D --> I["Total Cost per Tonne"]
    H --> I
    I --> J["End"]
```

---

## 5. Proposed Algorithm: Green Premium Calculation

### Explanation
This algorithm calculates the **Green Premium**—the additional price a low-carbon steel product should command (or the cost gap it needs to bridge). It accounts for regional carbon prices, the "Green" value in specific industries (Industry Factor), avoided CBAM costs, and potential revenue from carbon credits.

**Formula:**
$$ \text{Premium}_{\text{per tonne}} = \Delta E \times [ (P_{\text{region}} + P_{\text{CBAM}}) \times f_{\text{ind}} - P_{\text{credit}} ] $$

Where:
*   $\Delta E$: Emissions saved per tonne (Conventional - Low Carbon).
*   $P_{\text{region}}$: Local carbon price avoided.
*   $P_{\text{CBAM}}$: Avoided border tax (if applicable).
*   $f_{\text{ind}}$: Industry willingness-to-pay factor (>1).
*   $P_{\text{credit}}$: Revenue from selling carbon credits.

### Inputs and Outputs
*   **Inputs:**
    *   $E_{conv}, E_{green}$: Emissions of conventional vs. green steel
    *   $P_{region}$: Local Carbon Price
    *   $P_{CBAM}$: Target Market Carbon Price (if exporting)
    *   $f_{ind}$: Industry Factor (e.g., 1.2 for Auto)
    *   $P_{credit}$: Value of Carbon Credits
    *   $L, Y$: Project Lifetime (years), Annual Production
*   **Output:**
    *   $Prem_{tonne}$: Premium per Tonne ($)
    *   $Prem_{life}$: Total Lifecycle Premium ($)

### Flowchart

```mermaid
flowchart TD
    A[Start] --> B[Input: Emissions E_conv, E_green]
    B --> C[Calculate Savings: dE = E_conv - E_green]
    C --> D[Input: Market Prices P_region, P_CBAM]
    D --> E[Input: Industry Factor f_ind]
    E --> F[Input: Credit Value P_credit]
    
    F --> G["Calculate Effective Carbon Value: \n V = (P_region + P_CBAM) * f_ind - P_credit"]
    G --> H["Calculate Premium per Tonne: \n P_tonne = dE * V"]
    
    H --> I[Input: Project Life L, Annual Output Y]
    I --> J["Calculate Lifecycle Premium: \n P_life = P_tonne * Y * L"]
    
    J --> K[Output: Green Premium Pricing]
    K --> L_End[End]
```

