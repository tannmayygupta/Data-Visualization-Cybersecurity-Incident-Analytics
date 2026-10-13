---
title: "Group 6 – Data Detective Challenge: Complete Preparation Guide"
subtitle: "Cybersecurity Incident Analytics | Data Visualization Techniques (CCP7005) | LA-2"
---

# How to use this guide

This guide explains **everything we did in our chat, from the first message to the final dashboard**, in simple language. After reading it, any team member should be able to answer: *What did we do? Why did we do it? How does the code work?*

**Roll numbers of Group 6:** 6, 24, 41, 59.

**Reading order:** Parts 1 to 4 explain the task and the decisions. Parts 5 to 8 explain the analysis. Part 9 explains the dashboard code. Part 10 explains how the Word document was made. Parts 11 and 12 are likely teacher questions and a glossary.

---

# Part 1. Understanding the task

## 1.1 What the college asked for (in plain words)

The college gave an activity called **Data Detective Challenge** (10 marks). We act like a small **consulting company**. We receive a topic, find a real dataset about it, study it, and build a **web dashboard** (a web page with charts, filters and headline numbers). The dashboard must tell a story and end with advice.

## 1.2 Our group and our topic

| Item | Value |
|---|---|
| Group | 6 |
| Roll numbers | 6, 24, 41, 59 |
| Assigned domain | Cybersecurity Incident Analytics |
| Programme | B. Tech. (Cyber Security), Semester VII |
| Course | Data Visualization Techniques, CCP7005 |

The college said the group and domain allocation is final, so we could not change the topic.

## 1.3 Everything the task required

1. **Find a real dataset** about our domain.
2. **Dataset Discovery Summary:** rows, columns, number columns, category columns, dates/locations, missing values, duplicates, outliers, patterns.
3. **At least five analytical questions**, each with: variables needed, the chart proposed, and why that chart fits.
4. **Choose suitable visualizations.** We are not required to use every technique. The choice must depend on the question.
5. **Build an interactive dashboard** in Streamlit or Dash with Plotly. It must contain a title and objective, a data description, KPIs, interactive filters, 3 to 5 charts, five findings and three recommendations.
6. **Wrong Visualization Challenge:** show one question with a correct chart and a deliberately bad chart, and explain why the bad one misleads.
7. **AI as a Critic:** ask an AI tool to critique one chart. Record: the AI recommendation, whether we ACCEPTED / PARTIALLY ACCEPTED / REJECTED it, and our justification.
8. **2-minute Data Story:** what we found, why it matters, what action to take. No code talk.
9. **Final submission** as one .zip.

## 1.4 Latest notice from the teacher

- Finish by **Wednesday, 14-10-2026**.
- Present group-wise (2 minutes) on **Thursday, 15-10-2026**, LA-2 (3 to 5 PM).
- Submit: **(1)** a Doc file with all details, **(2)** a 2 to 3 slide presentation with group details, dashboard, and questions analysed.
- LA-2 is out of 25 marks: Innovative Self-Learning Activity and presentation 10, attendance and timely lab submission 10, MCQ quiz 5. **No absentee LA-2 will be conducted.**

## 1.5 The three rules you gave me for this chat

1. I should **not make assumptions**; I ask you small clarifying questions.
2. I explain in **layman language**.
3. Research should follow **industry-driven practice**.

Because of rule 3, we used standard practice: check data quality first, choose charts based on the question, show KPIs, and state limits of the data honestly.

---

# Part 2. How the chat progressed (step by step)

| Step | What happened | Why |
|---|---|---|
| 1 | You pasted the task sheet and the teacher's notice. | I needed the real requirements. |
| 2 | I explained the task in simple words. | You said you did not understand it. |
| 3 | You gave group 6, roll no. 59, domain Cybersecurity Incident Analytics. | The domain is fixed by the college. |
| 4 | I listed three dataset options and recommended one. | We needed to choose a dataset. |
| 5 | You asked me to recommend one; I searched the web to verify the recommended dataset. | Facts should be checked, not guessed. |
| 6 | I asked whether the team knows Streamlit; you said yes. | To set the code difficulty. |
| 7 | You downloaded the CSV and uploaded it. | I needed to see the real columns. |
| 8 | I opened the file and checked rows, columns, missing values, duplicates, outliers. | This is the Dataset Discovery step. |
| 9 | I proposed 12 questions and the top 5; you asked to add Q9 as a sixth. | You wanted to cover more and impress. |
| 10 | I advised keeping 5 charts on the main dashboard and Q6 as a labelled bonus. | The rule says 3 to 5 charts. |
| 11 | I produced the formal Word document. | Required submission item. |
| 12 | You asked Power BI or Streamlit; I said Streamlit. | The task says Streamlit or Dash. |
| 13 | I built and tested the Streamlit dashboard. | Required submission item. |
| 14 | You asked for this preparation guide. | For viva and presentation readiness. |

---

# Part 3. Which dataset we chose, and why

## 3.1 The options I listed at the start

At the start I listed **three options**. Later, while searching the web, a **fourth** (University of Maryland) appeared, which I mentioned as a backup. All four are explained here.

### Option 1: Global Cybersecurity Threats 2015-2024 (Kaggle): **CHOSEN**

- Each row is one cyber incident from 2015 to 2024.
- Columns: Country, Year, Attack Type, Target Industry, Financial Loss, Number of Affected Users, Attack Source, Security Vulnerability Type, Defense Mechanism Used, Incident Resolution Time.
- 3,000 rows and 10 columns (we verified this from the actual file).

**Why we chose it**

1. **It has a time column (Year)**, so we can do time-series charts, which the task lists.
2. **It has a place column (Country)**, so we can draw a map, which the task also lists.
3. **It has money, users and time-to-fix numbers**, so we can build meaningful KPIs.
4. **It has many category columns** (attack type, industry, source, weakness, defence), so we can build heatmaps, treemaps and sunbursts.
5. **It is clean:** no missing values and no duplicates (we checked).
6. **It is small enough** (3,000 rows) to load instantly in Streamlit, which matters because we had only about one day.
7. **It is well known**, so there are other people's projects to compare with. We found a CMU (Carnegie Mellon) capstone report and a Power BI project using it.
8. **It matches the business-story style** the task wants: "what happened, where, how bad, how fixed".

**Weaknesses we found (we state them honestly)**

- The numbers are spread very evenly. For example, financial loss is spread between 0.5 and 99.99 million with an average of about 50. Affected users run from about 400 to about 1 million with an average of about 500,000. There are **no outliers**, which is unusual for real attack data.
- Because of this, the dataset looks like a **compiled or simulated** collection. A research paper that used it also reported no statistically significant increase in cyberattacks over time. So **differences between groups are small**, and we do not exaggerate.
- One website said the dataset has 13 columns. Our downloaded file has **10**. We use 10, because that is what our real file contains.
- Many other students and professionals may also use this dataset. So to be unique we chose our own question set, added a bonus sunburst question, and built extra features in the dashboard.

### Option 2: "Cybersecurity Attacks" dataset (Kaggle): not chosen

- Described as network attack logs with timestamps, IP addresses, protocols, severity and attack type.
- It feels more technical, like a security operations team.

**Why we did not choose it**

- It focuses on technical network details such as IP addresses and protocols. This makes **maps, industry comparison, and financial-loss KPIs** harder or impossible.
- The task wants a story with **decisions** (recommendations). Money and industry columns make recommendations easier.
- **Honest note:** we did not download or open this dataset in our chat. This reason is based on its description, not on a data inspection.

### Option 3: NSL-KDD, UNSW-NB15, CICIDS2017: not chosen

- These are famous **network intrusion research datasets** used mainly for machine learning.
- They contain technical network measurements such as packet counts, byte counts, protocol and connection flags.

**Why we did not choose them**

- They are **very large** (from hundreds of thousands to millions of rows). A laptop dashboard would be slow, and cleaning would eat our limited time.
- They are made for **training attack-detection models**, not for business storytelling. They have no country, industry or financial-loss columns.
- Most columns are technical numbers, so the five or more questions would be hard to explain to a non-technical teacher in 2 minutes.
- **Honest note:** again, we did not open these files in the chat. The reasons are based on how these datasets are generally described.

### Option 4 (backup, found during search): University of Maryland Cyber Events Database 2.0

- A publicly sourced database of global cyber events from 2014 onward. According to its publication, it had **16,382 coded events across 175 countries and 1,431 threat actors** as of February 2026.
- Each event is classified by actor type, motive, target sector, affected country and observable effects.

**Why it was only a backup**

- It is richer, but it is also **more complex** (many actors, many categories, news-based coding). Cleaning and explaining it in about a day is risky.
- It is designed for research. Our dataset is simpler and covers every task requirement already.
- We kept it as the plan B if Option 1 had failed.

## 3.2 Comparison table

| Dataset | Rows | Has time? | Has country? | Has money loss? | Easy to explain? | Verdict |
|---|---|---|---|---|---|---|
| Global Cybersecurity Threats 2015-2024 | 3,000 | Yes (Year) | Yes | Yes | Yes | **Chosen** |
| Cybersecurity Attacks (network logs) | Not checked | Timestamps | Not checked | No (severity only) | Technical | Not chosen |
| NSL-KDD / UNSW-NB15 / CICIDS2017 | Very large | Limited | No | No | Technical | Not chosen |
| UMD Cyber Events Database 2.0 | 16,382 | Yes | Yes | Not checked | Complex | Backup |

## 3.3 How we verified the chosen dataset

1. I searched the web for the dataset name. Results confirmed it is a Kaggle dataset and described its columns.
2. You downloaded the CSV from Kaggle and uploaded it.
3. I opened the file with Python (pandas) and confirmed: **3,000 rows, 10 columns, no missing values, no duplicates**, years 2015 to 2024, and the category lists.
4. This showed the file is the correct one.

---

# Part 4. Why Streamlit, and what Streamlit does

## 4.1 Why we needed to choose between tools

You asked: "Should I create it on Power BI or Streamlit?"

## 4.2 The answer and the reasons

We chose **Streamlit**.

1. **The task sheet says so.** It says "Streamlit OR Dash + Plotly". Power BI is not listed, so a Power BI dashboard would not meet the requirement.
2. **We must submit the source code** (the .zip needs "complete executable source code"). Streamlit is plain Python code, which is easy to submit and explain.
3. **Your team already knows Streamlit basics.**
4. **Streamlit is simpler than Dash.** Dash needs separate "callback" functions to connect filters to charts. Streamlit just re-runs the script, so filters work with very little code.
5. **It uses Plotly for charts**, which gives interactive hover, zoom and click.

## 4.3 What Streamlit does (layman explanation)

Streamlit is a free Python library that turns a Python script into a **web page**. You write Python; Streamlit makes the page.

- `st.title("Hello")` shows a heading on the web page.
- `st.slider(...)` shows a slider the user can move.
- `st.metric(...)` shows a big headline number.

**How it works:** every time the user changes a filter, Streamlit **re-runs the entire script from top to bottom** with the new filter values. Because the charts are built from the filtered data, they update automatically. This "re-run everything" idea is the single most important thing to remember about Streamlit.

## 4.4 What Plotly does

Plotly is a chart library. Its charts are **interactive** (hover for details, zoom, click). We used `plotly.express` (shorter code, called `px`) and `plotly.graph_objects` (more control, called `go`).

## 4.5 Why not Dash

Dash + Plotly is also allowed. It is more powerful but needs more code and the callback system. Since we had little time and the team knows Streamlit, Streamlit was the better choice.

---

# Part 5. How to analyse a dataset (the method we followed)

This is the standard process used in industry. You can describe it as a **six-step routine**.

| Step | What you do | What we did |
|---|---|---|
| 1. Look | Open the file, see rows and columns | 3,000 rows, 10 columns |
| 2. Types | Which columns are numbers and which are categories? | 4 numbers, 6 categories |
| 3. Quality | Missing values, duplicates, outliers | None found |
| 4. Describe | Averages, ranges, counts | See below |
| 5. Explore | Group, compare, correlate | Totals by country, attack, industry, year |
| 6. Question and chart | Turn patterns into questions and pick charts | 12 questions, then 6 selected |

## 5.1 Numerical vs categorical (layman)

- **Numerical** columns hold numbers you can add or average: Year, Financial Loss, Affected Users, Resolution Time.
- **Categorical** columns hold labels or groups: Country, Attack Type, Industry, Attack Source, Vulnerability, Defence.

This matters because the chart type depends on it. For example: category vs number suits bars, number vs number suits scatter, and category vs category suits heatmaps.

## 5.2 What we found in each quality check

| Check | How it is done | Result |
|---|---|---|
| **Missing values** | Count empty cells in each column | **0**. Every cell is filled. |
| **Duplicates** | Count rows that are exact copies | **0** |
| **Format problems** | Look at data types and category spellings | The columns have correct types (numbers are numbers, text is text). We did not find bad spellings. The only change was **shortening column names** for coding convenience, for example "Financial Loss (in Million $)" became "Loss". |
| **Outliers** | IQR method (explained below) | **0** in Loss, Users and Hours. Skewness is about 0. |

**Answer if asked "Was the data in a good format?":** Yes. It was clean and ready to use. We only renamed columns to make them easier to type in code.

## 5.3 The IQR outlier method in layman terms

1. Sort the numbers. Find Q1 (the value 25% of the way up) and Q3 (the value 75% of the way up).
2. IQR = Q3 minus Q1. This is the "middle spread".
3. Anything below `Q1 − 1.5 × IQR` or above `Q3 + 1.5 × IQR` is flagged as an outlier.

For our three number columns, **no value crossed those limits**, so there are no outliers. It is the same method a box plot uses to draw its dots.

## 5.4 Basic numbers (summary statistics)

| Column | Minimum | Average | Maximum |
|---|---|---|---|
| Financial Loss (million $) | 0.50 | 50.49 | 99.99 |
| Affected Users | 424 | 504,684 | 999,635 |
| Resolution Time (hours) | 1 | 36.48 | 72 |

The average is almost in the middle of the range in every case. That is the signal that the numbers are spread evenly. Real data usually has a few huge values pulling the average upward.

## 5.5 Correlation (how we checked relationships)

Correlation (r) measures whether two number columns move together. It runs from −1 to +1. Near 0 means "no relationship".

| Pair | r |
|---|---|
| Loss and Users | about 0.002 |
| Loss and Hours | about −0.013 |
| Users and Hours | about 0.006 |

All are practically zero. So in this data, a bigger loss does **not** mean more users or longer fixing time. This became Finding 5 and Question 5.

## 5.6 Group totals we calculated (basis for the findings)

We used "group by" (split rows into groups, then add or average each group). Examples:

- Total loss by Country: UK about 16.5 billion dollars (highest), China about 13.7 billion (lowest).
- Incidents by Year: peak 2017 (319), lowest 2019 (263).
- Loss by Attack Type and Industry: Phishing against Banking about 5.1 billion (highest pair), Phishing against Telecommunications about 2.6 billion (lowest).
- Average resolution hours by Defence and Attack: Firewall against DDoS about 32.3 (fastest), Encryption against Malware about 40.6 (slowest).

---

# Part 6. The 12 questions and how we chose the top 6

## 6.1 How we generated 12 questions

We used a simple trick: **look at each column and ask what interesting thing it can show**, and combine two or three columns.

- Place column → "Which countries?" (Q1, Q11)
- Time column → "How did it change?" (Q2)
- Two categories + a number → "Which pair is worst?" (Q3, Q4)
- Two numbers → "Are they related?" (Q5, Q12)
- Several categories in layers → "How do they connect?" (Q9)
- One number → "How spread out is it?" (Q10)
- One category → "Which is most common?" (Q6, Q7, Q8)

## 6.2 The full list of 12

| # | Question | Chart idea | Concept it covers |
|---|---|---|---|
| 1 | Which countries lose the most money? | Choropleth map | Geographical analysis |
| 2 | How did incidents and losses change 2015 to 2024? | Line chart | Time series / trend |
| 3 | Which attack type hurts which industry most? | Heatmap | Two categories vs a number |
| 4 | Which defence fixes which attack fastest? | Heatmap | Performance comparison |
| 5 | Do more affected users mean more loss? | Scatter plot | Correlation |
| 6 | Which industry is hit most often? | Bar chart | Ranking |
| 7 | Who is behind attacks? | Donut chart | Part-of-whole (few parts) |
| 8 | Which weakness is exploited most? | Bar chart | Ranking |
| 9 | How do source, weakness and attack type connect? | Sunburst / treemap | Hierarchy |
| 10 | How spread out are losses and times? | Histogram and box plot | Distribution and outliers |
| 11 | Which country is slowest at fixing incidents? | Bar chart | Ranking of a performance measure |
| 12 | Do all numeric columns relate to each other? | Correlation heatmap | Multi-variable correlation |

## 6.3 How we chose the top ones

We looked for questions that give **variety, business meaning, and a clear story**.

1. **Different chart types:** map, line, heatmap, heatmap, scatter. A dashboard with five bar charts looks boring and does not show skills.
2. **Cover the techniques the task names:** Choropleth, Time-series, Heatmap, Scatter, Plotly interactive charts, Sunburst.
3. **Actionable:** Q3 and Q4 directly lead to recommendations (protect banks from phishing, match defences to attacks).
4. **Honest surprise:** Q5 shows no relationship, which is an unexpected, interesting insight and also a good reminder not to assume.
5. **Skipped ones:** Q6, Q7, Q8 and Q11 are simple rankings (bar charts). They are correct but add little new compared with the chosen ones. Q10 and Q12 are mostly data-checking and fit in the Discovery Summary. Q7's donut would add little because the four sources are almost equal.

## 6.4 Final 6 and what concept each covers

| Q | Question | Chart | Concept | Why this chart fits |
|---|---|---|---|---|
| Q1 | Which countries lose the most? | Choropleth | Geographical | Place data is read most naturally on a map |
| Q2 | How did it change over time? | Line (two axes) | Time series | Lines show direction over time |
| Q3 | Which attack hurts which industry? | Heatmap | Cross-category comparison | Colour intensity reveals hotspots |
| Q4 | Which defence is fastest for which attack? | Heatmap | Performance comparison | A matrix gives a practical answer |
| Q5 | Do more users mean more loss? | Scatter + trendline | Correlation | Scatter plots show relationship between two numbers |
| Q6 | How do source, weakness, attack connect? | Sunburst | Hierarchy | Layers in one clickable circle |

## 6.5 Why 5 on the main dashboard and Q6 as a bonus

The task says the dashboard needs **3 to 5 charts**. If we put six on the main page, a teacher with a checklist might mark it as not following the instruction. So Q1 to Q5 are on the main tab (the 5 allowed), and Q6 sits in a clearly labelled **Bonus Insight** tab. This shows initiative without breaking the rule. The task also says we need at least five questions, so six is allowed.

---

# Part 7. Findings and recommendations

## 7.1 Five major findings (all calculated from the real data)

1. **Losses are spread widely, led by the UK.** UK about 16.5 billion dollars (10.9%) and China about 13.7 billion (9.1%). The gap is only about 20%.
2. **A slight upward drift, not a surge.** Incidents rise about 2.6 per year. Total loss in 2020 to 2024 was about 78.9 billion dollars against about 72.6 billion in 2015 to 2019 (roughly 8.7% higher).
3. **Phishing against Banking is the biggest hotspot** at about 5.1 billion dollars. Phishing against Telecommunications is the lowest pair at about 2.6 billion.
4. **No single defence is best, but some pairings work better.** Average resolution time is almost equal across defences (35.7 to 36.9 hours). Firewall against DDoS is fastest (about 32.3 hours). Encryption against Malware is slowest (about 40.6 hours).
5. **More affected users does not mean higher loss.** Correlation is about 0.002.

Bonus (Q6): Nation-state is the biggest source (26.5% of incidents) and Zero-day is the most common weakness (26.2%).

## 7.2 Three recommendations

1. **Prioritise anti-phishing controls in Banking** (email filtering, multi-factor authentication, staff training).
2. **Match defences to attack types and test weak pairings.** Use firewall protection first for DDoS. Where encryption is the main defence against malware, add endpoint detection and tested backups. Because differences are moderate, run a pilot before large spending.
3. **Measure severity with several indicators and prepare for zero-day weaknesses.** Build a risk score from loss, resolution time and users, and strengthen patching and monitoring.

## 7.3 Why we stated limits

A good analyst does not claim "cyber attacks are exploding" if the data does not show it. A teacher who checks the numbers will respect an honest conclusion. A research paper using the same dataset also found no significant increase in the number or severity of attacks.

---

# Part 8. Wrong Visualization Challenge

**Question chosen:** Which countries suffer the highest financial loss? (Q1)

| | Correct chart | Wrong chart |
|---|---|---|
| Type | Sorted horizontal bar chart | Ten-slice pie chart |
| Why | Bars share a baseline and are sorted, so you can compare lengths exactly | Ten slices each near 10% look identical |
| Effect | Ranking from UK to China is obvious | Readers cannot tell who is highest and may think every country is equal |

**Lesson:** humans compare lengths well but angles and areas badly. Pie charts only work for a few parts (about 2 to 5). The wrong chart is not "false", but it hides information, which can lead to poor decisions such as spending the same security budget everywhere.

---

# Part 9. The Streamlit code, explained piece by piece

The dashboard is one file, `app.py`. This part explains **every section**. The code is shown in small pieces with explanations.

## 9.1 Libraries used (and why)

| Library | What it is | Why we used it |
|---|---|---|
| `streamlit` | Turns Python into a web page | Required tool for the dashboard |
| `pandas` | Handles tables of data (called DataFrames) | Reading the CSV, filtering, grouping |
| `numpy` | Maths on numbers | Trendline and correlation |
| `plotly.express` | Quick interactive charts | Map, heatmaps, scatter, sunburst, pie, bar |
| `plotly.graph_objects` | Detailed chart building | Lines and the trendline on top of the scatter |
| `plotly.subplots` | Charts with two y-axes | Q2 shows incidents and loss on one chart |
| `pathlib.Path` | Handles file locations | Finds the CSV next to `app.py` |

## 9.2 The imports

```python
from pathlib import Path
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots
```

- `import X as Y` loads a library and gives it a short nickname, so `pd` means pandas, `px` means plotly express, `st` means streamlit.
- `from plotly.subplots import make_subplots` loads just one tool from a library.

## 9.3 Page setup

```python
st.set_page_config(
    page_title="Cybersecurity Incident Analytics",
    page_icon=":shield:",
    layout="wide",
)
```

- Sets the browser tab title and icon.
- `layout="wide"` uses the full screen width instead of a narrow centre column, which suits dashboards with many charts.
- This must be the **first** Streamlit command in the script.

## 9.4 Constants

```python
CSV_NAME = "Global_Cybersecurity_Threats_2015-2024.csv"
NAVY = "#1F3A5F"
RED = "#C0392B"
```

- Values we reuse are stored once at the top. If we change the file name or a colour, we change it in one place.
- The colours are hex codes (navy blue and red) used for chart lines.

## 9.5 The country code dictionary

```python
ISO3 = {"China": "CHN", "India": "IND", "UK": "GBR", ... "USA": "USA"}
```

- A **dictionary** pairs a key with a value.
- The world map needs standard 3-letter country codes (ISO-3). Our file has names such as "UK" and "USA", which maps sometimes cannot read. We translate: UK to GBR, USA to USA, and so on.
- Later we add this as a new column named `ISO3`.

## 9.6 The `show()` helper

```python
def show(fig):
    try:
        st.plotly_chart(fig, width="stretch")
    except TypeError:
        st.plotly_chart(fig, use_container_width=True)
```

- A **function** is a reusable block of code. Instead of writing the long display command 8 times, we write `show(fig)`.
- Newer Streamlit versions use `width="stretch"` to make a chart fill its column. Older versions use `use_container_width=True`.
- `try ... except TypeError` means: try the new way; if the version is old and complains, use the old way. This makes the code work on both versions, which matters because your team members may have different Streamlit versions.

## 9.7 Loading the data

```python
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    df.columns = ["Country", "Year", "Attack Type", "Industry", "Loss",
                  "Users", "Source", "Vulnerability", "Defense", "Hours"]
    df["ISO3"] = df["Country"].map(ISO3)
    return df
```

- `pd.read_csv(path)` reads the CSV into a table (DataFrame).
- `df.columns = [...]` renames all 10 columns in order. Short names are easier to type (we write `df["Loss"]` instead of the long original name).
- `df["Country"].map(ISO3)` creates a new column by looking up each country in the dictionary.
- `@st.cache_data` is a **decorator**. It tells Streamlit: "remember the result of this function". Since Streamlit re-runs the script on every click, caching avoids reloading the CSV each time and keeps the dashboard fast.

```python
data_path = Path(__file__).parent / CSV_NAME
if data_path.exists():
    df = load_data(data_path)
else:
    up = st.file_uploader(f"Upload {CSV_NAME}", type="csv")
    if up is None:
        st.info("Place the CSV next to app.py or upload it above.")
        st.stop()
    df = load_data(up)
```

- `Path(__file__).parent` means "the folder where app.py lives". We look for the CSV there.
- If the file is found, load it. If not, show an upload box so the user can provide it. `st.stop()` stops the app until the user uploads, so the rest of the code never runs on missing data.
- This makes the app friendly for teachers who run it on another machine.

## 9.8 Title, objective and dataset description

```python
st.title("Cybersecurity Incident Analytics Dashboard")
st.caption("Data Detective Challenge | Group 6 | Data Visualization Techniques (CCP7005)")
st.markdown("**Objective:** ...")
with st.expander("About the dataset"):
    st.write("**Source:** Kaggle ...")
```

- `st.title`, `st.caption`, `st.markdown`: big heading, small grey text, and formatted text (`**` makes bold).
- `st.expander` creates a collapsible box, so the dataset description is available but does not crowd the page.
- This covers the task requirement: **project title and objective, dataset/problem description**.

## 9.9 Sidebar filters (interactive controls)

```python
st.sidebar.header("Filters")
yr_min, yr_max = int(df["Year"].min()), int(df["Year"].max())
years = st.sidebar.slider("Year range", yr_min, yr_max, (yr_min, yr_max))
```

- `st.sidebar` places controls in the left panel.
- We find the smallest and largest year from the data (2015 and 2024) instead of typing them. If the dataset changes, the slider adjusts itself.
- A slider with two numbers `(yr_min, yr_max)` as the default gives a **range slider** with two handles.

```python
def multi(label, col):
    options = sorted(df[col].unique())
    return st.sidebar.multiselect(label, options, default=options)

countries  = multi("Country", "Country")
attacks    = multi("Attack Type", "Attack Type")
industries = multi("Target Industry", "Industry")
defenses   = multi("Defense Mechanism", "Defense")
```

- `df[col].unique()` lists each distinct value of a column. `sorted()` puts them in alphabetical order.
- `multiselect` lets the user pick several values. `default=options` means **everything is selected at the start**, so the dashboard shows all data initially.
- We wrote a small function `multi` because the same steps repeat four times. This avoids copy-paste.
- So we have **five interactive filters**: year, country, attack type, industry, defence.

## 9.10 Applying the filters

```python
f = df[
    df["Year"].between(*years)
    & df["Country"].isin(countries)
    & df["Attack Type"].isin(attacks)
    & df["Industry"].isin(industries)
    & df["Defense"].isin(defenses)
]
```

- Each line creates a True/False list for every row. `between(*years)` is true if the year is inside the slider range. `isin(countries)` is true if the row's country is in the selected list.
- The symbol `&` means **AND**. A row is kept only if **all five conditions are true**.
- The result, `f`, is the **filtered table**. **Every chart uses `f`**, not `df`, so charts respond to filters.

```python
if f.empty:
    st.warning("No incidents match the selected filters. Please widen the filters.")
    st.stop()
```

- If the user unticks everything, there is no data and charts would crash. This shows a friendly message and stops. This is good practice called **error handling**.

## 9.11 KPIs

```python
k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Total Incidents", f"{len(f):,}")
k2.metric("Total Loss", f"${f['Loss'].sum() / 1000:,.1f} B")
k3.metric("Avg Loss / Incident", f"${f['Loss'].mean():,.1f} M")
k4.metric("Avg Resolution Time", f"{f['Hours'].mean():,.1f} hrs")
k5.metric("Users Affected", f"{f['Users'].sum() / 1e6:,.0f} M")
```

- **KPI** means Key Performance Indicator: a headline number. We show five.
- `st.columns(5)` splits the page into five equal columns, so the KPIs sit in a row.
- `len(f)` counts rows (incidents). `.sum()` adds up, `.mean()` averages.
- Loss is in millions, so dividing by 1,000 gives billions (`B`). Users are divided by 1,000,000 (`1e6`) to show millions (`M`).
- The `:,.1f` inside the text is a **format code**: `,` adds thousand separators and `.1f` shows one decimal place. For example 151478.91 becomes 151.5.
- Because KPIs use `f`, they **change when filters change**.

## 9.12 Tabs

```python
tab1, tab2, tab3, tab4 = st.tabs(
    ["Dashboard", "Bonus Insight", "Findings & Recommendations", "Wrong Visualization Challenge"])
```

- Tabs organise content so the page is not overcrowded. Each `with tabN:` block puts content inside that tab.

## 9.13 Q1: Choropleth map

```python
c = f.groupby(["Country", "ISO3"], as_index=False)["Loss"].sum()
c["Loss ($B)"] = (c["Loss"] / 1000).round(2)
fig = px.choropleth(c, locations="ISO3", color="Loss ($B)", hover_name="Country",
                    color_continuous_scale="Reds")
fig.update_geos(showframe=False, showcoastlines=False, projection_type="natural earth")
```

- `groupby(["Country","ISO3"])["Loss"].sum()` adds up loss for each country. `as_index=False` keeps Country as a normal column.
- We convert to billions and round to 2 decimals.
- `px.choropleth` colours each country on a world map. `locations="ISO3"` says "use the country code column to place it". `color="Loss ($B)"` says "shade by this number". `"Reds"` means darker red = more loss. `hover_name` shows the country name when hovering.
- `update_geos` removes the map frame and coastline outline and uses the "natural earth" projection, which looks like a familiar world map.
- Below the chart a caption tells the user the highest-loss country in the current view. We found it by sorting `c` and taking the first row.

## 9.14 Q2: Time series with two axes

```python
y = f.groupby("Year").agg(Incidents=("Loss", "size"), Loss=("Loss", "sum")).reset_index()
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=y["Year"], y=y["Incidents"], name="Incidents", ...), secondary_y=False)
fig.add_trace(go.Scatter(x=y["Year"], y=y["Loss"]/1000, name="Total loss ($B)", ...), secondary_y=True)
```

- `groupby("Year").agg(...)` builds a small table with two numbers per year: number of incidents (`size` counts rows) and total loss (`sum`).
- Incidents are in the hundreds while total loss is in billions. On one axis, one line would look flat. So we use a **secondary y-axis** on the right for the loss line. That is why we call `make_subplots` with `secondary_y: True`.
- `go.Scatter(... mode="lines+markers")` draws a line with dots. The solid navy line is incidents and the dotted red line is loss.
- `fig.update_xaxes(dtick=1)` shows every year on the x-axis instead of every second year.

## 9.15 Q3 and Q4: Heatmaps

```python
p = f.pivot_table(index="Attack Type", columns="Industry", values="Loss", aggfunc="sum").fillna(0) / 1000
fig = px.imshow(p.round(2), text_auto=".1f", aspect="auto", color_continuous_scale="Reds")
```

- A **pivot table** reshapes data into a grid: rows are attack types, columns are industries, and each cell holds the total loss for that pair. This is the same as a pivot table in Excel.
- `.fillna(0)` puts 0 in any empty cell (can happen after filtering). Dividing by 1,000 converts to billions.
- `px.imshow` paints the grid as a heatmap. `text_auto=".1f"` prints the number in each cell. Darker red = more loss.

```python
p = f.pivot_table(index="Defense", columns="Attack Type", values="Hours", aggfunc="mean")
fig = px.imshow(p.round(1), text_auto=".1f", aspect="auto", color_continuous_scale="Blues_r")
```

- Same idea, but with the **average** resolution hours per defence and attack.
- `"Blues_r"` is the reversed blue scale. In this heatmap **lower hours is better**, so we reverse the colours to make the best (fastest) cells the darkest.

## 9.16 Q5: Scatter plot with a trendline

```python
fig = px.scatter(f, x="Users", y="Loss", color="Industry", opacity=0.55, labels={...})
m, b = np.polyfit(f["Users"], f["Loss"], 1)
xs = np.array([f["Users"].min(), f["Users"].max()])
fig.add_trace(go.Scatter(x=xs, y=m*xs + b, mode="lines", name="Trendline", ...))
r = np.corrcoef(f["Users"], f["Loss"])[0, 1]
```

- `px.scatter` draws one dot per incident: x is users affected, y is loss, colour shows industry. `opacity=0.55` makes dots slightly see-through so overlapping dots are visible.
- `np.polyfit(x, y, 1)` finds the best straight line through the dots. It returns the slope `m` and intercept `b` (the line is `y = m·x + b`).
- We draw that line using only its two end points (`xs`), because two points define a straight line.
- `np.corrcoef` computes the correlation coefficient `r`. The caption prints it, so the viewer sees that it is about 0, meaning no relationship.
- We calculated the trendline with NumPy instead of Plotly's built-in trendline because the built-in one needs an extra library (`statsmodels`). Fewer libraries means fewer things that can break on your teammates' computers.
- `if len(f) > 2` protects against the case where the filters leave too few points to fit a line.

## 9.17 Q6 (bonus): Sunburst

```python
fig = px.sunburst(f, path=["Source", "Vulnerability", "Attack Type"],
                  color="Source", color_discrete_sequence=px.colors.qualitative.Set2)
```

- A sunburst is a **circle with rings**. `path=[...]` lists the layers from the centre outward: Attack Source, then Vulnerability, then Attack Type. Each segment's size is the number of incidents.
- You can click a segment to zoom in. This interactivity is why it is a good fit.

## 9.18 Findings and recommendations tab

- Written as plain text using `st.markdown`, with a note that the numbers are calculated on the **full dataset**. They do not change with filters, because findings are a fixed conclusion from the whole data.

## 9.19 Wrong Visualization tab

```python
cl = df.groupby("Country", as_index=False)["Loss"].sum()
fig = px.bar(s, x="Loss ($B)", y="Country", orientation="h", text="Loss ($B)", ...)   # correct
fig = px.pie(cl, names="Country", values="Loss")                                         # wrong
```

- It uses `df` (the full data), not `f`, so the comparison is always the same regardless of filters.
- `orientation="h"` makes bars horizontal, which keeps country names readable.
- The same numbers are drawn two ways, side by side, to show how the pie hides the ranking.

## 9.20 How we tested the code

- We used Streamlit's built-in test tool (`AppTest`) to run the app without a browser.
- Tests: the app starts with no errors; the KPIs show 3,000 incidents and 151.5 billion dollars; after setting the year filter to 2020 to 2024 the KPIs showed 1,546 incidents and 78.9 billion (matching our finding); with only UK selected it showed 163 incidents and 8.4 billion; with no country selected it showed the warning message.
- **Limit:** we could not open a real browser in our environment. So you should run it on your laptop and look at the charts yourself.

## 9.21 How to run it

```
pip install -r requirements.txt
streamlit run app.py
```

Keep the CSV in the same folder as `app.py`.

---

# Part 10. How we made the Word document

1. **Content first.** We wrote all sections from the task sheet: title and objective, dataset description, Discovery Summary, questions, dashboard, findings, recommendations, Wrong Visualization, AI critique, data story, conclusion, checklist. Every number comes from the real data.
2. **Charts for the Wrong Visualization section** were made with Python's `matplotlib` library in grey shades, so the document stays black and white.
3. **The Word file was generated by a script** using a JavaScript library called `docx`. We used it so the formatting is perfectly consistent.
4. **Formatting rules you gave:** Century Schoolbook 12 pt for the body text and Arial in the tables; bold numbered headings; centred college name and title; left-aligned body; clean tables; uniform margins; black and white. We chose A4 paper, as used in India.
5. **We checked the result** by converting it to PDF and viewing each page. We found and fixed two issues: headings showed blue (we forced black) and a blank page appeared (we changed the page break method).
6. **Placeholders left on purpose:** names of students, the dashboard screenshots, and the AI critique. These must be your team's real work.

---

# Part 11. Questions a teacher may ask (with simple answers)

**Q. Why did you choose this dataset?**
It has time, country, money and category columns, which lets us use maps, time series and heatmaps. It is clean and small enough to build a fast dashboard in the time given.

**Q. Why not a network intrusion dataset like NSL-KDD?**
Those are large technical datasets meant for training detection models. They have no country, industry or money columns, so a business-style story and map would be hard.

**Q. Is the data real?**
It is a public Kaggle dataset compiled from reports and archives. Its numbers are spread very evenly and have no outliers, so it may be partly simulated. We state this limit openly.

**Q. Did you find missing values or duplicates?**
No. There are 3,000 complete rows and no exact duplicates.

**Q. How did you check for outliers?**
With the IQR method. No value in loss, users or resolution time went outside the limits.

**Q. Why Streamlit and not Power BI?**
The task asks for Streamlit or Dash with Plotly. Streamlit is pure Python, simple, and we must submit source code.

**Q. What happens when a user changes a filter?**
Streamlit re-runs the script from top to bottom. The filtered table `f` changes, so every KPI and chart is rebuilt from it.

**Q. What does `@st.cache_data` do?**
It remembers the loaded data so Streamlit does not reread the CSV on every click.

**Q. What is a pivot table and why did you use it?**
It reshapes data into a grid of rows by columns with a summary number in each cell. Heatmaps need that grid shape.

**Q. Why a choropleth for Q1?**
Because the data is geographical and a map shows location and amount together.

**Q. Why two axes in the time series?**
Incidents are in hundreds and total loss is in billions. On one axis one of the lines would look flat.

**Q. What does a correlation of 0.002 mean?**
Practically no relationship. It means knowing the number of affected users tells you nothing about the financial loss.

**Q. Why is the pie chart a bad choice?**
Ten slices of nearly equal size cannot be compared by eye, and the ranking is hidden.

**Q. Why only five charts on the dashboard?**
The task says 3 to 5. We put the extra sunburst in a labelled Bonus tab.

**Q. What is your main recommendation?**
Prioritise phishing protection in banking, match defences to attacks, and judge incidents by several indicators together.

**Q. What would you do with more time?**
Add a risk score, try a larger or real dataset such as the Maryland Cyber Events Database, add a forecasting chart, and test with real users.

**Q. How did you use AI?**
For guidance, planning and drafting. Every team member must be able to explain all work, and the AI critique section is based on our own request to an AI tool and our decision to accept, partly accept or reject its advice.

---

# Part 12. Glossary (simple meanings)

| Term | Meaning |
|---|---|
| Dataset | A table of data. Rows are records, columns are attributes. |
| Row / record | One item, here one cyber incident. |
| Column / attribute | One property of every record, such as Country. |
| Numerical variable | A column of numbers you can add or average. |
| Categorical variable | A column of labels or groups. |
| Missing value | An empty cell. |
| Duplicate | A row that is an exact copy of another. |
| Outlier | A value unusually far from the rest. |
| IQR | The middle spread of data, used to detect outliers. |
| Skewness | Whether the data is lopsided. Near 0 means balanced. |
| Correlation (r) | How strongly two number columns move together, from −1 to +1. |
| DataFrame | The table object used by pandas. |
| Group by | Split rows into groups and calculate for each group. |
| Pivot table | A grid summary of two categories. |
| KPI | A headline number for quick performance checking. |
| Filter | A control that narrows the data shown. |
| Choropleth | A map where regions are shaded by a value. |
| Heatmap | A grid coloured by value. |
| Scatter plot | Dots showing two number columns against each other. |
| Sunburst | A ring chart showing hierarchy. |
| Time series | Data tracked over time. |
| Trendline | A straight line showing the general direction of the dots. |
| Streamlit | A Python library that makes web dashboards. |
| Plotly | A library for interactive charts. |
| Cache | Remembered results to save time. |
| ISO-3 code | A standard 3-letter country code, such as IND for India. |

---

# Part 13. What is still pending for you

1. **Run the dashboard** on your laptop and take **three screenshots** for the Word document.
2. **AI as a Critic:** pick one chart, ask an AI tool to critique it, then record the recommendation, your decision (accepted, partly accepted, rejected) and your reason in Section 9 of the Word document.
3. **Add the four student names** to the cover page.
4. **Prepare the 2-3 slide PPT:** group details, dashboard screenshot and questions analysed.
5. **Practise the 2-minute Data Story** (what we found, why it matters, what action to take).
6. **Make the final .zip** with the dataset, source code, screenshots, document and presentation.
7. **Each member** should read this guide and be able to explain any part. The task says every team member must understand the whole project.
8. **Remember the deadlines:** submit by 14-10-2026 and present on 15-10-2026 (3 to 5 PM). The MCQ quiz is also on that day.
