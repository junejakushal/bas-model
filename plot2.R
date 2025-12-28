library(tidyverse)

# --------------------------------
# Football field data (₹/t steel)
# --------------------------------
football_df <- tribble(
  ~segment,                ~min,  ~p25,  ~median, ~p75,  ~max,
  "EU Export Market",        4500, 6500,  8000,    9500, 10000,
  "India – Domestic",       1200, 1800,  2500,    3200, 3500,
  "India – Export (ex-EU)", 1500, 2500,  3300,    4200, 4500,
  "South Korea",             600, 1000,  1500,    2200, 2500,
  "Japan",                   300,  700,  1200,    1600, 1800
)

# --------------------------------
# Company pricing corridors (India only)
# --------------------------------
company_corridors <- tribble(
  ~segment,          ~company, ~low,  ~high,
  "India – Domestic","Tata",    2000, 3500,
  "India – Domestic","JSW",     1800, 3000,
  "India – Domestic","AMNS",    1500, 2500
)


p <- ggplot(football_df, aes(y = segment)) +

  # --------------------------------
  # Full feasible range (Min–Max)
  # --------------------------------
  geom_segment(
    aes(x = min, xend = max, yend = segment, color = "Market feasible range"),
    linewidth = 1.2
  ) +

  # --------------------------------
  # Market clearing zone (P25–P75)
  # --------------------------------
  geom_rect(
    aes(
      xmin = p25,
      xmax = p75,
      ymin = as.numeric(factor(segment)) - 0.15,
      ymax = as.numeric(factor(segment)) + 0.15,
      fill = "Market clearing zone (P25–P75)"
    ),
    alpha = 0.9
  ) +

  # --------------------------------
  # Median marker
  # --------------------------------
  geom_point(
    aes(x = median, color = "Median market price"),
    size = 3,
    shape = 95
  ) +

  # --------------------------------
  # India company pricing corridors
  # --------------------------------
  geom_rect(
    data = company_corridors,
    aes(
      xmin = low,
      xmax = high,
      ymin = as.numeric(factor(segment)) - 0.18,
      ymax = as.numeric(factor(segment)) + 0.18,
      fill = company
    ),
    alpha = 0.35
  ) +

  # --------------------------------
  # Annotations
  # --------------------------------
  annotate(
    "text",
    x = 7500,
    y = 5.3,
    label = "Line = full feasible premium range (Min–Max)",
    hjust = 0,
    size = 3.5,
    color = "grey30"
  ) +
  annotate(
    "text",
    x = 7500,
    y = 5.05,
    label = "Box = market clearing zone (P25–P75)",
    hjust = 0,
    size = 3.5,
    color = "grey30"
  ) +

  # --------------------------------
  # Scales
  # --------------------------------
  scale_x_continuous(
    labels = scales::comma_format(),
    expand = expansion(mult = c(0.02, 0.12))
  ) +

  scale_color_manual(
    values = c(
      "Market feasible range" = "grey40",
      "Median market price"   = "black"
    ),
    name = NULL
  ) +

  scale_fill_manual(
    values = c(
      "Market clearing zone (P25–P75)" = "grey70",
      "Tata" = "#1f77b4",
      "JSW"  = "#2ca02c",
      "AMNS" = "#ff7f0e"
    ),
    name = "India company pricing corridor"
  ) +

  # --------------------------------
  # Labels
  # --------------------------------
  labs(
    title = "Green Steel Premium Football Field (₹/t steel)",
    subtitle = "Cross-market premium ranges with Indian producer pricing corridors",
    x = "Green premium (₹ per tonne of steel)",
    y = NULL,
    caption = "Premiums reflect carbon pricing, CBAM exposure, lifecycle amortization, and observed market willingness to pay"
  ) +

  # --------------------------------
  # Theme (Goldman / McKinsey style)
  # --------------------------------
  theme_minimal(base_size = 13) +
  theme(
    panel.grid.major.y = element_blank(),
    panel.grid.minor = element_blank(),
    axis.text.y = element_text(face = "bold"),
    plot.title = element_text(face = "bold"),
    plot.subtitle = element_text(color = "grey30"),
    legend.position = "bottom",
    legend.box = "horizontal"
  )

p


ggsave(
  filename = "outputs/charts/green_steel_football_field_global_india_overlay.pdf",
  plot = p,
  width = 13,
  height = 6,
  device = cairo_pdf
)

ggsave(
  filename = "outputs/charts/green_steel_football_field_global_india_overlay.png",
  plot = p,
  width = 13,
  height = 6,
  dpi = 300,
  bg = "white"
)
