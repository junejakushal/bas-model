# Green Steel Premium Calculator -- Key Parameters and Pricing Logic

**Abatement cost per tCO₂:** Recent analyses suggest carbon abatement
costs in steel production on the order of \~\$50--\$100 per tonne of
CO₂. For example, an Indian study notes that if carbon capture costs
\~\$92/tCO₂, near-zero steel costs \~40--70% more, whereas at \$50/tCO₂
the premium falls to
15--25%[\[1\]](https://www.ceew.in/publications/how-can-india-decarbonise-for-net-zero-steel-industry#:~:text=,depending%20on%20the%20production%20route).
International experience shows public incentives for green steel vary
widely (\$110--\$1,168/tCO₂
abated[\[2\]](https://ieefa.org/articles/india-needs-targeted-public-finance-scale-green-steel#:~:text=International%20evidence%20shows%20public%20costs,alone%20cannot%20drive%20the%20transition)),
implying that a mid-range abatement cost assumption (\~\$100/tCO₂) is
reasonable for initial modeling. The algorithm should allow updating
this value as carbon prices and technologies evolve (e.g. India's carbon
scheme may target \~\$60/tCO₂ by
2030[\[3\]](https://www.rystadenergy.com/news/india-steel-europe-carbon-rules#:~:text=Currently%2C%20these%20companies%20are%20on,and%20India%27s%20high%20carbon%20intensity)).

**CBAM avoidance value:** To account for avoided carbon border taxes on
exports, we use an EU-like carbon price. Recent estimates show EU carbon
costs effectively add roughly €200--€225 per tonne of Indian steel
(about
\$220--\$245/t)[\[4\]](https://www.metalbook.com/blogs/cbam-and-the-future-of-indias-steel-exports/#:~:text=To%20understand%20CBAM%E2%80%99s%20commercial%20impact%2C,could%20be%20greater%20than%20%E2%82%AC220%2Ftonne).
Using the Indian steel emission intensity (\~2.36 tCO₂/t
steel[\[5\]](https://www.ceew.in/publications/how-can-india-decarbonise-for-net-zero-steel-industry#:~:text=the%20same%20year%2C%20equating%20to,alternative%20fuels%20and%20carbon%20management))
and a carbon price (\~€80/tCO₂), one obtains \~\$200+ per tonne. For the
domestic focus, we treat "CBAM avoidance" as the dollar-equivalent
carbon cost per tonne of conventional steel (≈\$200/t), reflecting the
premium customers might pay to avoid future carbon penalties. This value
should be revisable with updated carbon prices; for now we use \~\$200/t
steel (≈\$85--\$100/tCO₂) based on EU
prices[\[4\]](https://www.metalbook.com/blogs/cbam-and-the-future-of-indias-steel-exports/#:~:text=To%20understand%20CBAM%E2%80%99s%20commercial%20impact%2C,could%20be%20greater%20than%20%E2%82%AC220%2Ftonne)[\[3\]](https://www.rystadenergy.com/news/india-steel-europe-carbon-rules#:~:text=Currently%2C%20these%20companies%20are%20on,and%20India%27s%20high%20carbon%20intensity).

**Willingness-to-pay multipliers:** End users' willingness to pay extra
for green steel varies by segment. Reports find that committed buyers
(e.g. large automakers) pay premiums and tie long-term offtakes at
\~20--30% above
market[\[6\]](https://ieefa.org/articles/india-needs-targeted-public-finance-scale-green-steel#:~:text=Global%20project%20failures%20reveal%20a,production%20to%20final%20steel%20output).
For example, green-steel start-ups report targeting \~25% price premiums
for early customers (value-based
pricing)[\[7\]](https://www.mckinsey.com/capabilities/sustainability/our-insights/henrik-henriksson-rapidly-scaling-a-green-steel-start-up#:~:text=McKinsey%3A%20Green%20steel%20is%20going,pay%20more%20for%20your%20product).
In India, a \$210/t premium (for hydrogen-based DRI steel) translates to
+3.7% in construction cost, +5.2% in infrastructure and +4.1% in
automotive
costs[\[8\]](https://www.indiagreensteelcoalition.org/reports-articles/unlocking-green-steel-demand-in-india/#:~:text=Currently%2C%20the%20premium%20on%20green,of%20green%20hydrogen%20and%20the),
suggesting stronger WTP in automotive/infrastructure sectors. Hence we
recommend sector multipliers roughly in the range 1.0 (baseline, e.g.
price-sensitive construction) to 1.3 (high-end infrastructure/OEM
purchasers). These can be calibrated: e.g. 1.1× for automotive and 1.3×
for infrastructure relative to construction (based on the above
impacts)[\[8\]](https://www.indiagreensteelcoalition.org/reports-articles/unlocking-green-steel-demand-in-india/#:~:text=Currently%2C%20the%20premium%20on%20green,of%20green%20hydrogen%20and%20the).
(These are illustrative; actual WTP data is limited, so the model should
allow user-defined multipliers.) Importantly, surveys and analyses
emphasize segmentation -- "different sectors will command different
green
premiums"[\[9\]](https://www.crugroup.com/en/communities/thought-leadership/2024/how-will-the-green-steel-premia-be-determined/#:~:text=The%20willingness%20of%20consumers%20to,and%20commanding%20different%20green%20premium)[\[10\]](https://www.bcg.com/publications/2023/consumers-are-willing-to-pay-for-net-zero-production#:~:text=case,would%20set%20a%20low%20initial)
-- so the algorithm should apply distinct multipliers or rates by
customer type.

**Verification and other costs:** Any third-party verification or
certification costs (to prove steel is "green") should be amortized
similarly. For example, if a verification process costs \$X per plant
per year, include this annual cost divided by production volume.
Documentation and audit costs are typically a small fraction of steel
value, but should be included for completeness. We recommend adding a
fixed "verification cost" per tonne (e.g. \$1--\$5/t) amortized over the
project life.

# Amortized Premium Pricing Logic

The premium pricing model is updated to **spread abatement and
verification costs over the project lifecycle**. Key steps:

-   **Project lifetime input:** Allow the user to specify the project
    lifetime (years); default to 10 years if unspecified. This reflects
    a typical steel plant's capital amortization period.

-   **Annualized cost per tonne:** Compute the annual cost of
    decarbonization per tonne of steel as:

\\text{Annual Cost per tsteel} = \\frac{\\text{abatement_cost_per_tCO2}
\\times \\text{CO₂ intensity (tCO₂/tsteel)}}{\\text{lifetime}} +
\\frac{\\text{verification_cost_per_year}}{\\text{annual steel
production (t)}}

For simplicity, if abatement_cost is viewed as a one-time
capital-equipment cost per tCO₂ captured per year, dividing by life
spreads it out. Alternatively, if abatement_cost is interpreted as an
ongoing carbon tax, the /lifetime factor effectively distributes it
evenly. In either case, using a 10-year life divides upfront costs by
10.

-   **Premium calculation:** The **green-premium per tonne** is then the
    sum of amortized costs (above) plus any markup multiplier reflecting
    WTP. Formally:

```{=html}
<!-- -->
```
-   \\text{Premium} = \\Bigl(\\frac{\\text{abatement_cost_per_tCO2}
    \\times \\text{CO₂ intensity}}{\\text{lifetime}} +
    \\frac{\\text{verification_cost_per_year}}{\\text{annual
    output}}\\Bigr) \\times \\text{WTP multiplier}.
    For example, with abatement_cost\~\$100/tCO₂, CO₂ intensity\~2.36,
    life=10y: base cost ≈\$23.6/t; a 1.1× multiplier yields \~\$25.9/t
    premium. (These numbers are illustrative.)

```{=html}
<!-- -->
```
-   **Cost recovery vs. time:** This approach ensures that high upfront
    capex (e.g. for a hydrogen plant or CCUS system) is not front-loaded
    on year-1 steel price, but spread out. It also allows the user to
    enter a shorter or longer lifecycle (e.g. 20 years) if justified by
    technology lifetime.

-   **Example (with default values):** Assume abatement_cost=\$100/tCO₂,
    CO₂ intensity=2.36, lifetime=10y, verification=\$50k per year, plant
    output=100k t/yr (so \$0.50/t). Annual cost/t = \$(100×2.36)/10 +
    0.5 = \$23.6 + \$0.5 = \$24.1/t. With, say, a 1.1× sector
    multiplier, the premium \~ \$26.5/t.

This amortized logic is more realistic than a one-time addition, and
aligns with financial models (e.g. levelized cost). All parameters
(abatement cost, intensity, lifetime, verification) are inputs or
defaults and can be refined with actual project data.

# Comparison of Approaches and Algorithms

Several research and industry models exist for green-steel pricing.
Table 1 summarizes key differences in how each handles **carbon
abatement costs**, **customer segmentation**, and **pricing logic**:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Approach / Source**                                                                                                                                                                                                                                                                                                                                                                                                                                       **Carbon Abatement**                                                                                                                                                                                                                     **Customer Segmentation**                                                                                                                                                                                                          **Pricing Logic**
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **CRU "Green Premium" framework                                                                                                                                                                                                                                                                                                                                                                                                                             Models a **Steel Abatement Value (Steav)** -- the inherent value of reducing emissions. Uses carbon cost as floor, but market *pull* (demand from decarbonization targets) sets upper                                                    Emphasizes **segmented demand**. Different end-markets (automotive vs construction vs distribution) have distinct premium willingness. Recognizes heterogeneity -- e.g. OEMs pay more than commodity                               **Premium = perceived value above all costs.** Not limited by cost of decarbonization
  (2024)**[\[11\]](https://www.crugroup.com/en/communities/thought-leadership/2024/how-will-the-green-steel-premia-be-determined/#:~:text=A%20green%20premium%20is%20ultimately,any%20carbon%20taxes%2Femissions%20trading%20schemes)[\[9\]](https://www.crugroup.com/en/communities/thought-leadership/2024/how-will-the-green-steel-premia-be-determined/#:~:text=The%20willingness%20of%20consumers%20to,and%20commanding%20different%20green%20premium)   bound[\[12\]](https://www.crugroup.com/en/communities/thought-leadership/2024/how-will-the-green-steel-premia-be-determined/#:~:text=conducted%20with%20potential%20buyers%20of,any%20carbon%20taxes%2Femissions%20trading%20schemes).   buyers[\[9\]](https://www.crugroup.com/en/communities/thought-leadership/2024/how-will-the-green-steel-premia-be-determined/#:~:text=The%20willingness%20of%20consumers%20to,and%20commanding%20different%20green%20premium).      alone[\[13\]](https://www.crugroup.com/en/communities/thought-leadership/2024/how-will-the-green-steel-premia-be-determined/#:~:text=A%20green%20premium%20is%20ultimately,and%20future%20carbon%20costs%20or). Additional
                                                                                                                                                                                                                                                                                                                                                                                                                                                              Carbon costs (ETS, CBAM) define baseline.                                                                                                                                                                                                                                                                                                                                                                                                                                   premium on top of any carbon price. If supply \< demand (e.g. early green steel scarcity), premium exceeds costs; if oversupply, premium
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          erodes[\[14\]](https://www.crugroup.com/en/communities/thought-leadership/2024/how-will-the-green-steel-premia-be-determined/#:~:text=Our%20research%20has%20shown%20that,set%20by%20the%20market%20pull). Conceptual model
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          rather than a closed-form formula.

  **Agora Industry "Steel Transformation Cost Calculator" (2022)**[\[15\]](https://www.agora-industry.org/data-tools/steel-transformation-cost-calculator#:~:text=This%20online%20tool%20allows%20one,the%20conventional%20blast%20furnace%20route)                                                                                                                                                                                                           **Cost-based model.** Computes incremental capital/O&M for H₂-DRI or NG-DRI vs BF-BOF. Outputs CO₂ abatement cost (\$/tCO₂) and per-ton steel cost. The model inputs hydrogen price, energy, etc.                                        Not sector-specific. Focuses on plant-level economics, not customer segments. Assumes decarbonizing steel will serve general demand.                                                                                               **Incremental cost approach.** Calculates *levelized cost of steel* for each technology, giving a "premium" as the difference vs baseline steel. This can inform carbon contracts (CfDs). Essentially "cost-plus": premium
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          covers extra capex/O&M of green tech[\[15\]](https://www.agora-industry.org/data-tools/steel-transformation-cost-calculator#:~:text=This%20online%20tool%20allows%20one,the%20conventional%20blast%20furnace%20route). No
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          explicit markup by customer.

  **India Green Steel Coalition / EY Demand Model (2025)**[\[8\]](https://www.indiagreensteelcoalition.org/reports-articles/unlocking-green-steel-demand-in-india/#:~:text=Currently%2C%20the%20premium%20on%20green,of%20green%20hydrogen%20and%20the)                                                                                                                                                                                                       Uses **static scenario analysis**. Assumes a baseline green-steel cost premium (currently \~\$210/t for GH₂-DRI steel) and simulates decline as hydrogen cost falls. Implicitly includes abatement (high H₂ cost→high premium). Does not Applies **sector multipliers indirectly**. Reports premium impact on three end-use sectors (auto, construction, infra), reflecting that automotive/infrastructure can absorb \~5% cost hikes vs 3.7% in                            **Fixed plus decline**: starts at a given premium (\$210/t) then falls to \~\$7/t by 2030 as tech
                                                                                                                                                                                                                                                                                                                                                                                                                                                              separately model carbon tax.                                                                                                                                                                                                             construction[\[8\]](https://www.indiagreensteelcoalition.org/reports-articles/unlocking-green-steel-demand-in-india/#:~:text=Currently%2C%20the%20premium%20on%20green,of%20green%20hydrogen%20and%20the). Assumes uniform \$/t    scales[\[16\]](https://www.indiagreensteelcoalition.org/reports-articles/unlocking-green-steel-demand-in-india/#:~:text=early%20adoption%20phase%2C%20largely%20driven,2040). Pricing logic is scenario-driven (tech cost
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       premium but different % impacts.                                                                                                                                                                                                   curves + assumed demand elasticity). Does not derive premium from marginal costs, but posits a future price path based on interviews.

  **H₂ Green Steel (Industry, Sweden)**[\[7\]](https://www.mckinsey.com/capabilities/sustainability/our-insights/henrik-henriksson-rapidly-scaling-a-green-steel-start-up#:~:text=McKinsey%3A%20Green%20steel%20is%20going,pay%20more%20for%20your%20product)                                                                                                                                                                                                 Implicitly, green steel capex paid upfront (renewable H₂ production → green iron). Emphasizes that rising carbon prices justify higher green prices.                                                                                     **Selective, value-based**: targets customers with binding science-based targets (e.g. BMW,                                                                                                                                        **Value-based premium (\~25%)**: CEO states green steel will sell "around 25% above" brown steel, moving from commodity to value
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Mercedes)[\[7\]](https://www.mckinsey.com/capabilities/sustainability/our-insights/henrik-henriksson-rapidly-scaling-a-green-steel-start-up#:~:text=McKinsey%3A%20Green%20steel%20is%20going,pay%20more%20for%20your%20product).   pricing[\[7\]](https://www.mckinsey.com/capabilities/sustainability/our-insights/henrik-henriksson-rapidly-scaling-a-green-steel-start-up#:~:text=McKinsey%3A%20Green%20steel%20is%20going,pay%20more%20for%20your%20product).
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Focuses on OEMs willing to prepay for green credits. Company avoids mass market.                                                                                                                                                   This premium is set by customer willingness, carbon expectations, and supply scarcity. It is not formulaic but based on negotiations (pre-sold contracts used as financing collateral).

  **BCG Consumer WTP Survey (2023)**[\[10\]](https://www.bcg.com/publications/2023/consumers-are-willing-to-pay-for-net-zero-production#:~:text=case,would%20set%20a%20low%20initial)                                                                                                                                                                                                                                                                         Carbon abatement is not explicitly modeled; instead focuses on end-product decarbonization cost. Uses consumer willingness as proxy for premium potential.                                                                               **Customer segmentation by value/affinity.** Identifies high-value, sustainability-driven consumer segments in autos/appliances. Recommends either "skimming" (high price to niche) or "penetration" (modest premium to broad)     **Pricing strategy** rather than formula. Recommends a **skimming approach**: charge a high green premium to a smaller segment of eco-conscious
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       strategies[\[10\]](https://www.bcg.com/publications/2023/consumers-are-willing-to-pay-for-net-zero-production#:~:text=case,would%20set%20a%20low%20initial).                                                                       buyers[\[10\]](https://www.bcg.com/publications/2023/consumers-are-willing-to-pay-for-net-zero-production#:~:text=case,would%20set%20a%20low%20initial). Premium size based on survey demand elasticity -- e.g. many will pay
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          small premium, few pay very high.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Each approach treats **abatement and costs** differently: cost-based
models (Agora) derive premiums strictly from engineering costs, while
market models (CRU, H₂GS) allow premiums above costs when buyers value
sustainability. Segmentation is often addressed qualitatively: CRU and
BCG explicitly segment by end-use, whereas the IGSC/EY model embeds
segmentation via sectoral cost
impacts[\[8\]](https://www.indiagreensteelcoalition.org/reports-articles/unlocking-green-steel-demand-in-india/#:~:text=Currently%2C%20the%20premium%20on%20green,of%20green%20hydrogen%20and%20the).

The **updated calculator** should draw from these lessons: it uses
actual abatement cost inputs (like Agora), applies customer-specific
multipliers (in line with CRU/BCG emphasis on segmentation), and
amortizes costs over time (ensuring realistic project finance). In
contrast to a simple cost adder, these approaches highlight that early
green steel may command a substantial premium (tens of dollars per
tonne) which should be justified by both higher production costs and the
willingness of certain buyers to pay for
decarbonization[\[7\]](https://www.mckinsey.com/capabilities/sustainability/our-insights/henrik-henriksson-rapidly-scaling-a-green-steel-start-up#:~:text=McKinsey%3A%20Green%20steel%20is%20going,pay%20more%20for%20your%20product)[\[13\]](https://www.crugroup.com/en/communities/thought-leadership/2024/how-will-the-green-steel-premia-be-determined/#:~:text=A%20green%20premium%20is%20ultimately,and%20future%20carbon%20costs%20or).

**Table 1.** Summary of green-steel pricing approaches (sources in
text).

[\[1\]](https://www.ceew.in/publications/how-can-india-decarbonise-for-net-zero-steel-industry#:~:text=,depending%20on%20the%20production%20route)
[\[5\]](https://www.ceew.in/publications/how-can-india-decarbonise-for-net-zero-steel-industry#:~:text=the%20same%20year%2C%20equating%20to,alternative%20fuels%20and%20carbon%20management)
How can India Decarbonise for Low Carbon Steel Sustainability?

<https://www.ceew.in/publications/how-can-india-decarbonise-for-net-zero-steel-industry>

[\[2\]](https://ieefa.org/articles/india-needs-targeted-public-finance-scale-green-steel#:~:text=International%20evidence%20shows%20public%20costs,alone%20cannot%20drive%20the%20transition)
[\[6\]](https://ieefa.org/articles/india-needs-targeted-public-finance-scale-green-steel#:~:text=Global%20project%20failures%20reveal%20a,production%20to%20final%20steel%20output)
India needs targeted public finance to scale green steel \| IEEFA

<https://ieefa.org/articles/india-needs-targeted-public-finance-scale-green-steel>

[\[3\]](https://www.rystadenergy.com/news/india-steel-europe-carbon-rules#:~:text=Currently%2C%20these%20companies%20are%20on,and%20India%27s%20high%20carbon%20intensity)
India steel sector competitiveness under threat as Europe tightens
carbon rules

<https://www.rystadenergy.com/news/india-steel-europe-carbon-rules>

[\[4\]](https://www.metalbook.com/blogs/cbam-and-the-future-of-indias-steel-exports/#:~:text=To%20understand%20CBAM%E2%80%99s%20commercial%20impact%2C,could%20be%20greater%20than%20%E2%82%AC220%2Ftonne)
CBAM and the Future of India's Steel Exports

<https://www.metalbook.com/blogs/cbam-and-the-future-of-indias-steel-exports/>

[\[7\]](https://www.mckinsey.com/capabilities/sustainability/our-insights/henrik-henriksson-rapidly-scaling-a-green-steel-start-up#:~:text=McKinsey%3A%20Green%20steel%20is%20going,pay%20more%20for%20your%20product)
Henrik Henriksson: Scaling a green steel start-up \| McKinsey

<https://www.mckinsey.com/capabilities/sustainability/our-insights/henrik-henriksson-rapidly-scaling-a-green-steel-start-up>

[\[8\]](https://www.indiagreensteelcoalition.org/reports-articles/unlocking-green-steel-demand-in-india/#:~:text=Currently%2C%20the%20premium%20on%20green,of%20green%20hydrogen%20and%20the)
[\[16\]](https://www.indiagreensteelcoalition.org/reports-articles/unlocking-green-steel-demand-in-india/#:~:text=early%20adoption%20phase%2C%20largely%20driven,2040)
Unlocking Green Steel Demand In India - India Green Steel Coalition

<https://www.indiagreensteelcoalition.org/reports-articles/unlocking-green-steel-demand-in-india/>

[\[9\]](https://www.crugroup.com/en/communities/thought-leadership/2024/how-will-the-green-steel-premia-be-determined/#:~:text=The%20willingness%20of%20consumers%20to,and%20commanding%20different%20green%20premium)
[\[11\]](https://www.crugroup.com/en/communities/thought-leadership/2024/how-will-the-green-steel-premia-be-determined/#:~:text=A%20green%20premium%20is%20ultimately,any%20carbon%20taxes%2Femissions%20trading%20schemes)
[\[12\]](https://www.crugroup.com/en/communities/thought-leadership/2024/how-will-the-green-steel-premia-be-determined/#:~:text=conducted%20with%20potential%20buyers%20of,any%20carbon%20taxes%2Femissions%20trading%20schemes)
[\[13\]](https://www.crugroup.com/en/communities/thought-leadership/2024/how-will-the-green-steel-premia-be-determined/#:~:text=A%20green%20premium%20is%20ultimately,and%20future%20carbon%20costs%20or)
[\[14\]](https://www.crugroup.com/en/communities/thought-leadership/2024/how-will-the-green-steel-premia-be-determined/#:~:text=Our%20research%20has%20shown%20that,set%20by%20the%20market%20pull)
How will the green steel premia be determined? - CRU Group

<https://www.crugroup.com/en/communities/thought-leadership/2024/how-will-the-green-steel-premia-be-determined/>

[\[10\]](https://www.bcg.com/publications/2023/consumers-are-willing-to-pay-for-net-zero-production#:~:text=case,would%20set%20a%20low%20initial)
Consumers Willing to Pay for Net Zero Production \| BCG

<https://www.bcg.com/publications/2023/consumers-are-willing-to-pay-for-net-zero-production>

[\[15\]](https://www.agora-industry.org/data-tools/steel-transformation-cost-calculator#:~:text=This%20online%20tool%20allows%20one,the%20conventional%20blast%20furnace%20route)
Steel Transformation Cost Calculator

<https://www.agora-industry.org/data-tools/steel-transformation-cost-calculator>
