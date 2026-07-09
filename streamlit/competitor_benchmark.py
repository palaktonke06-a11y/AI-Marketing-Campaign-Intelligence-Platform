"""
=========================================================
AI COMPETITOR BENCHMARK CENTER
AI Marketing Campaign Intelligence Platform
=========================================================
"""

import os
import sys
import streamlit as st
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(

    page_title="AI Competitor Benchmark",

    page_icon="🏆",

    layout="wide"

)

# =========================================================
# PATH
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

from ai_engine.competitor_benchmark import CompetitorBenchmark

# =========================================================
# PREMIUM CSS
# =========================================================

st.markdown("""

<style>

/* Main */

.block-container{

padding-top:1.5rem;

padding-bottom:2rem;

}

/* KPI */

div[data-testid="stMetric"]{

background:#111827;

padding:20px;

border-radius:18px;

border-left:6px solid #2563EB;

box-shadow:0px 6px 18px rgba(0,0,0,.25);

}

/* Overview */

.benchmark-box{

background:#111827;

padding:22px;

border-radius:18px;

border-left:6px solid #2563EB;

margin-bottom:20px;

box-shadow:0px 6px 18px rgba(0,0,0,.25);

}

/* Cards */

.summary-card{
background:#111827;
border:1px solid #334155;
border-radius:18px;
padding:20px;
height:220px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
text-align:center;
box-shadow:0 6px 18px rgba(0,0,0,.25);
margin-bottom:10px;
}

.summary-card h1{
font-size:48px;
margin:10px 0;
color:white;
}

.summary-card h2{
font-size:40px;
margin:10px 0;
color:white;
}

.summary-card h3{
color:#60A5FA;
margin-bottom:10px;
}

.summary-card p{
color:#CBD5E1;
font-size:15px;
}

.summary-card:hover{

transform:translateY(-5px);

box-shadow:0px 10px 24px rgba(37,99,235,.30);

}


</style>

""", unsafe_allow_html=True)

def show_benchmark():

    st.title("🏆 AI Competitor Benchmark Center")

    st.caption(
        "Compare campaign performance against industry benchmarks using Artificial Intelligence."
    )

    st.markdown("---")

    benchmark = CompetitorBenchmark()

    report = benchmark.compare()

    above = len(
        report[
            report["Status"] == "Above Market"
        ]
    )

    below = len(
        report[
            report["Status"] == "Below Market"
        ]
    )

    total = len(report)

    # =====================================================
    # AI OVERVIEW
    # =====================================================

    st.markdown("""

<div class="benchmark-box">

<h3>🚀 AI Competitor Benchmark Overview</h3>

This module compares your marketing campaigns
against industry benchmarks.

✔ Industry Performance Comparison

✔ Benchmark Score Analysis

✔ AI Competitive Position

✔ Growth Opportunities

✔ Executive Benchmark Report

</div>

""", unsafe_allow_html=True)

    # =====================================================
    # KPI CARDS
    # =====================================================

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "📢 Total Campaigns",
            total
        )

    with c2:

        st.metric(
            "🏆 Above Market",
            above
        )

    with c3:

        st.metric(
            "📉 Below Market",
            below
        )

    st.markdown("---")

    # =====================================================
    # AI EXECUTIVE SUMMARY
    # =====================================================

    benchmark_rate = round((above / total) * 100, 2)

    st.info(f"""

### 🤖 AI Benchmark Summary

🏆 Above Market Campaigns : **{above}**

📉 Below Market Campaigns : **{below}**

📊 Campaigns Analysed : **{total}**

🎯 Competitive Score : **{benchmark_rate}%**

### AI Recommendation

Increase investment in campaigns already performing
above market while improving campaigns that are
currently below benchmark.

""")

    st.markdown("---")

    # =====================================================
    # QUICK INSIGHTS
    # =====================================================

    st.markdown("""

    <style>

    .summary-card{

        background:#111827;
        border:1px solid #334155;
        border-radius:18px;
        padding:25px;
        text-align:center;
        min-height:220px;
        box-shadow:0 6px 18px rgba(0,0,0,.25);

    }

    .summary-card h1,
    .summary-card h2{
        color:white;
    }

    .summary-card h3{
        color:#60A5FA;
    }

    .summary-card p{
        color:#CBD5E1;
        font-size:16px;
    }

    </style>

    """, unsafe_allow_html=True)


    decision = (
        "Excellent"
        if benchmark_rate >= 70
        else "Moderate"
        if benchmark_rate >= 50
        else "Needs Improvement"
    )


    s1, s2, s3 = st.columns(3, gap="large")


    with s1:

        st.markdown(f"""
        <div class="summary-card">
            <h3>🏆 Market Leaders</h3>
            <h1>{above}</h1>
            <p>Campaigns performing above competitors.</p>
        </div>
        """, unsafe_allow_html=True)


    with s2:

        st.markdown(f"""
        <div class="summary-card">
            <h3>📉 Need Improvement</h3>
            <h1>{below}</h1>
            <p>Campaigns below market average.</p>
        </div>
        """, unsafe_allow_html=True)


    with s3:

        st.markdown(f"""
        <div class="summary-card">
            <h3>🤖 AI Decision</h3>
            <h2>{decision}</h2>
            <p>Competitive Performance</p>
        </div>
        """, unsafe_allow_html=True)


    st.markdown("---")

    # =====================================================
    # MARKET STATUS CHART
    # =====================================================

    left, right = st.columns(2)

    with left:

        status = (
            report["Status"]
            .value_counts()
            .reset_index()
        )

        status.columns = [
            "Status",
            "Count"
        ]

        fig = px.pie(

            status,

            names="Status",

            values="Count",

            hole=0.60,

            title="Market Position Distribution",

            color="Status",

            color_discrete_map={

                "Above Market": "#22C55E",

                "Below Market": "#EF4444"

            }

        )

        fig.update_layout(height=430)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        # Find score column automatically
        score_col = None

        for col in report.columns:
            if "benchmark" in col.lower() and "score" in col.lower():
                score_col = col
                break

        if score_col:

            fig = px.bar(
                report.sort_values(
                    "Benchmark Score",
                    ascending=False
                ),
                x="Metric",
                y="Benchmark Score",
                color="Status",
                text="Benchmark Score",
                title="Benchmark Score by Metric",
                color_discrete_map={
                    "Above Market": "#22C55E",
                    "Below Market": "#EF4444"
                }
            )

            fig.update_traces(
                textposition="outside"
            )

            fig.update_layout(
                height=450,
                xaxis_title="Performance Metric",
                yaxis_title="Benchmark Score",
                title_x=0.25
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:
            st.warning(
                f"Benchmark score column not found.\nAvailable columns:\n{list(report.columns)}"
            )

    st.markdown("---")

    # =====================================================
    # AI COMPETITIVE INSIGHTS
    # =====================================================

    st.subheader("🤖 AI Competitive Insights")

    if benchmark_rate >= 75:

        st.success("""

### Market Position : Excellent 🟢

✔ Majority of campaigns are outperforming competitors.

✔ Continue increasing investment in top campaigns.

✔ Current strategy is highly competitive.

""")

    elif benchmark_rate >= 50:

        st.warning("""

### Market Position : Average 🟡

✔ Several campaigns are above market.

✔ Optimize weaker campaigns.

✔ Improve CTR and Conversion Rate.

""")

    else:

        st.error("""

### Market Position : Weak 🔴

✔ Most campaigns are below market benchmark.

✔ Review targeting strategy.

✔ Optimize budget allocation.

✔ Improve creatives and landing pages.

""")

    st.markdown("---")

    # =====================================================
    # BENCHMARK TABLE
    # =====================================================

    st.subheader("📋 Competitor Benchmark Report")

# Automatically detect benchmark score column
    score_col = None

    for col in report.columns:
        if "benchmark" in col.lower() and "score" in col.lower():
            score_col = col
            break

    if score_col:

        report_display = report.sort_values(
            score_col,
            ascending=False
        )

    else:

        report_display = report

        st.warning(
            "Benchmark Score column not found. Showing unsorted report."
        )

    st.dataframe(

    report.sort_values(

        "Benchmark Score",

        ascending=False

    ),

    use_container_width=True,

    hide_index=True

)

    st.markdown("---")

    # =====================================================
    # DOWNLOAD REPORT
    # =====================================================

    csv = report.to_csv(index=False).encode("utf-8")

    st.download_button(

        "📥 Download Benchmark Report",

        data=csv,

        file_name="Competitor_Benchmark_Report.csv",

        mime="text/csv",

        use_container_width=True

    )

    st.markdown("---")

    st.success("✅ AI Competitor Benchmark Analysis Completed Successfully")


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    show_benchmark()