library(tidyverse)

# -----------------------------
# Input data
# -----------------------------
football_df <- tribble(
  ~segment, ~min, ~p25, ~median, ~p75, ~max,
  "Domestic + Construction", 386, 710, 1052, 1476, 2684,
  "Domestic + Automobile",   442, 811, 1202, 1687, 3067,
  "Export + Construction",   407, 1111, 2028, 5402, 18024,
  "Export + Automobile",     462, 1247, 2232, 5515, 18407
)

tata_corridor <- football_df %>%
  mutate(
    tata_low  = median,
    tata_high = p75
  )

# -----------------------------
# Plot
# -----------------------------
p <- ggplot(football_df, aes(y = segment)) +

  # Full feasible range (Min–Max)
  geom_segment(
    aes(x = min, xend = max, yend = segment, color = "Market feasible range"),
    linewidth = 1.2
  ) +

  # Interquartile range (P25–P75)
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

  # Median marker
  geom_point(
    aes(x = median, color = "Median market price"),
    size = 3,
    shape = 95
  ) +

  # Tata Steel pricing corridor
  geom_rect(
    data = tata_corridor,
    aes(
      xmin = tata_low,
      xmax = tata_high,
      ymin = as.numeric(factor(segment)) - 0.18,
      ymax = as.numeric(factor(segment)) + 0.18,
      fill = "Tata Steel optimal pricing corridor"
    ),
    alpha = 0.35
  ) +

  # Annotation explaining horizontal line
  annotate(
    "text",
    x = 12000,
    y = 4.4,
    label = "Horizontal line = full feasible premium range\n(Min–Max across scenarios)",
    hjust = 0,
    size = 3.5,
    color = "grey30"
  ) +

  # Annotation explaining box
  annotate(
    "text",
    x = 12000,
    y = 4.15,
    label = "Box = market clearing zone (P25–P75)",
    hjust = 0,
    size = 3.5,
    color = "grey30"
  ) +

  # Scales
  scale_x_continuous(
    labels = scales::comma_format(),
    expand = expansion(mult = c(0.02, 0.1))
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
      "Tata Steel optimal pricing corridor" = "steelblue"
    ),
    name = NULL
  ) +

  labs(
    title = "Green Steel Premium Football Field (₹/t steel)",
    subtitle = "Scenario-based premium ranges with Tata Steel recommended pricing corridor",
    x = "Green premium (₹ per tonne of steel)",
    y = NULL,
    caption = "Source: Green steel pricing model; premiums derived from abatement cost, lifecycle amortization, and carbon pricing scenarios"
  ) +

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
  filename = "outputs/charts/green_steel_football_field_tata_pricing.pdf",
  plot = p,
  width = 12,
  height = 6,
  device = cairo_pdf
)

ggsave(
  filename = "outputs/charts/green_steel_football_field_tata_pricing.png",
  plot = p,
  width = 12,
  height = 6,
  dpi = 300,
  bg = "white"
)


#“Each horizontal line shows the full feasible range of green steel premiums across all scenarios. The box highlights where the market is most likely to clear, while the blue band marks Tata Steel’s optimal pricing corridor that balances value capture with adoption risk.”
# -----------------------------


