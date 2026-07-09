"""
=========================================================
AI EXECUTIVE REPORT CENTER
AI Marketing Campaign Intelligence Platform
=========================================================
"""

import os
import sys
import io
import pandas as pd
import streamlit as st
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Executive Reports",
    page_icon="📑",
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

from ai_engine.executive_summary import ExecutiveSummary
from ai_engine.business_advisor import AIBusinessAdvisor
from ai_engine.campaign_health import CampaignHealthScore
from ai_engine.risk_detector import CampaignRiskDetector

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""

<style>

.block-container{

    padding-top:1.5rem;
    padding-bottom:2rem;

}

/* KPI Cards */

div[data-testid="stMetric"]{

    background:#111827;
    border-radius:18px;
    padding:18px;
    border-left:6px solid #2563EB;
    box-shadow:0px 6px 18px rgba(0,0,0,.30);

}

/* Summary Card */

.summary-card{

    background:#111827;
    padding:22px;
    border-radius:18px;
    border-left:6px solid #10B981;
    margin-bottom:20px;
    box-shadow:0px 6px 18px rgba(0,0,0,.25);

}

/* Download Buttons */

.stDownloadButton>button{

    width:100%;
    height:48px;
    border-radius:10px;
    font-weight:600;

}

/* Tables */

[data-testid="stDataFrame"]{

    border-radius:14px;

}

</style>

""", unsafe_allow_html=True)

# =========================================================
# MAIN
# =========================================================

def show_reports():

    st.title("📑 AI Executive Reporting Center")

    st.caption(
        "Generate executive reports, KPI summaries, campaign health reports, business recommendations and AI-powered executive insights."
    )

    st.markdown("---")

    # =====================================================
    # LOAD AI MODULES
    # =====================================================

    summary = ExecutiveSummary()

    advisor = AIBusinessAdvisor()

    health = CampaignHealthScore()

    risk = CampaignRiskDetector()

    # =====================================================
    # KPI DATA
    # =====================================================

    kpi = summary.generate_kpis()

    total_campaigns = kpi["Total Campaigns"]
    total_revenue = kpi["Total Revenue"]
    avg_roi = kpi["Average ROI"]
    success_rate = kpi["Campaign Success Rate"]

    # =====================================================
    # KPI CARDS
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📢 Campaigns",
        total_campaigns
    )

    c2.metric(
        "💰 Revenue",
        f"${total_revenue:,.0f}"
    )

    c3.metric(
        "📈 Average ROI",
        f"{avg_roi:.2f}%"
    )

    c4.metric(
        "🎯 Success Rate",
        f"{success_rate:.2f}%"
    )

    st.markdown("---")

    # =====================================================
    # AI EXECUTIVE SUMMARY
    # =====================================================

    st.markdown(f"""

<div class="summary-card">

<h2>🤖 AI Executive Summary</h2>

<b>Total Campaigns :</b> {total_campaigns}<br><br>

<b>Total Revenue :</b> ${total_revenue:,.0f}<br><br>

<b>Average ROI :</b> {avg_roi:.2f}%<br><br>

<b>Campaign Success Rate :</b> {success_rate:.2f}%<br><br>

<h4>🚀 AI Recommendation</h4>

<ul>

<li>Increase investment in high-performing campaigns.</li>

<li>Reduce spend on campaigns with poor ROI.</li>

<li>Monitor campaign health weekly.</li>

<li>Focus more on high-converting marketing channels.</li>

<li>Optimize risky campaigns before scaling.</li>

</ul>

</div>

""", unsafe_allow_html=True)

    st.markdown("---")

    # =====================================================
    # KPI TABLE
    # =====================================================

    st.subheader("📊 Executive KPI Summary")

    kpi_df = pd.DataFrame(

        list(kpi.items()),

        columns=[
            "Metric",
            "Value"
        ]

    )

    st.dataframe(

        kpi_df,

        use_container_width=True,

        hide_index=True

    )

    st.markdown("---")

    # =====================================================
    # KPI VISUALIZATION
    # =====================================================

    fig = px.bar(

        kpi_df,

        x="Metric",

        y="Value",

        color="Value",

        color_continuous_scale="Blues",

        text="Value",

        title="Executive KPI Overview"

    )

    fig.update_traces(

        textposition="outside"

    )

    fig.update_layout(

        height=430,

        xaxis_title="",

        yaxis_title="",

        title_x=0.33

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    # =====================================================
    # BUSINESS RECOMMENDATIONS
    # =====================================================

    st.subheader("🤖 AI Business Recommendations")

    recommendations = advisor.recommendations()

    for rec in recommendations:

        st.success(rec)

    st.markdown("---")

    # =====================================================
    # HEALTH ANALYSIS
    # =====================================================

    st.subheader("❤️ Top Healthy Campaigns")

    health_df = (

        health.calculate_health()

        .sort_values(
            "Health_Score",
            ascending=False
        )

        .head(15)

    )

    fig = px.bar(

        health_df,

        x="Campaign_Name",

        y="Health_Score",

        color="Health_Score",

        color_continuous_scale="Greens",

        text_auto=".1f",

        title="Campaign Health Score"

    )

    fig.update_layout(

        height=430,

        xaxis_title="",

        yaxis_title="Health Score",

        title_x=0.34

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(

        health_df,

        use_container_width=True,

        hide_index=True

    )

    st.markdown("---")

    # =====================================================
    # RISK ANALYSIS
    # =====================================================

    st.subheader("⚠ High Risk Campaigns")

    risk_df = (

        risk.detect()

        .sort_values(
            "Risk_Score",
            ascending=False
        )

        .head(15)

    )

    fig = px.bar(

        risk_df,

        x="Campaign_Name",

        y="Risk_Score",

        color="Risk_Score",

        color_continuous_scale="Reds",

        text_auto=".1f",

        title="Campaign Risk Score"

    )

    fig.update_layout(

        height=430,

        xaxis_title="",

        yaxis_title="Risk Score",

        title_x=0.35

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(

        risk_df,

        use_container_width=True,

        hide_index=True

    )

    st.markdown("---")

    # =====================================================
    # EXECUTIVE CONCLUSION
    # =====================================================

    st.markdown("""

<div class="summary-card">

<h2>📌 Executive AI Conclusion</h2>

✅ Campaign performance analyzed successfully.<br><br>

✅ High-performing campaigns identified.<br><br>

✅ High-risk campaigns detected for optimization.<br><br>

✅ AI recommendations generated for better ROI.<br><br>

✅ Campaign Health monitoring completed.

</div>

""", unsafe_allow_html=True)

    st.markdown("---")

    # =====================================================
    # EXPORT REPORTS
    # =====================================================

    output = io.BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        kpi_df.to_excel(
            writer,
            sheet_name="Executive KPI",
            index=False
        )

        health_df.to_excel(
            writer,
            sheet_name="Campaign Health",
            index=False
        )

        risk_df.to_excel(
            writer,
            sheet_name="Risk Report",
            index=False
        )

    output.seek(0)

    left, right = st.columns(2)

    with left:

        st.download_button(

            "📥 Download Executive Excel Report",

            data=output,

            file_name="AI_Executive_Report.xlsx",

            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

            use_container_width=True

        )

    with right:

        csv = risk_df.to_csv(index=False).encode("utf-8")

        st.download_button(

            "📄 Download Risk Report (CSV)",

            data=csv,

            file_name="Risk_Report.csv",

            mime="text/csv",

            use_container_width=True

        )

    st.markdown("---")

    st.success("✅ AI Executive Report Generated Successfully")


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    show_reports()