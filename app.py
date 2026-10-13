"""
Data Detective Challenge - Group 6
Cybersecurity Incident Analytics Dashboard (2015-2024)
Course: Data Visualization Techniques (CCP7005)

Run with:  streamlit run app.py
"""
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

# ------------------------------------------------------------------
# 1. PAGE SETUP
# ------------------------------------------------------------------
st.set_page_config(
    page_title="Cybersecurity Incident Analytics",
    page_icon=":shield:",
    layout="wide",
)

CSV_NAME = "Global_Cybersecurity_Threats_2015-2024.csv"
NAVY = "#1F3A5F"
RED = "#C0392B"

# Country name -> ISO-3 code (needed for the world map)
ISO3 = {
    "China": "CHN", "India": "IND", "UK": "GBR", "Germany": "DEU",
    "France": "FRA", "Australia": "AUS", "Russia": "RUS",
    "Brazil": "BRA", "Japan": "JPN", "USA": "USA",
}


def show(fig):
    """Display a Plotly figure full width (works on old and new Streamlit)."""
    try:
        st.plotly_chart(fig, width="stretch")
    except TypeError:
        st.plotly_chart(fig, use_container_width=True)


# ------------------------------------------------------------------
# 2. LOAD DATA
# ------------------------------------------------------------------
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    # Short, code-friendly column names
    df.columns = [
        "Country", "Year", "Attack Type", "Industry", "Loss",
        "Users", "Source", "Vulnerability", "Defense", "Hours",
    ]
    df["ISO3"] = df["Country"].map(ISO3)
    return df


data_path = Path(__file__).parent / CSV_NAME
if data_path.exists():
    df = load_data(data_path)
else:
    up = st.file_uploader(f"Upload {CSV_NAME}", type="csv")
    if up is None:
        st.info("Place the CSV next to app.py or upload it above.")
        st.stop()
    df = load_data(up)

# ------------------------------------------------------------------
# 3. TITLE AND OBJECTIVE
# ------------------------------------------------------------------
st.title("Cybersecurity Incident Analytics Dashboard")
st.caption("Data Detective Challenge | Group 6 | Data Visualization Techniques (CCP7005)")
st.markdown(
    "**Objective:** Understand where, when and how cyber incidents happen, how much "
    "damage they cause, and which defences resolve them fastest, so that security "
    "teams can make better decisions."
)
with st.expander("About the dataset"):
    st.write(
        "**Source:** Kaggle, *Global Cybersecurity Threats 2015-2024*. "
        "Each row is one cybersecurity incident (3,000 records, 10 attributes, "
        "10 countries, 7 industries, 6 attack types, 2015 to 2024). "
        "Loss is in million US dollars and resolution time is in hours. "
        "The dataset is a public compilation, so differences between groups "
        "are modest."
    )

# ------------------------------------------------------------------
# 4. SIDEBAR FILTERS
# ------------------------------------------------------------------
st.sidebar.header("Filters")
yr_min, yr_max = int(df["Year"].min()), int(df["Year"].max())
years = st.sidebar.slider("Year range", yr_min, yr_max, (yr_min, yr_max))


def multi(label, col):
    options = sorted(df[col].unique())
    return st.sidebar.multiselect(label, options, default=options)


countries = multi("Country", "Country")
attacks = multi("Attack Type", "Attack Type")
industries = multi("Target Industry", "Industry")
defenses = multi("Defense Mechanism", "Defense")

f = df[
    df["Year"].between(*years)
    & df["Country"].isin(countries)
    & df["Attack Type"].isin(attacks)
    & df["Industry"].isin(industries)
    & df["Defense"].isin(defenses)
]

st.sidebar.markdown("---")
st.sidebar.write(f"Showing **{len(f):,}** of {len(df):,} incidents")

if f.empty:
    st.warning("No incidents match the selected filters. Please widen the filters.")
    st.stop()

# ------------------------------------------------------------------
# 5. KPIs
# ------------------------------------------------------------------
k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Total Incidents", f"{len(f):,}")
k2.metric("Total Loss", f"${f['Loss'].sum() / 1000:,.1f} B")
k3.metric("Avg Loss / Incident", f"${f['Loss'].mean():,.1f} M")
k4.metric("Avg Resolution Time", f"{f['Hours'].mean():,.1f} hrs")
k5.metric("Users Affected", f"{f['Users'].sum() / 1e6:,.0f} M")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Dashboard", "Bonus Insight", "Findings & Recommendations", "Wrong Visualization Challenge"]
)

# ------------------------------------------------------------------
# 6. MAIN DASHBOARD (Q1 to Q5)
# ------------------------------------------------------------------
with tab1:
    left, right = st.columns(2)

    # Q1 - Choropleth map
    with left:
        st.subheader("Q1. Which countries lose the most money?")
        c = f.groupby(["Country", "ISO3"], as_index=False)["Loss"].sum()
        c["Loss ($B)"] = (c["Loss"] / 1000).round(2)
        fig = px.choropleth(
            c, locations="ISO3", color="Loss ($B)", hover_name="Country",
            color_continuous_scale="Reds",
        )
        fig.update_geos(showframe=False, showcoastlines=False, projection_type="natural earth")
        fig.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=380)
        show(fig)
        top = c.sort_values("Loss", ascending=False).iloc[0]
        st.caption(f"Highest loss in current view: **{top['Country']}** (${top['Loss ($B)']:.1f} B).")

    # Q2 - Time series
    with right:
        st.subheader("Q2. How did incidents and losses change over time?")
        y = f.groupby("Year").agg(Incidents=("Loss", "size"), Loss=("Loss", "sum")).reset_index()
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=y["Year"], y=y["Incidents"], name="Incidents",
                                 mode="lines+markers", line=dict(color=NAVY, width=3)), secondary_y=False)
        fig.add_trace(go.Scatter(x=y["Year"], y=y["Loss"] / 1000, name="Total loss ($B)",
                                 mode="lines+markers", line=dict(color=RED, width=3, dash="dot")), secondary_y=True)
        fig.update_yaxes(title_text="Incidents", secondary_y=False)
        fig.update_yaxes(title_text="Total loss ($B)", secondary_y=True)
        fig.update_xaxes(dtick=1)
        fig.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=380,
                          legend=dict(orientation="h", y=1.12))
        show(fig)
        st.caption("Look for direction, not single spikes: the trend is a slight drift, not a surge.")

    left, right = st.columns(2)

    # Q3 - Heatmap attack x industry (loss)
    with left:
        st.subheader("Q3. Which attack hurts which industry most?")
        p = f.pivot_table(index="Attack Type", columns="Industry", values="Loss", aggfunc="sum").fillna(0) / 1000
        fig = px.imshow(p.round(2), text_auto=".1f", aspect="auto",
                        color_continuous_scale="Reds", labels=dict(color="Loss ($B)"))
        fig.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=380)
        show(fig)
        st.caption("Darker cell = more total loss (in $ billion).")

    # Q4 - Heatmap defence x attack (hours)
    with right:
        st.subheader("Q4. Which defence resolves which attack fastest?")
        p = f.pivot_table(index="Defense", columns="Attack Type", values="Hours", aggfunc="mean")
        fig = px.imshow(p.round(1), text_auto=".1f", aspect="auto",
                        color_continuous_scale="Blues_r", labels=dict(color="Avg hours"))
        fig.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=380)
        show(fig)
        st.caption("Darker cell = faster resolution (fewer average hours).")

    # Q5 - Scatter with trendline
    st.subheader("Q5. Do incidents affecting more users also cost more?")
    fig = px.scatter(f, x="Users", y="Loss", color="Industry", opacity=0.55,
                     labels={"Users": "Users affected", "Loss": "Financial loss ($ million)"})
    if len(f) > 2:
        m, b = np.polyfit(f["Users"], f["Loss"], 1)
        xs = np.array([f["Users"].min(), f["Users"].max()])
        fig.add_trace(go.Scatter(x=xs, y=m * xs + b, mode="lines", name="Trendline",
                                 line=dict(color="black", width=3)))
        r = np.corrcoef(f["Users"], f["Loss"])[0, 1]
    else:
        r = float("nan")
    fig.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=420)
    show(fig)
    st.caption(f"Correlation between users affected and loss: **r = {r:.3f}** "
               "(close to 0 means almost no relationship).")

# ------------------------------------------------------------------
# 7. BONUS INSIGHT (Q6)
# ------------------------------------------------------------------
with tab2:
    st.subheader("Bonus Q6. How do attack source, weakness and attack type connect?")
    st.write("Click a segment to zoom in. Rings from the centre: Attack Source, Vulnerability, Attack Type.")
    fig = px.sunburst(f, path=["Source", "Vulnerability", "Attack Type"],
                      color="Source", color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=650)
    show(fig)

# ------------------------------------------------------------------
# 8. FINDINGS AND RECOMMENDATIONS (full dataset)
# ------------------------------------------------------------------
with tab3:
    st.caption("Findings below are calculated on the full dataset of 3,000 incidents.")
    st.subheader("Five Major Findings")
    st.markdown(
        """
1. **Losses are spread widely across countries, led by the UK.** The UK loses about $16.5 B (10.9%) and China about $13.7 B (9.1%); the gap is only about 20%.
2. **Incidents and losses show a slight upward drift, not a surge.** Incidents rise about 2.6 per year; total loss in 2020-2024 ($78.9 B) is about 8.7% above 2015-2019 ($72.6 B).
3. **Phishing against Banking is the biggest hotspot** at about $5.1 B, while Phishing against Telecommunications is among the lowest at about $2.6 B.
4. **No single defence is best, but some pairings work better.** Firewall against DDoS is fastest (about 32.3 hrs); Encryption against Malware is slowest (about 40.6 hrs).
5. **More affected users does not mean higher loss.** The correlation is about 0.002, effectively zero.
        """
    )
    st.subheader("Three Actionable Recommendations")
    st.markdown(
        """
1. **Prioritise anti-phishing controls in Banking:** email filtering, multi-factor authentication and staff training.
2. **Match defences to attack types and test weak pairings:** use firewall protection first against DDoS; add endpoint detection and tested backups where encryption alone is used against malware. Pilot before large spending.
3. **Measure severity with several indicators and prepare for zero-day weaknesses:** build a risk score from loss, resolution time and users; strengthen patching and monitoring.
        """
    )

# ------------------------------------------------------------------
# 9. WRONG VISUALIZATION CHALLENGE
# ------------------------------------------------------------------
with tab4:
    st.subheader("Question: Which countries suffer the highest financial loss?")
    cl = df.groupby("Country", as_index=False)["Loss"].sum()
    cl["Loss ($B)"] = (cl["Loss"] / 1000).round(2)
    a, b = st.columns(2)
    with a:
        st.markdown("**Correct: sorted bar chart**")
        s = cl.sort_values("Loss ($B)")
        fig = px.bar(s, x="Loss ($B)", y="Country", orientation="h", text="Loss ($B)",
                     color_discrete_sequence=[NAVY])
        fig.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=400)
        show(fig)
        st.write("Bars share a baseline and are sorted, so exact comparison and ranking are easy.")
    with b:
        st.markdown("**Wrong: ten-slice pie chart**")
        fig = px.pie(cl, names="Country", values="Loss")
        fig.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=400)
        show(fig)
        st.write("Ten slices near 10% look identical. The ranking is hidden and readers may wrongly "
                 "conclude every country loses the same amount.")
