# Green Premium Calculator Logic

## 1. Logic Explanation

The calculator determines the "Green Premium" (the extra price a customer pays for low-carbon steel) using two different approaches simultaneously:

1.  **Value-Based Approach:** Calculates the premium based on the **regulatory cost avoided** (e.g., not paying carbon taxes) and the **market value** created for the customer (e.g., Scope 3 reduction value).
2.  **Cost-Plus Approach:** Calculates the premium based on the **production cost increase** (abatement technology) plus a commercial margin.

Both approaches are adjusted by a unified **Industry Factor ($f_{ind}$)**, which represents commercial leverage based on the customer segment, allocation method, and willingness to pay.

## 2. Example Scenario: "Automotive Client in Europe"

Let's trace the numbers for a hypothetical deal with a European car manufacturer.

**Inputs:**
*   **Emissions Savings ($\Delta E$):**
    *   Conventional Steel ($E_{conv}$): 2.2 tCO2/t
    *   Green Steel ($E_{green}$): 0.5 tCO2/t
    *   **$\Delta E$ = 1.7 tCO2/t**
*   **Market Factors:**
    *   Segment: **Automotive** (Multiplier: 1.2x)
    *   Allocation: **Physical** (Multiplier: 1.15x)
    *   Willingness to Pay (WTP): **20%** (Multiplier: 1.2x)
*   **Regulatory Costs:**
    *   EU ETS Price ($P_{region}$): **$70/tCO2**
*   **Production Costs:**
    *   Abatement Cost: **$60/tCO2**
    *   Verification Cost: **$2.50/t steel**

**Step-by-Step Transformation:**

1.  **Calculate Industry Factor ($f_{ind}$):**
    $$f_{ind} = 1.2 \text{ (Auto)} \times 1.15 \text{ (Physical)} \times 1.2 \text{ (WTP)} = \mathbf{1.656}$$

2.  **Path A: Value-Based Premium**
    *   *Effective Carbon Value:* $(70 + 0) \times 1.656 - 0 = \$115.92 / tCO2$
    *   *Final Premium:* $1.7 \text{ (Savings)} \times 115.92 = \mathbf{\$197.06 / t \text{ steel}}$

3.  **Path B: Cost-Plus Premium**
    *   *Base Cost:* $(1.7 \times 60) + 2.5 = \$104.50$
    *   *Final Premium:* $104.50 \times 1.656 = \mathbf{\$173.05 / t \text{ steel}}$

## 3. Data Flow Diagram (Mermaid)

```mermaid
graph TD
    subgraph Inputs
        E_conv[Conventional Emissions<br>2.2]
        E_green[Green Emissions<br>0.5]
        Seg[Segment: Auto<br>x1.2]
        Alloc[Allocation: Physical<br>x1.15]
        WTP[WTP: 20%<br>x1.2]
        Reg[EU ETS Price<br>$70]
        Abate[Abatement Cost<br>$60]
        Verif[Verification Cost<br>$2.5]
    end

    subgraph Transformations
        DeltaE(Delta E<br>1.7 tCO2)
        Find(Industry Factor f_ind<br>1.656)
        
        %% Connections
        E_conv --> DeltaE
        E_green --> DeltaE
        Seg --> Find
        Alloc --> Find
        WTP --> Find
    end

    subgraph Value_Based_Logic
        ValCalc["Effective Carbon Value<br>($70 * 1.656)"]
        ValPrem["Premium Calculation<br>(1.7 * $115.92)"]
        
        Reg --> ValCalc
        Find --> ValCalc
        ValCalc --> ValPrem
        DeltaE --> ValPrem
    end

    subgraph Cost_Plus_Logic
        CostCalc["Base Cost Calculation<br>(1.7 * $60) + $2.5"]
        CostPrem["Margin Application<br>($104.5 * 1.656)"]
        
        Abate --> CostCalc
        Verif --> CostCalc
        DeltaE --> CostCalc
        CostCalc --> CostPrem
        Find --> CostPrem
    end

    subgraph Outputs
        Out1([Value-Based Premium<br>$197.06 /t])
        Out2([Cost-Plus Premium<br>$173.05 /t])
        
        ValPrem --> Out1
        CostPrem --> Out2
    end

    style Out1 fill:#d4f1f9,stroke:#333,stroke-width:2px
    style Out2 fill:#e1f7d5,stroke:#333,stroke-width:2px
    style Find fill:#fff3cd,stroke:#333
```
## 4. Updated Logic: CAPEX Amortization (Project Finance)

The calculator has been updated to refine the **Cost-Plus Approach** by incorporating **Capital Expenditure (CAPEX)** amortization. This ensures that the massive upfront investments required for green steel plants (e.g., Hydrogen DRI) are spread over the project`s life and reflected in the per-tonne premium.

### New Inputs
*   **Upfront CAPEX ($):** Total investment required for the green transition.
*   **Cost of Capital (r):** The interest rate or discount rate.
*   **Project Life (n):** Duration of the project in years.
*   **Annual Production:** Expected output in tonnes per year.

### Amortization Formula
The tool uses the **Capital Recovery Factor (CRF)** to convert the lump-sum CAPEX into an equivalent annual cost.

1.  **Calculate CRF:**
    $$CRF = \frac{r(1+r)^n}{(1+r)^n - 1}$$
2.  **Annualized CAPEX:**
    $$Annual\_CAPEX = Upfront\_CAPEX \times CRF$$
3.  **CAPEX per Tonne:**
    $$CAPEX_{unit} = \frac{Annual\_CAPEX}{Annual\_Production}$$
4.  **Revised Base Cost (Cost-Plus):**
    $$Base\_Cost = (\Delta E \times OPEX_{abatement}) + Verification + CAPEX_{unit}$$

### Updated Data Flow (Mermaid)

```mermaid
graph TD
    subgraph Inputs
        DeltaE["Delta E (Savings)"]
        Opex[Abatement OPEX]
        Verif[Verification Cost]
        Capex[Upfront CAPEX]
        Rate[Interest Rate %]
        Life[Project Life]
        Prod[Annual Production]
        IndFactor[Industry Factor f_ind]
    end

    subgraph Financial_Modeling
        CRF(Calculate CRF<br>Capital Recovery Factor)
        AnnCapex(Annualized CAPEX<br>Capex * CRF)
        UnitCapex(CAPEX per Tonne<br>Annual / Production)
        
        Rate --> CRF
        Life --> CRF
        Capex --> AnnCapex
        CRF --> AnnCapex
        AnnCapex --> UnitCapex
        Prod --> UnitCapex
    end

    subgraph Cost_Plus_Logic
        BaseCost["Base Cost Calculation<br>(Delta E * OPEX) + Verif + CAPEX/t"]
        FinalPrem[Final Cost-Plus Premium<br>Base Cost * f_ind]
        
        DeltaE --> BaseCost
        Opex --> BaseCost
        Verif --> BaseCost
        UnitCapex --> BaseCost
        BaseCost --> FinalPrem
        IndFactor --> FinalPrem
    end

    subgraph Output
        Result(["Cost-Plus Premium ($/t)"])
        FinalPrem --> Result
    end

    style UnitCapex fill:#ffdfba,stroke:#333
    style FinalPrem fill:#e1f7d5,stroke:#333,stroke-width:2px
```
