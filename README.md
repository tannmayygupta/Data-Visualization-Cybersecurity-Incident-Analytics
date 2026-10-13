# Cybersecurity Incident Analytics Dashboard

An interactive Streamlit + Plotly dashboard that explores a decade of global cyber incidents (2015–2024): where they happen, how much they cost, and which defences resolve them fastest.

> **Data Detective Challenge** · Group 6 · B.Tech. (Cyber Security), Semester VII · Data Visualization Techniques (CCP7005)

---

## Objective

Understand **where, when and how** cyber incidents happen, **how much damage** they cause, and **which defences** resolve them fastest, so that security teams can make better decisions.

## Dataset

| | |
|---|---|
| **Source** | Kaggle – *Global Cybersecurity Threats 2015-2024* |
| **File** | `Global_Cybersecurity_Threats_2015-2024.csv` |
| **Size** | 3,000 incidents × 10 attributes |
| **Coverage** | 10 countries · 7 industries · 6 attack types · 2015–2024 |
| **Quality** | 0 missing values, 0 duplicates, 0 outliers (IQR method) |

**Columns:** Country, Year, Attack Type, Target Industry, Financial Loss (million $), Number of Affected Users, Attack Source, Security Vulnerability Type, Defense Mechanism Used, Incident Resolution Time (hours).

**Why this dataset?** It has a time column (trends), a country column (maps), money/users/time columns (KPIs) and many category columns (heatmaps, sunburst). It is clean and small enough to load instantly.

**Honest limitation:** values are spread very evenly (e.g. average loss ≈ \$50 M in a 0.5–100 M range, no outliers), which suggests the data is compiled or partly simulated. Differences between groups are therefore modest, and we avoid exaggerating them.

## Features

- **Five interactive filters:** year range, country, attack type, target industry, defence mechanism
- **Five KPIs** that update with the filters: total incidents, total loss, average loss per incident, average resolution time, users affected
- **Four tabs:** Dashboard, Bonus Insight, Findings & Recommendations, Wrong Visualization Challenge

## Analytical questions and chart choices

| # | Question | Chart | Why this chart |
|---|---|---|---|
| Q1 | Which countries lose the most money? | Choropleth map | Place data reads naturally on a map |
| Q2 | How did incidents and losses change over time? | Dual-axis line chart | Lines show direction; two axes because incidents are in hundreds and loss in billions |
| Q3 | Which attack type hurts which industry most? | Heatmap | Colour intensity reveals hotspots |
| Q4 | Which defence resolves which attack fastest? | Heatmap | A matrix gives a practical lookup |
| Q5 | Do incidents affecting more users also cost more? | Scatter + trendline | Shows the relationship between two numbers |
| Q6 *(bonus)* | How do source, weakness and attack type connect? | Sunburst | Hierarchy in one clickable chart |

The main dashboard keeps to five charts (Q1–Q5); Q6 sits in its own **Bonus Insight** tab.

## Key findings

1. **Losses are spread widely, led by the UK** (~\$16.5 B, 10.9%) with China lowest (~\$13.7 B, 9.1%): a gap of only ~20%.
2. **A slight upward drift, not a surge.** Total loss in 2020–2024 (~\$78.9 B) is ~8.7% above 2015–2019 (~\$72.6 B).
3. **Phishing against Banking is the biggest hotspot** (~\$5.1 B); Phishing against Telecommunications is among the lowest (~\$2.6 B).
4. **No single defence wins everywhere.** Firewall vs DDoS is fastest (~32.3 hrs); Encryption vs Malware is slowest (~40.6 hrs).
5. **More affected users does not mean higher loss** (correlation r ≈ 0.002).

*Bonus:* Nation-state is the largest attack source (26.5% of incidents) and Zero-day is the most common weakness (26.2%).

## Recommendations

1. **Prioritise anti-phishing controls in Banking:** email filtering, multi-factor authentication, staff training.
2. **Match defences to attack types and pilot weak pairings** before large spending (firewall first for DDoS; add endpoint detection and tested backups against malware).
3. **Measure severity with several indicators** (loss, resolution time, users) and strengthen patching and monitoring for zero-day weaknesses.

## Wrong Visualization Challenge

The same question, "Which countries suffer the highest financial loss?", is drawn twice:

- **Correct:** sorted horizontal bar chart. Shared baseline, easy to compare lengths and read the ranking.
- **Wrong:** ten-slice pie chart. Ten near-equal slices look identical, hiding the ranking and implying every country loses the same.

People compare lengths well but angles and areas badly; pies only work for roughly 2–5 parts.

## Tech stack

| Library | Used for |
|---|---|
| Streamlit | Web app, filters, KPIs, tabs |
| Plotly (`express`, `graph_objects`, `subplots`) | Interactive charts |
| pandas | Loading, filtering, group-by, pivot tables |
| NumPy | Trendline and correlation |

## Getting started

Requires **Python 3.9+**.

```bash
git clone https://github.com/tannmayygupta/Data-Visualization-Cybersecurity-Incident-Analytics.git
cd Data-Visualization-Cybersecurity-Incident-Analytics

pip install -r requirements.txt
streamlit run app.py
```

The app opens at <http://localhost:8501>. Keep the CSV in the same folder as `app.py`; if it is missing, the app shows an upload box.

## Project structure

```
├── app.py                                    # Streamlit dashboard
├── Global_Cybersecurity_Threats_2015-2024.csv # dataset
├── requirements.txt
└── README.md
```

## How it works

Streamlit re-runs `app.py` from top to bottom on every interaction. The sidebar filters build one filtered table (`f`), and every KPI and chart is drawn from `f`, so everything updates together. `@st.cache_data` keeps the CSV in memory so it isn't re-read on each click. The Findings tab and the Wrong Visualization tab use the full dataset so their conclusions stay fixed.

