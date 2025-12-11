# Green Steel Premium Calculator - Mathematical Model Documentation

## Overview

The calculator determines the **premium price** customers should pay for green steel (lower emissions) compared to conventional steel, based on cost-plus pricing with market adjustments.

## Inputs

### Primary Emissions Parameters
- **`baseline_emission`** (tCO₂/t): CO₂ emissions from conventional steel production
- **`product_emission`** (tCO₂/t): CO₂ emissions from the green steel product

### Cost Parameters
- **`abatement_cost_per_tco2`** (₹/tCO₂): Cost to reduce emissions by one tonne of CO₂
- **`verification_cost_per_tonne`** (₹/t): Fixed cost per tonne for verification and administration
- **`margin_pct`** (%): Profit margin percentage

### Market Adjustment Parameters
- **`customer_segment`**: "automotive", "construction", or "other"
- **`allocation_method`**: "physical" or "certificate" 
- **`cbam_avoidance_per_tco2`** (₹/tCO₂): Value customers gain from avoiding CBAM (Carbon Border Adjustment Mechanism) costs
- **`willingness_to_pay_multiplier`**: Market adjustment factor (e.g., 1.2 = 20% higher willingness)

### Volume & Constraints
- **`volume_tonnes`** (t): Total volume of steel
- **`floor_premium_per_t`** (₹/t): Minimum premium per tonne
- **`ceiling_premium_per_t`** (₹/t): Maximum premium per tonne (optional)

### Metadata
- **`product_type`**: "HRC", "GI", or "Other" (for tracking only)

---

## Mathematical Formulas

### Step 1: CO₂ Savings Calculation

$$\text{CO₂ Savings} = \max(0, \text{baseline\_emission} - \text{product\_emission})$$

### Step 2: Cost Components

**Abatement Component:**
$$\text{Abatement Cost} = \text{CO₂ Savings} \times \text{abatement\_cost\_per\_tCO₂}$$

**Verification Component:**
$$\text{Verification Cost} = \text{verification\_cost\_per\_tonne}$$

**Base Cost Stack:**
$$\text{Base Cost} = \text{Abatement Cost} + \text{Verification Cost}$$

### Step 3: Margin Addition

$$\text{Margin Component} = \text{Base Cost} \times \frac{\text{margin\_pct}}{100}$$

### Step 4: Customer Value Offset

$$\text{Customer Value Offset} = \text{CO₂ Savings} \times \text{cbam\_avoidance\_per\_tCO₂}$$

This represents the value customers capture by avoiding CBAM taxes, which reduces the premium they'll pay.

### Step 5: Pre-Multiplier Premium

$$\text{Pre-Multiplier Premium} = \text{Base Cost} + \text{Margin Component} - \text{Customer Value Offset}$$

### Step 6: Segment Multiplier Calculation

$$\text{Segment Multiplier} = \text{allocation\_factor} \times \text{customer\_segment\_factor}$$

Where:
- **Allocation factor**: 1.15 for "physical", 1.0 for "certificate"
- **Segment factor**: 1.2 for "automotive", 1.05 for "construction", 1.0 for "other"

### Step 7: Final Premium Calculation

$$\text{Premium per Tonne} = \text{Pre-Multiplier Premium} \times \text{willingness\_to\_pay} \times \text{Segment Multiplier}$$

**With floor and ceiling constraints:**
$$\text{Final Premium} = \min(\max(\text{Premium}, \text{floor}), \text{ceiling})$$

### Step 8: Derived Metrics

**Premium per tCO₂ saved:**
$$\text{Premium per tCO₂} = \frac{\text{Premium per Tonne}}{\text{CO₂ Savings}}$$

**Total premium for volume:**
$$\text{Total Premium} = \text{Premium per Tonne} \times \text{volume\_tonnes}$$

---

## Process Flow Diagram

```mermaid
graph TD
    A[Input: Baseline & Product Emissions] --> B[Calculate CO₂ Savings]
    B --> C{Savings > 0?}
    C -->|Yes| D[Abatement Cost = Savings × Cost per tCO₂]
    C -->|No| E[Abatement Cost = 0]
    D --> F[Add Verification Cost]
    E --> F
    F --> G[Base Cost Stack]
    G --> H[Add Margin %]
    H --> I[Calculate Customer Value Offset<br/>CBAM Avoidance]
    I --> J[Pre-Multiplier Premium =<br/>Base + Margin - Offset]
    
    K[Input: Allocation Method] --> L[Calculate Segment Multiplier]
    M[Input: Customer Segment] --> L
    
    J --> N[Apply Multipliers:<br/>WTP × Segment]
    L --> N
    O[Input: WTP Multiplier] --> N
    
    N --> P[Premium per Tonne]
    
    Q[Input: Floor/Ceiling] --> R{Apply Constraints}
    P --> R
    
    R --> S[Final Premium per Tonne]
    S --> T[Calculate Premium per tCO₂]
    S --> U[Calculate Total Premium<br/>Premium × Volume]
    
    style B fill:#e1f5ff
    style G fill:#fff4e1
    style L fill:#ffe1f0
    style S fill:#c8e6c9
    style T fill:#c8e6c9
    style U fill:#c8e6c9
```

## Data Flow with Example Values

```mermaid
flowchart LR
    subgraph Inputs
        A1[Baseline: 2.0 tCO₂/t]
        A2[Product: 0.8 tCO₂/t]
        A3[Abatement: ₹5000/tCO₂]
        A4[Verification: ₹200/t]
        A5[Margin: 20%]
        A6[CBAM: ₹6000/tCO₂]
        A7[Volume: 1000t]
        A8[Segment: Automotive]
        A9[Allocation: Physical]
    end
    
    subgraph Processing
        B1[CO₂ Savings: 1.2 tCO₂/t]
        B2[Abatement: ₹6000/t]
        B3[Base Cost: ₹6200/t]
        B4[With Margin: ₹7440/t]
        B5[After Offset: ₹240/t]
        B6[Seg Mult: 1.38]
        B7[Premium: ₹331/t]
    end
    
    subgraph Outputs
        C1[Premium/tonne: ₹331]
        C2[Premium/tCO₂: ₹276]
        C3[Total: ₹331,000]
    end
    
    A1 --> B1
    A2 --> B1
    B1 --> B2
    A3 --> B2
    B2 --> B3
    A4 --> B3
    B3 --> B4
    A5 --> B4
    B4 --> B5
    A6 --> B5
    B5 --> B7
    A8 --> B6
    A9 --> B6
    B6 --> B7
    B7 --> C1
    C1 --> C2
    C1 --> C3
    A7 --> C3
    
    style B1 fill:#e1f5ff
    style B3 fill:#fff4e1
    style B6 fill:#ffe1f0
    style C1 fill:#c8e6c9
    style C2 fill:#c8e6c9
    style C3 fill:#c8e6c9
```    

## COmponent Breakdown

```mermaid
graph TB
    subgraph Cost Structure
        A[Abatement Cost<br/>₹6000] --> D[Base Cost Stack<br/>₹6200]
        B[Verification Cost<br/>₹200] --> D
        D --> E[+ Margin 20%<br/>₹1240]
        E --> F[Gross Premium<br/>₹7440]
        F --> G[- CBAM Offset<br/>₹7200]
        G --> H[Net Pre-Multiplier<br/>₹240]
    end
    
    subgraph Multipliers
        I[Allocation: Physical<br/>×1.15] --> K[Combined<br/>×1.38]
        J[Segment: Automotive<br/>×1.20] --> K
    end
    
    H --> L[Apply Multipliers]
    K --> L
    L --> M[Final Premium<br/>₹331/t]
    
    style D fill:#fff4e1
    style F fill:#ffebcc
    style H fill:#e1f5ff
    style K fill:#ffe1f0
    style M fill:#c8e6c9
```