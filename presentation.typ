#set page(
  paper: "a4",
  margin: (x: 1.5cm, y: 1.5cm),
)
#set text(font: "Roboto", size: 10pt)
#set par(justify: true)

// --- Styling Definitions ---
#let section-header(title, color) = {
  block(fill: color.lighten(80%), width: 100%, inset: 8pt, radius: 4pt)[
    #text(weight: "bold", size: 14pt, fill: color)[#title]
  ]
}

#let cue-box(time, title, content) = {
  box(width: 100%, inset: (y: 6pt))[
    #grid(
      columns: (15%, 85%),
      gutter: 10pt,
      align(right)[#text(weight: "bold", fill: gray)[#time]],
      [
        #text(weight: "bold")[#title] \
        #content
      ]
    )
  ]
}

#let math-note(title, formula, explanation) = {
  block(stroke: (left: 2pt + gray), inset: (left: 10pt), width: 100%)[
    *#title* \
    #formula
    #text(style: "italic", size: 9pt)[#explanation]
  ]
}

#let qa-block(q, a) = {
  block(fill: luma(245), width: 100%, inset: 8pt, radius: 4pt)[
    *Q:* #q \
    *A:* #a
  ]
}

// ==========================================
// DOCUMENT START
// ==========================================

#align(center)[
  #text(size: 18pt, weight: "black")[Green Steel Pricing Engine: Presenter Cheat Sheet] \
  #text(size: 11pt, style: "italic")[Narrative Flow, Live Demo & Technical Defense]
]

#v(1em)

// ------------------------------------------
// SECTION 1: THE NARRATIVE (Script Cues)
// ------------------------------------------
#section-header("1. Narrative & Demo Flow", blue)

#cue-box("0:00 - 0:15", "The Hook (Problem/Solution)", [
  Start: The hurdle isn't making green steel—it is *pricing* it. \
  Goal: Move from *arbitrary markups* to a *transparent, market-linked engine*.
])

#cue-box("0:15 - 0:45", "The Methodology (Two Pillars)", [
  1. *Lifecycle-Based:* No upfront shock. Costs are amortized over project life. \
  2. *Segment-Smart:* We distinguish Automotive (High WTP) from Construction.
])

#line(stroke: 0.5pt + gray)

#cue-box("0:45 - 1:15", "The Live Demo (Web App)", [
  #table(
    columns: (auto, 1fr),
    stroke: none,
    inset: 4pt,
    [*1. Setup*], [Select *HRC* + *Automotive*. Note Baseline Emission (2.36).],
    [*2. Inputs*], [Enter Green Emission (*1.50*) → Savings = 0.86. Add Abatement (*₹5,000*).],
    [*3. Logic*], [We don't charge 5000 upfront. We amortize it over 15 years. Verify cost (₹200/ton) added. Apply multipliers (WTP: 1.3, Segment: 1.2, Allocation: 1.15 = 1.794).],
    [*4. Export*], [Select *EU (CBAM)*. Carbon Price loads (₹6,500).],
    [*5. Result*], [Domestic: *₹873* | Export Component: *₹5,590* | Export Premium: *₹6,463/ton*]
  )
])

#v(1em)

// ------------------------------------------
// SECTION 2: THE MATH (Deep Dive Notes)
// ------------------------------------------
#section-header("2. The Math (Technical Notes)", orange)

#grid(
  columns: (1fr, 1fr),
  gutter: 15pt,
  [
    #math-note("1. CO2 Savings", 
      $Delta E = E_("baseline") - E_("green")$, 
      "Ex: 2.36 - 1.50 = 0.86 tCO2 saved."
    )
    
    #v(5pt)
    
    #math-note("2. Amortized Abatement (The Floor)",
      $C_("abate") = (P_("cost") times Delta E) / L_("years")$,
      "Ex: (₹5,000 × 0.86) / 15 = ₹287/ton."
    )

    #v(5pt)

    #math-note("3. Verification Cost",
      $C_("ver") = C_("fixed") / V_("annual")$,
      "Ex: ₹20M / 100k tons = ₹200/ton. Base = ₹287 + ₹200 = ₹487."
    )
  ],
  [
    #math-note("4. The Multiplier (Compound)",
      $M_("total") = M_("wtp") times M_("seg") times M_("alloc")$,
      "Ex: 1.3 × 1.2 × 1.15 = 1.794. Domestic = ₹487 × 1.794 = ₹873."
    )

    #v(5pt)

    #math-note("5. Export Component (CBAM)",
      $P_("exp") = Delta E times P_("carbon") times (1 - f_("free"))$,
      "Ex: 0.86 × ₹6,500 = ₹5,590. Export Premium = ₹873 + ₹5,590 = ₹6,463."
    )
  ]
)

#v(1em)

// ------------------------------------------
// SECTION 3: JURY Q&A STRATEGY
// ------------------------------------------
#section-header("3. Anticipated Q&A", green)

#qa-block(
  "Why is the premium for HRC different than TMT?",
  "It is based on 'Baseline Emissions' and 'Willingness to Pay.' HRC has a higher baseline (more savings potential) and goes into Automotive (higher margin)."
)

#v(5pt)

#qa-block(
  "Why are you compounding the multipliers? Isn't that inflating the price?",
  "Multiplicative factors reflect exponential complexity. Delivering 'Physical' green steel to an 'Automotive' client is significantly harder than a certificate for construction."
)

#v(5pt)

#qa-block(
  "How does the model handle the 'Export' price difference?",
  "It maintains parity. If a client buys dirty steel, they pay the CBAM tax. If they buy Green Steel, they pay us. The 'Total Cost of Ownership' is identical."
)

#v(5pt)

#qa-block(
  "Is the verification cost fixed? What if volume drops?",
  "It is dynamic. Formula = Fixed Cost / Annual Volume. If volume drops, the per-ton premium rises to cover the fixed certification overhead."
)