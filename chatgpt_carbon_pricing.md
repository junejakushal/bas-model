# Carbon Pricing in the Steel Sector

This report examines how steel producers face carbon pricing in three
regions -- Europe, East Asia (South Korea and Japan), and emerging
markets (India and China) -- focusing on production‐level emissions
(Scope 1 and 2), pricing models (ETS, carbon taxes, CBAM, etc.),
industry‐specific incentives, use of credits/allowances, regional carbon
prices (in local/US\$), and any lifecycle‐amortization mechanisms. We
then propose an algorithm to calculate a **green premium** for
low‐emission steel that uses these factors, amortizes costs over a
project's life (10--20 years), and yields a premium per tonne, per
tonne‐CO₂ saved, and total lifecycle premium.

## Europe

Europe's steel industry operates under the EU Emissions Trading System
(EU ETS), which charges for **Scope 1** (on‐site fuel/coal) and
indirectly for **Scope 2** (purchased electricity) emissions. EU ETS
allowance prices have climbed sharply: from about **€30/tCO₂** in early
2021 to above **€80/tCO₂ by
2024**[\[1\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=the%20EU%20ETS%2C%20carbon%20allowance,free%20allocation%20phases%20out%20completely),
and currently average roughly **€64--65/tCO₂** (about **\$70/tCO₂**) in
2024[\[2\]](https://icapcarbonaction.com/en/ets/eu-emissions-trading-system-eu-ets#:~:text=Current%20Allowance%20Price%20).
(For example, a German blast‐furnace steel plant emitting \~2.1 tCO₂ per
tonne of steel would incur carbon costs of **€130--€170 per tonne** of
steel at €65/tCO₂.) The EU still gives trade‐exposed steel producers
free allowances, but these are being phased down; by 2027 free
allocations will largely
end[\[1\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=the%20EU%20ETS%2C%20carbon%20allowance,free%20allocation%20phases%20out%20completely).
**Carbon Border Adjustment Mechanism (CBAM):** Beginning 2023--2026
(transitional), and fully from 2026, imports of steel (and other
carbon‐intensive goods) face the EU's CBAM. Importers must surrender
**CBAM certificates** equal to embedded CO₂, priced at the EU ETS
allowance
rate[\[3\]](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en#:~:text=certificates%20from%20the%20national%20authorities,weekly%20average%20from%202027%20onwards).
(Certificates are deducted by any carbon price already paid abroad.) In
effect, exporters to the EU must pay roughly the same carbon price as EU
producers.

-   **Industry‐specific measures:** Europe has begun pushing demand for
    "green steel". For example, German states have proposed rules to
    **incentivize automakers to buy certified low‐CO₂ steel** for
    cars[\[4\]](https://gmk.center/en/news/germany-calls-on-the-eu-to-promote-the-use-of-green-steel-in-the-automotive-industry/#:~:text=The%20proposal%20provides%20for%20the,of%20the%20EU%E2%80%99s%20climate%20goals).
    Germany has also promoted *Carbon Contracts for Difference* (CCfDs)
    to underwrite industrial decarbonization: under CCfDs, the
    government guarantees a floor carbon price for clean steel projects,
    offsetting their higher costs. Meanwhile, a recent study proposes a
    **Value‐Chain Transition Fund**: a small premium on end‐products
    (e.g. electric vehicles, high‐speed trains) would fund steel
    decarbonization and be recouped in 2--8 years for steel
    projects[\[5\]](https://www.sciencedirect.com/science/article/pii/S0301421524004336#:~:text=along%20CO_%7B2%7D,examples%20of%20representative%20end%20products).
    Such mechanisms effectively **amortize** the upfront cost of
    low‐carbon steel over its lifecycle.

-   **Carbon credits/allowances:** Under EU ETS, steelmakers use EU
    allowances. International credits (CERs) are largely phased out.
    Allowances are 100% freely allocated to eligible steel facilities
    (subject to benchmarks and free‐allocation rules). EU ETS revenues
    fund R&D and support (Innovation/Modernisation Funds), but there is
    no formal "amortization" scheme -- instead, governments may use
    revenue to subsidize industry decarbonization.

-   **Carbon price:** As of 2024, EU ETS permits trade around **€65/tCO₂
    (≈\$70/tCO₂)**[\[2\]](https://icapcarbonaction.com/en/ets/eu-emissions-trading-system-eu-ets#:~:text=Current%20Allowance%20Price%20).
    Future trajectories are much higher (analysts project €100--120 by
    2027[\[1\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=the%20EU%20ETS%2C%20carbon%20allowance,free%20allocation%20phases%20out%20completely)).
    The EU CBAM will effectively impose this price on imports. In sum,
    the **effective carbon price** faced by EU steel (direct + indirect)
    is on the order of tens of €/tCO₂ (hundreds of
    \$/t‐steel)[\[1\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=the%20EU%20ETS%2C%20carbon%20allowance,free%20allocation%20phases%20out%20completely)[\[3\]](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en#:~:text=certificates%20from%20the%20national%20authorities,weekly%20average%20from%202027%20onwards).

-   **Lifecycle amortization:** Beyond CCfDs, one proposal suggests
    recouping steel decarbonization costs by adding a small "carbon
    premium" into product prices across industries. For example, a study
    finds that surcharges raising EV prices by \~0.2--1.1% or train
    production costs by \~0.3--0.6% could finance steel and cement
    capture technologies, with payback in \~3--8
    years[\[5\]](https://www.sciencedirect.com/science/article/pii/S0301421524004336#:~:text=along%20CO_%7B2%7D,examples%20of%20representative%20end%20products).
    (This aligns with EU discussions on spreading transition costs over
    supply chains.)

## South Korea and Japan

**South Korea:** South Korea's ETS (K-ETS) has covered major steel
producers since 2015. It mandates emission cuts for large emitters
(alloys, power, cement, etc.) and covers Scope 1 and indirect Scope 2.
In Phase 3 (2021--2025), \~730 entities (including POSCO, Hyundai Steel)
participate, covering \>70% of national
emissions[\[6\]](http://www.reccessary.com/en/news/asia-carbon-pricing-shift-japan-korea-indonesia-ets-reform#:~:text=South%20Korea%E2%80%99s%20ETS%20has%20been,makers%2C%20and%2021%20financial%20institutions).
Each tonne of CO₂ must be covered by one allowance (Korean Allowance
Unit, KAU).

-   **Current carbon price:** Korea's carbon market has been volatile.
    Prices have swung from over **KRW 40,000/tCO₂ (\~\$28)** down to
    under **KRW 10,000 (\~\$7)** in
    2023[\[7\]](http://www.reccessary.com/en/news/asia-carbon-pricing-shift-japan-korea-indonesia-ets-reform#:~:text=demand%20imbalances,08%29%2C%20a%20fourfold%20gap).
    By October 2025, KAU spot traded near KRW 10,250
    (≈\$7)[\[8\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=If%20the%20current%20price%20of,a%20year%20in%20extra%20costs).
    Government forecasts expect prices to rise: projections say
    **KRW 40,000--61,000** per tCO₂ by 2030
    (≈\$29--\$44)[\[9\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=The%20Ministry%20of%20Environment%20of,won%20per%20ton%20by%202030).

-   **Allowances and credits:** South Korea still allocates large free
    quotas to EITE sectors (including steel). Under Phase 4
    (2026--2030), free allowances to steel will shrink (e.g. free quota
    cut from 114 to
    \~89 MtCO₂)[\[10\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=Under%20the%20fourth%20plan%2C%20the,to%20about%2089%20million%20tons),
    forcing integrated mills to buy the rest on the market. The K-ETS
    allows limited offsets: domestic **Korean Offset Credits (KOC)** and
    some CDM credits, up to \~5--10% of
    obligations[\[11\]](https://icapcarbonaction.com/en/ets/korea-emissions-trading-system-k-ets#:~:text=Qualitative%20limit%3A%20The%20use%20only,April%202010)[\[12\]](https://icapcarbonaction.com/en/ets/korea-emissions-trading-system-k-ets#:~:text=Quantitative%20limit%3A%C2%A0Up%20to%205,compliance%20obligation%2C%20regardless%20of%20type).
    (In Phases 1--2 they could use up to 10% offsets; in Phase 3 only
    5%.) Offset usage so far has been modest.

-   **Industry impacts/incentives:** The steel industry warns that
    rising carbon costs (combined with US/EU tariffs and cheap imports)
    threaten profits. For example, POSCO and Hyundai Steel together
    expect \~KRW 3 trillion (\$2.1B) in extra ETS costs over
    2026--2030[\[13\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=The%20two%20largest%20steelmakers%20alone,over%20the%20next%20five%20years).
    At **KRW 30,000/tCO₂** (\~\$21), their cumulative shortfall is
    \~20 MtCO₂, roughly 600 billion
    KRW/year[\[8\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=If%20the%20current%20price%20of,a%20year%20in%20extra%20costs).
    Industry groups urge relief: proposals include recycling ETS
    revenues into decarbonization aid (e.g. Germany‐style
    CCfDs)[\[14\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=Steelmakers%20say%20they%20support%20the,any%20shock%20to%20industrial%20earnings).
    No dedicated "amortization fund" exists yet, but the government is
    reforming K-ETS (Phase 4) to improve liquidity and may consider
    support measures as costs rise. There are few targeted incentives
    (most government focus is R&D in hydrogen steel), though power
    sector free allocations will be reduced (50% auction by 2030), which
    may indirectly raise steel power prices.

**Japan:** Japan currently has **no economy‐wide carbon price for
steel**, but policy is evolving. Japan maintains a small national carbon
tax (introduced 2012) of **¥289/tCO₂
(\~\$2)**[\[15\]](https://www.carbon-direct.com/insights/inside-japan-s-gx-ets-carbon-market-and-its-global-climate-impact#:~:text=Japan%20maintains%20a%20small%20carbon,fossil%20fuel%20consumption%20and%20complementing)
-- effectively negligible for steel. However, under the *Green
Transformation (GX) Initiative*, Japan launched a voluntary corporate
ETS (GX-ETS) in 2023, to become mandatory by
2026[\[16\]](http://www.reccessary.com/en/news/asia-carbon-pricing-shift-japan-korea-indonesia-ets-reform#:~:text=Japan%20to%20enforce%20mandatory%20ETS,in%202026).
Initially, \~300--400 large firms (emitting \>100kt CO₂) will set
targets and trade allowances (mostly
free‐allocated)[\[17\]](http://www.reccessary.com/en/news/asia-carbon-pricing-shift-japan-korea-indonesia-ets-reform#:~:text=Under%20the%20current%20plan%2C%20companies,firms%20short%20on%20allowances%20can).
Allowances will have government‐set floors and ceilings; companies may
also use **J-Credits** (existing voluntary credits) to meet
obligations[\[15\]](https://www.carbon-direct.com/insights/inside-japan-s-gx-ets-carbon-market-and-its-global-climate-impact#:~:text=Japan%20maintains%20a%20small%20carbon,fossil%20fuel%20consumption%20and%20complementing).
The GX-ETS rules (once finalized) may extend to heavy industry,
including steel.

-   **Scope 1/2 and pricing:** Today Japanese steelmakers pay the €2
    equivalent tax on fuel (scope 1) and no price on electricity
    (scope 2 aside from power prices). The new GX-ETS and a planned
    fossil fuel levy (2028) will add explicit carbon costs. Absent
    these, Japan's steel sector currently faces an **effective carbon
    price near zero** domestically, though government plans strongly
    encourage zero‐emission steel.

-   **Credits/allowances:** Japan's emerging carbon market includes
    **J-Credits**, a voluntary registry of emissions reductions. As of
    early 2024, a new Tokyo Carbon Credit Market platform trades
    J-Credits and voluntary
    credits[\[18\]](https://www.carbon-direct.com/insights/inside-japan-s-gx-ets-carbon-market-and-its-global-climate-impact#:~:text=In%20October%202023%2C%20the%20Tokyo,voluntary%20credits%20through%20an%20online).
    In the near future, GX-ETS companies can use credits (likely limited
    % of their cap) to comply.

-   **Industry incentives:** Japan is actively supporting green steel
    demand. The government's **"Green Steel for GX"** strategy defines
    low-carbon steel and offers procurement and subsidies. Notably, the
    Green Purchasing Act was amended (2025) to prioritize such steel,
    and the *Clean Energy Vehicle subsidy* was increased by up to
    **¥50,000 (≈\$350)** per vehicle if it uses steel from innovative
    electric‐arc
    furnaces[\[19\]](https://www.renewable-ei.org/en/activities/column/REupdate/20251023.php#:~:text=Prior%20to%20this%20summary%2C%20the,side%20support%20measures).
    In short, automakers get higher EV subsidies when buying "green"
    steel. Steel producers also have brands (NS Carbolex®, JFE
    JGreeneX®, etc.) under a JISF mass‐balance certification, with
    government support. These policies spread the cost of steel
    decarbonization onto auto and other demand sectors (an amortization
    in industry), rather than burden steel costs fully at once.

-   **Carbon price:** Summarizing, Japan's current carbon price is
    **very low** (¥289/t ≈
    \$2[\[15\]](https://www.carbon-direct.com/insights/inside-japan-s-gx-ets-carbon-market-and-its-global-climate-impact#:~:text=Japan%20maintains%20a%20small%20carbon,fossil%20fuel%20consumption%20and%20complementing)).
    The forthcoming GX-ETS is expected to introduce a price signal (with
    floors/ceilings set by government), but initial prices will likely
    remain modest compared to EU or Korea.

## Emerging Economies (India and China)

**India:** India has no operational carbon tax or ETS for steel. A
legacy *coal cess* (a coal usage tax) once added \~₹400/ton of coal
(\~\$5.7/tCO₂)[\[20\]](https://www.reuters.com/sustainability/boards-policy-regulation/indian-coal-prices-be-lower-after-tax-revision-industry-officials-say-2025-09-04/#:~:text=India%27s%20finance%20minister%20hiked%20consumption,ton%2C%20known%20as%20a%20cess),
but this flat "carbon levy" was abolished in
2025[\[20\]](https://www.reuters.com/sustainability/boards-policy-regulation/indian-coal-prices-be-lower-after-tax-revision-industry-officials-say-2025-09-04/#:~:text=India%27s%20finance%20minister%20hiked%20consumption,ton%2C%20known%20as%20a%20cess).
As of late 2025, **no national carbon price** applies to steel. The
government is developing a **Carbon Credit Trading Scheme (CCTS)**
(adopted July 2024) -- an intensity‐based ETS covering 9 industrial
sectors (likely including
steel)[\[21\]](https://www.pib.gov.in/PressNoteDetails.aspx?id=154721&NoteId=154721&ModuleId=3®=3&lang=2#:~:text=,outperform%20benchmark%20emissions%20intensity%20levels)
-- but it is still in regulatory design and initial rollout. Until then,
Indian steelmakers (which produce \~3.6 tCO₂/ton crude via BF-BOF) face
essentially **zero domestic carbon
cost**[\[22\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=Electric%20arc%20furnace%20,similarly%20operates%20without%20carbon%20constraints).

-   **Export pressures:** However, EU CBAM (effective 2026) will levy a
    carbon tax on Indian steel exports to
    Europe[\[23\]](https://www.reuters.com/sustainability/boards-policy-regulation/indias-steel-exports-europe-set-drop-eu-carbon-tax-looms-2025-12-05/#:~:text=Imports%20of%20steel%20into%20the,electricity%2C%20fertilisers%20and%20other%20products).
    This external "carbon border tax" effectively forces Indian mills to
    decarbonize if they want EU markets. (Industry is uncertain how CBAM
    rates will be
    calculated[\[24\]](https://www.reuters.com/sustainability/boards-policy-regulation/indias-steel-exports-europe-set-drop-eu-carbon-tax-looms-2025-12-05/#:~:text=%22About%2060,said%20one%20of%20the%20executives),
    but all blast‐furnace steel -- \~60% of Indian exports -- will incur
    significant CBAM charges.) For example, analysts expect EU CBAM to
    raise India's steel export costs substantially, prompting some mills
    to seek new
    markets[\[25\]](https://www.reuters.com/sustainability/boards-policy-regulation/indias-steel-exports-europe-set-drop-eu-carbon-tax-looms-2025-12-05/#:~:text=NEW%20DELHI%2C%20Dec%205%20,industry%20executives%20and%20analysts%20said)[\[26\]](https://www.reuters.com/sustainability/boards-policy-regulation/indias-steel-exports-europe-set-drop-eu-carbon-tax-looms-2025-12-05/#:~:text=Additional%20planned%20capacity%20could%20add,based%20research%20group).

-   **Pricing models:** Absent domestic ETS, India has relied on
    performance standards (the existing PAT scheme) and will use CCTS
    intensity targets. The Press Information Bureau notes India is
    "moving towards" a rate‐based ETS (CCTS) covering heavy
    industries[\[21\]](https://www.pib.gov.in/PressNoteDetails.aspx?id=154721&NoteId=154721&ModuleId=3®=3&lang=2#:~:text=,outperform%20benchmark%20emissions%20intensity%20levels),
    and has approved voluntary carbon credit methodologies (renewables,
    efficiency,
    etc.)[\[27\]](https://www.pib.gov.in/PressNoteDetails.aspx?id=154721&NoteId=154721&ModuleId=3®=3&lang=2#:~:text=On%20March%2028%2C%202025%2C%20India%E2%80%99s,generating%20voluntary%20carbon%20credits%20including).
    The CCTS will issue credits for beating intensity benchmarks, and
    firms can use credits to comply, but it is not yet a strict cap.

-   **Use of credits/allowances:** India is establishing a voluntary
    carbon market (domestic credits, \~8 methodologies
    approved)[\[27\]](https://www.pib.gov.in/PressNoteDetails.aspx?id=154721&NoteId=154721&ModuleId=3®=3&lang=2#:~:text=On%20March%2028%2C%202025%2C%20India%E2%80%99s,generating%20voluntary%20carbon%20credits%20including).
    When CCTS becomes operational, facilities outperforming their
    targets will earn certificates. These credits may be sold or used
    against future obligations. There is no international linkage.

-   **Price per tCO₂:** Since India has no effective carbon pricing on
    steel, the **implied carbon price is essentially zero
    domestically**[\[28\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=electricity%20sources%20and%20scrap%20processing,similarly%20operates%20without%20carbon%20constraints).
    (By contrast, the coal cess before abolition was about
    \$5--6/tCO₂[\[20\]](https://www.reuters.com/sustainability/boards-policy-regulation/indian-coal-prices-be-lower-after-tax-revision-industry-officials-say-2025-09-04/#:~:text=India%27s%20finance%20minister%20hiked%20consumption,ton%2C%20known%20as%20a%20cess).)
    CCTS may yield an implicit price signal in future, but nothing
    concrete today.

**China:** China's national ETS (launched 2021) currently covers power
generation and, since 2024, has been phasing in industry. As of 2025,
around 3,500 installations are in the system (power, cement, steel,
aluminum)[\[29\]](https://icapcarbonaction.com/en/ets/china-national-ets#:~:text=The%20China%20national%20ETS%20regulates,to%20other%20sectors%20over%20time).
All allowances are initially **freely allocated** (output‐based
benchmarks); Chinese companies surrender allowances to cover annual
scope 1 emissions. China's ETS price has historically been **low**:
secondary market trading averaged about **CNY 96/tCO₂ (\~USD 13/t)** as
of
mid-2024[\[30\]](https://icapcarbonaction.com/en/ets/china-national-ets#:~:text=Current%20Allowance%20Price%20),
roughly one‐seventh of EU levels.

-   **Sector coverage:** Although the ETS framework now includes steel
    and cement, Phase 1 (2024--26) is largely a "familiarization" period
    where covered firms monitor and report emissions without strict
    caps[\[31\]](https://icapcarbonaction.com/en/ets/china-national-ets#:~:text=In%C2%A0March%202025%2C%20the%20MEE%C2%A0published%20a,2%7De).
    Full compliance (requiring allowance surrender for steel) is planned
    from 2027
    onwards[\[31\]](https://icapcarbonaction.com/en/ets/china-national-ets#:~:text=In%C2%A0March%202025%2C%20the%20MEE%C2%A0published%20a,2%7De).
    Today, Chinese steel producers face **no direct carbon charge**:
    they remain effectively unconstrained, similar to
    India[\[28\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=electricity%20sources%20and%20scrap%20processing,similarly%20operates%20without%20carbon%20constraints)[\[32\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=China%27s%20national%20ETS%2C%20launched%20in,Over%2050%20million%20tonnes%20of).

-   **Carbon price:** The current benchmark is the ETS allowance price.
    As noted, China's national allowance price is around **¥96** (RMB)
    per
    tCO₂[\[30\]](https://icapcarbonaction.com/en/ets/china-national-ets#:~:text=Current%20Allowance%20Price%20)
    (≈**\$13**). Regional pilot markets had traded even lower (often
    \$5--\$10). For context, China's power ETS price (\~¥80--90 by 2023)
    was only
    \~€10/t[\[32\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=China%27s%20national%20ETS%2C%20launched%20in,Over%2050%20million%20tonnes%20of).
    Analysts expect these prices to slowly rise as China tightens caps,
    but no dramatic carbon cost burdens exist yet.

-   **Offsets:** China relaunched its domestic offset program in 2024
    (CCER -- China Certified Emissions
    Reductions)[\[33\]](https://icapcarbonaction.com/en/ets/china-national-ets#:~:text=In%20January%202024%2C%20China%20launched,see%20%E2%80%98Offset%20Credits%E2%80%99%20section).
    This voluntary credit market will eventually allow projects (e.g.
    renewable energy, industry efficiency) to generate tradable credits.
    It is unclear if or how CCER credits will be used in the mandatory
    ETS (likely limited by future rules).

-   **Industry incentives:** China's government is heavily investing in
    green steel (hydrogen DRI, CCUS pilots) even without carbon pricing.
    A January 2025 EU--China agreement calls for "green-steel
    certificates" to boost low-carbon supply chains (pilot scheme led by
    Baowu and EU
    firms)[\[34\]](https://www.climatebonds.net/news-events/press-room/press-releases/targeted-incentives-key-accelerating-chinas-steel-sector-transition#:~:text=Targeted%20Incentives%20Key%20to%20Accelerating,gap%20in%20steel%20transition%20finance).
    However, formal incentives for end‐users (auto, construction) are
    still nascent. Unlike Japan, China has no known car‐sector subsidy
    tied to green steel. Instead, China's strategy is supply‐focused --
    supporting steelmakers and technology.

-   **Price per tCO₂:** In summary, China's **carbon price** (ETS
    allowance price) is roughly **¥80--100/t**
    (≈\$11--\$14)[\[30\]](https://icapcarbonaction.com/en/ets/china-national-ets#:~:text=Current%20Allowance%20Price%20)[\[32\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=China%27s%20national%20ETS%2C%20launched%20in,Over%2050%20million%20tonnes%20of).
    But as steel is just entering compliance, the **effective steel
    carbon cost today is essentially zero**, pending future market
    tightening.

## **Regional Comparison of Carbon Prices**

-   **Europe (EU ETS/CBAM):** \~€60--80 per tCO₂ (\~\$65--\$85) and
    rising[\[2\]](https://icapcarbonaction.com/en/ets/eu-emissions-trading-system-eu-ets#:~:text=Current%20Allowance%20Price%20)[\[1\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=the%20EU%20ETS%2C%20carbon%20allowance,free%20allocation%20phases%20out%20completely).
-   **South Korea (K-ETS):** \~₩10,000 per tCO₂ (≈\$7) in
    2025[\[8\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=If%20the%20current%20price%20of,a%20year%20in%20extra%20costs)[\[7\]](http://www.reccessary.com/en/news/asia-carbon-pricing-shift-japan-korea-indonesia-ets-reform#:~:text=demand%20imbalances,08%29%2C%20a%20fourfold%20gap);
    projected to reach ₩40,000--61,000 (\$29--\$44) by
    2030[\[9\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=The%20Ministry%20of%20Environment%20of,won%20per%20ton%20by%202030).
-   **Japan:** \~¥289 per tCO₂ (≈\$2) via carbon
    tax[\[15\]](https://www.carbon-direct.com/insights/inside-japan-s-gx-ets-carbon-market-and-its-global-climate-impact#:~:text=Japan%20maintains%20a%20small%20carbon,fossil%20fuel%20consumption%20and%20complementing);
    voluntary GX-ETS not yet price‐competitive.
-   **India:** effectively \$0 (no price); a coal cess of \~\$5/t was
    removed[\[20\]](https://www.reuters.com/sustainability/boards-policy-regulation/indian-coal-prices-be-lower-after-tax-revision-industry-officials-say-2025-09-04/#:~:text=India%27s%20finance%20minister%20hiked%20consumption,ton%2C%20known%20as%20a%20cess).
-   **China:** \~¥96 per tCO₂ (\~\$13) in
    2024[\[30\]](https://icapcarbonaction.com/en/ets/china-national-ets#:~:text=Current%20Allowance%20Price%20)
    (power sector ETS); steel soon to be priced.

(Currency conversion: €1≈\$1.1, ₩10,000≈\$7, ¥100≈\$0.68, ₹87≈\$1.)

## **Proposed Algorithm for a Low-Carbon Steel Green Premium**

To price a **green premium** for low‐emission steel (relative to
conventional steel), we incorporate region‐specific carbon costs,
project life, industry factors, and CBAM/credit values. A generalized
algorithm might proceed as follows:

1.  **Inputs:**

2.  **Regional carbon price** $P_{\text{region}}$ (in \$/tCO₂). Use
    local carbon price (ETS or tax) for the region where steel is
    produced or consumed.

3.  **Emissions reduction** $\Delta E$ (tCO₂ saved per tonne of steel) =
    (emissions of conventional steel -- emissions of low‐carbon steel)
    per tonne.

4.  **Project lifetime** $L$ (years) and **annual production** $Y$
    (tonnes/year).

5.  **Industry factor** $f_{\text{ind}}$ (dimensionless) \>1 to reflect
    higher willingness‐to‐pay or regulatory pressure in certain sectors
    (e.g. automotive vs. construction).

6.  **CBAM/exports:** if steel will be sold under EU CBAM, include an
    **EU CBAM price** $P_{\text{CBAM}}$ (≈EU ETS price) to capture
    avoided border tax.

7.  **Carbon credit value** $P_{\text{credit}}$ (\$/tCO₂): potential
    revenue per tCO₂ from selling credits or subsidies (e.g.
    CDM/J-Credit value).

8.  **Compute carbon‐cost basis:**

-   $$\text{Base premium per tCO₂} = \left( P_{\text{region}} + P_{\text{CBAM}} \right) \times f_{\text{ind}}\mspace{6mu} - \mspace{6mu} P_{\text{credit}}.$$
    This is the effective carbon‐price differential per tonne CO₂,
    adjusted for industry weighting and minus any credit revenues.

9.  **Premium per tonne steel:**

-   $$\text{Premium}_{\text{per tonne}} = \Delta E\mspace{6mu} \times \mspace{6mu}\left\lbrack \left( P_{\text{region}} + P_{\text{CBAM}} \right) \times f_{\text{ind}} - P_{\text{credit}} \right\rbrack.$$
    In words, multiply the emissions saved per tonne by the net carbon
    price. This yields an added cost (\$/tonne‐steel) for using
    low‐carbon instead of conventional steel.

10. **Premium per tCO₂:**\
    Optionally report the **premium per tCO₂ saved** as

-   $$\text{Premium}_{\text{per tCO₂}} = \left( P_{\text{region}} + P_{\text{CBAM}} \right) \times f_{\text{ind}}\mspace{6mu} - \mspace{6mu} P_{\text{credit}},$$
    which shows the effective price signal per tonne of CO₂ abated.

11. **Lifecycle (project) premium:**\
    Over a project producing $Y$ tonnes/year for $L$ years, total
    low‐carbon steel output is $Y \times L$. Thus

-   $$\text{Total lifecycle premium} = \text{Premium}_{\text{per tonne}}\mspace{6mu} \times \mspace{6mu} Y\mspace{6mu} \times \mspace{6mu} L.$$
    This is the aggregate additional cost (or price premium) over the
    project's life.

12. **Amortization:**\
    One can convert to an annualized premium by dividing by $L$, or by
    applying a discount rate for NPV calculations. In simple terms, the
    extra cost per tonne per year is

-   $$\text{Annualized premium per tonne} = \frac{\text{Premium}_{\text{per tonne}}}{L}.$$
    This spreads the upfront decarbonization premium evenly over the
    project life (as done in transition‐fund or CCfD
    schemes[\[5\]](https://www.sciencedirect.com/science/article/pii/S0301421524004336#:~:text=along%20CO_%7B2%7D,examples%20of%20representative%20end%20products)[\[14\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=Steelmakers%20say%20they%20support%20the,any%20shock%20to%20industrial%20earnings)).

**Note:** All currency units should be consistent (e.g. convert local
prices to USD). The algorithm allows for different scenarios by
adjusting $P_{\text{region}}$ for each country/market (e.g. €70/t in EU
vs. \$7/t in Korea), setting $f_{\text{ind}}$ (e.g. 1.2 for auto
sector), and including CBAM values (≈EU ETS price) if relevant. For
example, exporting low-carbon steel to Europe could add
$P_{\text{CBAM}} \approx €70$ per tCO₂ avoided (since CBAM avoids paying
EU price on imports).

This structured approach ensures the premium reflects **regional carbon
costs**, **emission savings**, **industry differences**, and **market
mechanisms** (CBAM, credits). The outputs -- premium per tonne, per
tCO₂, and total lifecycle premium -- give clear pricing signals for
manufacturers and buyers. Such a formula can be refined with real data:
e.g. EU: $P_{\text{region}} \sim \$ 70/t$; Korea: $\sim \$ 7/t$ (rising
to \\\$30--\\\$40 by
2030)[\[8\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=If%20the%20current%20price%20of,a%20year%20in%20extra%20costs)[\[9\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=The%20Ministry%20of%20Environment%20of,won%20per%20ton%20by%202030);
Japan: $\sim \$ 2/t$
(today)[\[15\]](https://www.carbon-direct.com/insights/inside-japan-s-gx-ets-carbon-market-and-its-global-climate-impact#:~:text=Japan%20maintains%20a%20small%20carbon,fossil%20fuel%20consumption%20and%20complementing);
India: \~\\\$0 (with CBAM impact if
exporting)[\[20\]](https://www.reuters.com/sustainability/boards-policy-regulation/indian-coal-prices-be-lower-after-tax-revision-industry-officials-say-2025-09-04/#:~:text=India%27s%20finance%20minister%20hiked%20consumption,ton%2C%20known%20as%20a%20cess)[\[23\]](https://www.reuters.com/sustainability/boards-policy-regulation/indias-steel-exports-europe-set-drop-eu-carbon-tax-looms-2025-12-05/#:~:text=Imports%20of%20steel%20into%20the,electricity%2C%20fertilisers%20and%20other%20products);
China:
$\sim \$ 13/t$[\[30\]](https://icapcarbonaction.com/en/ets/china-national-ets#:~:text=Current%20Allowance%20Price%20).
These feed into the algorithm above to yield practical green premiums.

**Sources:** Official and industry analyses provide the above data and
models. For Europe, EU legislative texts and market reports give ETS
prices and CBAM
rules[\[3\]](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en#:~:text=certificates%20from%20the%20national%20authorities,weekly%20average%20from%202027%20onwards)[\[2\]](https://icapcarbonaction.com/en/ets/eu-emissions-trading-system-eu-ets#:~:text=Current%20Allowance%20Price%20)[\[1\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=the%20EU%20ETS%2C%20carbon%20allowance,free%20allocation%20phases%20out%20completely).
South Korea and Japan information comes from government and market
updates (e.g. Korean ETS auction plans, Japan GX
reports)[\[8\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=If%20the%20current%20price%20of,a%20year%20in%20extra%20costs)[\[7\]](http://www.reccessary.com/en/news/asia-carbon-pricing-shift-japan-korea-indonesia-ets-reform#:~:text=demand%20imbalances,08%29%2C%20a%20fourfold%20gap)[\[15\]](https://www.carbon-direct.com/insights/inside-japan-s-gx-ets-carbon-market-and-its-global-climate-impact#:~:text=Japan%20maintains%20a%20small%20carbon,fossil%20fuel%20consumption%20and%20complementing)[\[19\]](https://www.renewable-ei.org/en/activities/column/REupdate/20251023.php#:~:text=Prior%20to%20this%20summary%2C%20the,side%20support%20measures).
India's carbon pricing is described by government releases and news
reports[\[35\]](https://www.pib.gov.in/PressNoteDetails.aspx?id=154721&NoteId=154721&ModuleId=3®=3&lang=2#:~:text=,outperform%20benchmark%20emissions%20intensity%20levels)[\[20\]](https://www.reuters.com/sustainability/boards-policy-regulation/indian-coal-prices-be-lower-after-tax-revision-industry-officials-say-2025-09-04/#:~:text=India%27s%20finance%20minister%20hiked%20consumption,ton%2C%20known%20as%20a%20cess).
China's ETS data are from ICAP and climate
news[\[30\]](https://icapcarbonaction.com/en/ets/china-national-ets#:~:text=Current%20Allowance%20Price%20)[\[32\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=China%27s%20national%20ETS%2C%20launched%20in,Over%2050%20million%20tonnes%20of).
Proposed financial frameworks (CCfDs, transition funds) are documented
in academic and industry
sources[\[5\]](https://www.sciencedirect.com/science/article/pii/S0301421524004336#:~:text=along%20CO_%7B2%7D,examples%20of%20representative%20end%20products)[\[14\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=Steelmakers%20say%20they%20support%20the,any%20shock%20to%20industrial%20earnings).
These ensure our analysis and the green premium algorithm are based on
the latest policy contexts and price levels.

[\[1\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=the%20EU%20ETS%2C%20carbon%20allowance,free%20allocation%20phases%20out%20completely)
[\[22\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=Electric%20arc%20furnace%20,similarly%20operates%20without%20carbon%20constraints)
[\[28\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=electricity%20sources%20and%20scrap%20processing,similarly%20operates%20without%20carbon%20constraints)
[\[32\]](https://www.steelonthenet.com/insights/steel-carbon-divide.html#:~:text=China%27s%20national%20ETS%2C%20launched%20in,Over%2050%20million%20tonnes%20of)
Two Worlds \| Carbon Pricing Splits the Steel Industry

<https://www.steelonthenet.com/insights/steel-carbon-divide.html>

[\[2\]](https://icapcarbonaction.com/en/ets/eu-emissions-trading-system-eu-ets#:~:text=Current%20Allowance%20Price%20)
EU Emissions Trading System (EU ETS) \| International Carbon Action
Partnership

<https://icapcarbonaction.com/en/ets/eu-emissions-trading-system-eu-ets>

[\[3\]](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en#:~:text=certificates%20from%20the%20national%20authorities,weekly%20average%20from%202027%20onwards)
Carbon Border Adjustment Mechanism - Taxation and Customs Union

<https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en>

[\[4\]](https://gmk.center/en/news/germany-calls-on-the-eu-to-promote-the-use-of-green-steel-in-the-automotive-industry/#:~:text=The%20proposal%20provides%20for%20the,of%20the%20EU%E2%80%99s%20climate%20goals)
Germany calls on the EU to promote the use of green steel in the
automotive industry

<https://gmk.center/en/news/germany-calls-on-the-eu-to-promote-the-use-of-green-steel-in-the-automotive-industry/>

[\[5\]](https://www.sciencedirect.com/science/article/pii/S0301421524004336#:~:text=along%20CO_%7B2%7D,examples%20of%20representative%20end%20products)
Financing high-cost measures for deep emission cuts in the basic
materials industry -- Proposal for a value chain transition fund -
ScienceDirect

<https://www.sciencedirect.com/science/article/pii/S0301421524004336>

[\[6\]](http://www.reccessary.com/en/news/asia-carbon-pricing-shift-japan-korea-indonesia-ets-reform#:~:text=South%20Korea%E2%80%99s%20ETS%20has%20been,makers%2C%20and%2021%20financial%20institutions)
[\[7\]](http://www.reccessary.com/en/news/asia-carbon-pricing-shift-japan-korea-indonesia-ets-reform#:~:text=demand%20imbalances,08%29%2C%20a%20fourfold%20gap)
[\[16\]](http://www.reccessary.com/en/news/asia-carbon-pricing-shift-japan-korea-indonesia-ets-reform#:~:text=Japan%20to%20enforce%20mandatory%20ETS,in%202026)
[\[17\]](http://www.reccessary.com/en/news/asia-carbon-pricing-shift-japan-korea-indonesia-ets-reform#:~:text=Under%20the%20current%20plan%2C%20companies,firms%20short%20on%20allowances%20can)
Asia's carbon pricing shift: How Japan, Korea, Indonesia step up ETS
reforms \| NEWS \| Reccessary

<http://www.reccessary.com/en/news/asia-carbon-pricing-shift-japan-korea-indonesia-ets-reform>

[\[8\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=If%20the%20current%20price%20of,a%20year%20in%20extra%20costs)
[\[9\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=The%20Ministry%20of%20Environment%20of,won%20per%20ton%20by%202030)
[\[10\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=Under%20the%20fourth%20plan%2C%20the,to%20about%2089%20million%20tons)
[\[13\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=The%20two%20largest%20steelmakers%20alone,over%20the%20next%20five%20years)
[\[14\]](https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233#:~:text=Steelmakers%20say%20they%20support%20the,any%20shock%20to%20industrial%20earnings)
Korean steel industry hit by carbon permit costs, high tariffs, ETInfra

<https://infra.economictimes.indiatimes.com/news/construction/korean-steel-industry-hit-by-carbon-permit-costs-high-tariffs/124632233>

[\[11\]](https://icapcarbonaction.com/en/ets/korea-emissions-trading-system-k-ets#:~:text=Qualitative%20limit%3A%20The%20use%20only,April%202010)
[\[12\]](https://icapcarbonaction.com/en/ets/korea-emissions-trading-system-k-ets#:~:text=Quantitative%20limit%3A%C2%A0Up%20to%205,compliance%20obligation%2C%20regardless%20of%20type)
Korea Emissions Trading System (K-ETS) \| International Carbon Action
Partnership

<https://icapcarbonaction.com/en/ets/korea-emissions-trading-system-k-ets>

[\[15\]](https://www.carbon-direct.com/insights/inside-japan-s-gx-ets-carbon-market-and-its-global-climate-impact#:~:text=Japan%20maintains%20a%20small%20carbon,fossil%20fuel%20consumption%20and%20complementing)
[\[18\]](https://www.carbon-direct.com/insights/inside-japan-s-gx-ets-carbon-market-and-its-global-climate-impact#:~:text=In%20October%202023%2C%20the%20Tokyo,voluntary%20credits%20through%20an%20online)
Inside Japan's GX-ETS carbon market and its global climate impact \|
Carbon Direct

<https://www.carbon-direct.com/insights/inside-japan-s-gx-ets-carbon-market-and-its-global-climate-impact>

[\[19\]](https://www.renewable-ei.org/en/activities/column/REupdate/20251023.php#:~:text=Prior%20to%20this%20summary%2C%20the,side%20support%20measures)
Decarbonizing Steel (Part 1: Japan): Remaining Challenges for Mass
Balance Products \| Column \| Renewable Energy Institute

<https://www.renewable-ei.org/en/activities/column/REupdate/20251023.php>

[\[20\]](https://www.reuters.com/sustainability/boards-policy-regulation/indian-coal-prices-be-lower-after-tax-revision-industry-officials-say-2025-09-04/#:~:text=India%27s%20finance%20minister%20hiked%20consumption,ton%2C%20known%20as%20a%20cess)
Indian coal prices to be lower after tax revision, industry officials
say \| Reuters

<https://www.reuters.com/sustainability/boards-policy-regulation/indian-coal-prices-be-lower-after-tax-revision-industry-officials-say-2025-09-04/>

[\[21\]](https://www.pib.gov.in/PressNoteDetails.aspx?id=154721&NoteId=154721&ModuleId=3®=3&lang=2#:~:text=,outperform%20benchmark%20emissions%20intensity%20levels)
[\[27\]](https://www.pib.gov.in/PressNoteDetails.aspx?id=154721&NoteId=154721&ModuleId=3®=3&lang=2#:~:text=On%20March%2028%2C%202025%2C%20India%E2%80%99s,generating%20voluntary%20carbon%20credits%20including)
[\[35\]](https://www.pib.gov.in/PressNoteDetails.aspx?id=154721&NoteId=154721&ModuleId=3®=3&lang=2#:~:text=,outperform%20benchmark%20emissions%20intensity%20levels)
Press Note Details: Press Information Bureau

<https://www.pib.gov.in/PressNoteDetails.aspx?id=154721&NoteId=154721&ModuleId=3®=3&lang=2>

[\[23\]](https://www.reuters.com/sustainability/boards-policy-regulation/indias-steel-exports-europe-set-drop-eu-carbon-tax-looms-2025-12-05/#:~:text=Imports%20of%20steel%20into%20the,electricity%2C%20fertilisers%20and%20other%20products)
[\[24\]](https://www.reuters.com/sustainability/boards-policy-regulation/indias-steel-exports-europe-set-drop-eu-carbon-tax-looms-2025-12-05/#:~:text=%22About%2060,said%20one%20of%20the%20executives)
[\[25\]](https://www.reuters.com/sustainability/boards-policy-regulation/indias-steel-exports-europe-set-drop-eu-carbon-tax-looms-2025-12-05/#:~:text=NEW%20DELHI%2C%20Dec%205%20,industry%20executives%20and%20analysts%20said)
[\[26\]](https://www.reuters.com/sustainability/boards-policy-regulation/indias-steel-exports-europe-set-drop-eu-carbon-tax-looms-2025-12-05/#:~:text=Additional%20planned%20capacity%20could%20add,based%20research%20group)
India\'s steel exports to Europe set to drop as EU carbon tax looms \|
Reuters

<https://www.reuters.com/sustainability/boards-policy-regulation/indias-steel-exports-europe-set-drop-eu-carbon-tax-looms-2025-12-05/>

[\[29\]](https://icapcarbonaction.com/en/ets/china-national-ets#:~:text=The%20China%20national%20ETS%20regulates,to%20other%20sectors%20over%20time)
[\[30\]](https://icapcarbonaction.com/en/ets/china-national-ets#:~:text=Current%20Allowance%20Price%20)
[\[31\]](https://icapcarbonaction.com/en/ets/china-national-ets#:~:text=In%C2%A0March%202025%2C%20the%20MEE%C2%A0published%20a,2%7De)
[\[33\]](https://icapcarbonaction.com/en/ets/china-national-ets#:~:text=In%20January%202024%2C%20China%20launched,see%20%E2%80%98Offset%20Credits%E2%80%99%20section)
China National ETS \| International Carbon Action Partnership

<https://icapcarbonaction.com/en/ets/china-national-ets>

[\[34\]](https://www.climatebonds.net/news-events/press-room/press-releases/targeted-incentives-key-accelerating-chinas-steel-sector-transition#:~:text=Targeted%20Incentives%20Key%20to%20Accelerating,gap%20in%20steel%20transition%20finance)
Targeted Incentives Key to Accelerating China\'s Steel Sector...

<https://www.climatebonds.net/news-events/press-room/press-releases/targeted-incentives-key-accelerating-chinas-steel-sector-transition>
