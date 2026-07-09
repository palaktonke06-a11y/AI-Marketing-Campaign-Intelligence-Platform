"""
=========================================================
AI MARKETING CAMPAIGN INTELLIGENCE PLATFORM
Main Streamlit Application
=========================================================
"""

import os
import sys
import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Marketing Campaign Intelligence Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PATHS
# =========================================================

ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

PYTHON_FOLDER = os.path.join(
    ROOT,
    "python"
)

if PYTHON_FOLDER not in sys.path:
    sys.path.append(PYTHON_FOLDER)

# =========================================================
# IMPORT PAGES
# =========================================================

from dashboard import show_dashboard
from prediction import show_prediction
from ai_insights import show_ai_insights
from optimization import show_optimization
from competitor_benchmark import show_benchmark
from reports import show_reports

# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown("""

<style>

/* ---------------- Main ---------------- */

.block-container{

padding-top:1.3rem;
padding-bottom:2rem;

}

/* ---------------- Sidebar ---------------- */

section[data-testid="stSidebar"]{

background:#0F172A;

}

section[data-testid="stSidebar"] *{

color:white;

}

/* ---------------- Hero ---------------- */

.hero{

background:linear-gradient(135deg,#2563EB,#1D4ED8,#06B6D4);

padding:40px;

border-radius:22px;

color:white;

margin-bottom:28px;

box-shadow:0 10px 25px rgba(0,0,0,.25);

}

/* ---------------- Feature Cards ---------------- */

.feature{
background:#1E293B;
padding:24px;
border-radius:18px;
text-align:center;
min-height:250px;
display:flex;
flex-direction:column;
justify-content:space-between;
align-items:center;
overflow:hidden;
transition:.3s;
box-shadow:0px 5px 18px rgba(0,0,0,.25);
}

.feature:hover{

transform:translateY(-8px);

box-shadow:0 12px 28px rgba(37,99,235,.35);

}

.feature h3{
font-size:28px;
line-height:1.3;
margin-bottom:12px;
color:#60A5FA;
}

.feature h2{
font-size:20px;
line-height:1.4;
margin-bottom:10px;
color:white;
}

.feature p{
font-size:15px;
line-height:1.6;
color:#CBD5E1;
}

/* ---------------- Metrics ---------------- */

div[data-testid="stMetric"]{

background:#111827;

padding:18px;

border-radius:16px;

border-left:5px solid #2563EB;

box-shadow:0 5px 16px rgba(0,0,0,.25);

}

/* ---------------- Footer ---------------- */

.footer{

text-align:center;

padding:25px;

color:#94A3B8;

}

</style>

""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🤖 AI Marketing Platform")

st.sidebar.markdown("---")

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Dashboard",

        "🎯 AI Prediction",

        "📈 AI Insights",

        "💰 Optimization",

        "🏆 Benchmark",

        "📑 Reports"

    ]

)

st.sidebar.markdown("---")

st.sidebar.success("🟢 Platform Online")

st.sidebar.metric("ML Models", "5")

st.sidebar.metric("AI Engines", "8")

st.sidebar.metric("Interactive Pages", "6")

st.sidebar.metric("Deployment", "Ready 🚀")

st.sidebar.markdown("---")

st.sidebar.info("""

### Platform

✔ Predict Campaign Success

✔ AI Insights

✔ Optimization

✔ Benchmarking

✔ Executive Reports

""")

st.sidebar.caption("Version 2.0")

# =========================================================
# HOME PAGE
# =========================================================

if page == "🏠 Dashboard":

    st.markdown("""

<div class="hero">

<h1>🚀 AI Marketing Campaign Intelligence Platform</h1>

<p style="font-size:18px;line-height:1.8;">

An End-to-End Artificial Intelligence solution for
Marketing Analytics, Campaign Prediction,
Business Insights, Budget Optimization,
Competitor Benchmarking and Executive Reporting.

</p>

</div>

""", unsafe_allow_html=True)

    # =====================================================
    # FEATURE CARDS
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown("""

<div class="feature">

<h3>🎯 AI Prediction</h3>

<h2>Machine Learning</h2>

<p>

Predict campaign success before launch using trained
Random Forest models.

</p>

</div>

""", unsafe_allow_html=True)

    with c2:

        st.markdown("""

<div class="feature">

<h3>📈 AI Insights</h3>

<h2>Business Intelligence</h2>

<p>

Generate executive insights, campaign health,
risk analysis and smart alerts.

</p>

</div>

""", unsafe_allow_html=True)

    with c3:

        st.markdown("""

<div class="feature">

<h3>💰 Optimization</h3>

<h2>AI Optimization</h2>

<p>

Optimize marketing budgets,
maximize ROI and simulate strategies.

</p>

</div>

""", unsafe_allow_html=True)

    with c4:

        st.markdown("""

<div class="feature">

<h3>📑 Executive Reports</h3>

<h2>Reporting Suite</h2>

<p>

Generate executive dashboards,
Excel reports and AI recommendations.

</p>

</div>

""", unsafe_allow_html=True)

    st.markdown("---")

    # =====================================================
    # PLATFORM OVERVIEW
    # =====================================================

    st.subheader("📊 Platform Overview")

    m1, m2, m3, m4 = st.columns(4)

    with m1:

        st.metric(
            "Modules",
            "6"
        )

    with m2:

        st.metric(
            "AI Engines",
            "8"
        )

    with m3:

        st.metric(
            "ML Models",
            "5"
        )

    with m4:

        st.metric(
            "Project Status",
            "Production Ready 🚀"
        )

    st.markdown("---")

    # =====================================================
    # PLATFORM CAPABILITIES
    # =====================================================

    st.subheader("✨ Platform Capabilities")

    l1, l2 = st.columns(2)

    with l1:

        st.success("""

### 🤖 Artificial Intelligence

✔ Campaign Success Prediction

✔ Business Advisor

✔ Budget Optimizer

✔ Performance Forecast

✔ Smart Alerts

✔ Campaign Health Score

""")

    with l2:

        st.info("""

### 📊 Analytics

✔ Executive Dashboard

✔ Competitor Benchmark

✔ AI Insights

✔ Risk Detection

✔ Executive Reports

✔ Interactive Visualizations

""")

    st.markdown("---")

# =========================================================
# PAGE ROUTING
# =========================================================

if page == "🏠 Dashboard":

    show_dashboard()

elif page == "🎯 AI Prediction":

    show_prediction()

elif page == "📈 AI Insights":

    show_ai_insights()

elif page == "💰 Optimization":

    show_optimization()

elif page == "🏆 Benchmark":

    show_benchmark()

elif page == "📑 Reports":

    show_reports()

    # =====================================================
    # PROJECT INFORMATION
    # =====================================================

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""

### 🚀 Platform

- AI Powered Analytics

- Machine Learning

- Business Intelligence

- Executive Reporting

""")

    with c2:

        st.markdown("""

### 🛠 Tech Stack

- Python

- Streamlit

- Scikit-Learn

- Plotly

- Pandas

- SQL

- Power BI

""")

    with c3:

        st.markdown("""

### 📦 Project

Version : **2.0**

Status : 🟢 Production Ready

Deployment : Ready

""")

    st.markdown("---")

    st.markdown("""

<div class="footer">

<h3>🤖 AI Marketing Campaign Intelligence Platform</h3>

<p>

End-to-End Artificial Intelligence Solution for

Marketing Analytics, Prediction, Optimization,

Business Intelligence and Executive Reporting

</p>

<p>

<b>Python</b> •

<b>Machine Learning</b> •

<b>Streamlit</b> •

<b>SQL</b> •

<b>Power BI</b>

</p>

<p style="color:#60A5FA;">

© 2026 All Rights Reserved

</p>

</div>

""", unsafe_allow_html=True)