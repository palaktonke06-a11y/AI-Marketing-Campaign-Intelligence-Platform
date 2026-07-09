"""
=========================================================
EXECUTIVE DASHBOARD
AI Marketing Campaign Intelligence Platform
=========================================================
"""

import os
import pandas as pd
import streamlit as st
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
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

DATA_PATH = os.path.join(
    ROOT,
    "python",
    "data_generation",
    "data",
    "processed",
    "campaign_dashboard_dataset.csv"
)

df = pd.read_csv(DATA_PATH)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.block-container{
    padding-top:1.8rem;
    padding-bottom:1rem;
}

div[data-testid="stMetric"]{
    background:#111827;
    border:1px solid #374151;
    border-radius:18px;
    padding:18px;
    box-shadow:0px 6px 16px rgba(0,0,0,.25);
}

div[data-testid="stMetricLabel"]{
    font-size:17px;
    font-weight:600;
}

div[data-testid="stMetricValue"]{
    font-size:32px;
    font-weight:bold;
}

.hero{

background:linear-gradient(90deg,#2563EB,#0EA5E9);

padding:28px;

border-radius:20px;

color:white;

margin-bottom:25px;

box-shadow:0px 8px 22px rgba(0,0,0,.25);

}

.insight-card{

background:#111827;

padding:20px;

border-radius:16px;

border-left:6px solid #2563EB;

box-shadow:0px 6px 16px rgba(0,0,0,.25);

}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HELPER FUNCTION
# =========================================================

def format_money(value):

    if value >= 1_000_000_000:
        return f"${value/1_000_000_000:.2f}B"

    elif value >= 1_000_000:
        return f"${value/1_000_000:.2f}M"

    elif value >= 1_000:
        return f"${value/1_000:.2f}K"

    return f"${value:,.0f}"

# =========================================================
# MAIN DASHBOARD
# =========================================================

def show_dashboard():

    filtered_df = df.copy()

    # =====================================================
    # HERO
    # =====================================================

    st.markdown("""

<div class="hero">

<h1>📊 Executive Marketing Dashboard</h1>

<p style="font-size:18px;">

Real-time AI Powered Marketing Analytics Dashboard with
Business Intelligence, Campaign Performance, Revenue Insights,
ROI Analysis and Executive KPIs.

</p>

</div>

""", unsafe_allow_html=True)

    # =====================================================
    # FILTERS
    # =====================================================

    st.subheader("🎛 Dashboard Filters")

    f1, f2, f3 = st.columns(3)

    with f1:

        channel = st.selectbox(
            "Marketing Channel",
            ["All"] + sorted(filtered_df["Marketing_Channel"].unique())
        )

    with f2:

        region = st.selectbox(
            "Region",
            ["All"] + sorted(filtered_df["Region_Target"].unique())
        )

    with f3:

        campaign = st.selectbox(
            "Campaign Type",
            ["All"] + sorted(filtered_df["Campaign_Type"].unique())
        )

    if channel != "All":

        filtered_df = filtered_df[
            filtered_df["Marketing_Channel"] == channel
        ]

    if region != "All":

        filtered_df = filtered_df[
            filtered_df["Region_Target"] == region
        ]

    if campaign != "All":

        filtered_df = filtered_df[
            filtered_df["Campaign_Type"] == campaign
        ]

    st.markdown("---")

    # =====================================================
    # KPI VALUES
    # =====================================================

    total_campaigns = len(filtered_df)

    total_budget = filtered_df["Budget"].sum()

    total_spend = filtered_df["Spend"].sum()

    total_revenue = filtered_df["Revenue"].sum()

    total_profit = total_revenue - total_spend

    avg_roi = filtered_df["ROI"].mean()

    avg_roas = filtered_df["ROAS"].mean()

    success_rate = round(
        filtered_df["Campaign_Success"].mean()*100,
        2
    )

    best_channel = (
        filtered_df.groupby("Marketing_Channel")["Revenue"]
        .sum()
        .idxmax()
    )

    best_region = (
        filtered_df.groupby("Region_Target")["Revenue"]
        .sum()
        .idxmax()
    )

    best_campaign = (
        filtered_df.groupby("Campaign_Type")["ROI"]
        .mean()
        .idxmax()
    )

    # =====================================================
    # KPI CARDS
    # =====================================================

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(
            "📢 Campaigns",
            f"{total_campaigns:,}"
        )

    with kpi2:
        st.metric(
            "💰 Budget",
            format_money(total_budget)
        )

    with kpi3:
        st.metric(
            "💸 Spend",
            format_money(total_spend)
        )

    with kpi4:
        st.metric(
            "📈 Revenue",
            format_money(total_revenue)
        )

    st.write("")

    kpi5, kpi6, kpi7, kpi8 = st.columns(4)

    with kpi5:
        st.metric(
            "💹 Profit",
            format_money(total_profit)
        )

    with kpi6:
        st.metric(
            "📊 Average ROI",
            f"{avg_roi:.2f}%"
        )

    with kpi7:
        st.metric(
            "🚀 Average ROAS",
            f"{avg_roas:.2f}"
        )

    with kpi8:
        st.metric(
            "🎯 Success Rate",
            f"{success_rate:.2f}%"
        )

    st.markdown("---")

    # =====================================================
    # AI EXECUTIVE SUMMARY
    # =====================================================

    st.markdown(f"""
    <div class="insight-card">

    <h2>🤖 AI Executive Summary</h2>

    <br>

    <b>🏆 Best Marketing Channel :</b> {best_channel}<br><br>

    <b>🌍 Best Performing Region :</b> {best_region}<br><br>

    <b>🚀 Best Campaign Type :</b> {best_campaign}<br><br>

    <b>📈 Campaign Success Rate :</b> {success_rate}%<br><br>

    <b>💡 AI Recommendation :</b>

    Continue investing in <b>{best_channel}</b>,
    increase campaign reach in
    <b>{best_region}</b>,
    and prioritize
    <b>{best_campaign}</b>
    campaigns for maximum ROI.

    </div>

    """, unsafe_allow_html=True)

    st.markdown("---")

    # =====================================================
    # ROW 1
    # =====================================================

    left_chart, right_chart = st.columns(2)

    with left_chart:

        revenue_channel = (

            filtered_df

            .groupby("Marketing_Channel")["Revenue"]

            .sum()

            .reset_index()

        )

        fig = px.bar(

            revenue_channel,

            x="Marketing_Channel",

            y="Revenue",

            color="Revenue",

            text_auto=".2s",

            color_continuous_scale="Blues",

            title="Revenue by Marketing Channel"

        )

        fig.update_layout(

            height=430,

            xaxis_title="",

            yaxis_title="Revenue",

            coloraxis_showscale=False

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    with right_chart:

        roi_channel = (

            filtered_df

            .groupby("Marketing_Channel")["ROI"]

            .mean()

            .reset_index()

        )

        fig = px.bar(

            roi_channel,

            x="Marketing_Channel",

            y="ROI",

            color="ROI",

            text_auto=".2f",

            color_continuous_scale="Greens",

            title="Average ROI by Marketing Channel"

        )

        fig.update_layout(

            height=430,

            xaxis_title="",

            yaxis_title="ROI (%)",

            coloraxis_showscale=False

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.markdown("---")

    # =====================================================
    # ROW 2
    # =====================================================

    left_chart, right_chart = st.columns(2)

    # -----------------------------------------------------
    # Campaign Distribution
    # -----------------------------------------------------

    with left_chart:

        campaign_distribution = (

            filtered_df

            .groupby("Campaign_Type")

            .size()

            .reset_index(name="Campaigns")

        )

        fig = px.pie(

            campaign_distribution,

            names="Campaign_Type",

            values="Campaigns",

            hole=0.55,

            title="Campaign Type Distribution"

        )

        fig.update_traces(

            textposition="inside",

            textinfo="percent+label"

        )

        fig.update_layout(

            height=430,

            legend_title="Campaign Type"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # -----------------------------------------------------
    # Revenue by Region
    # -----------------------------------------------------

    with right_chart:

        region_revenue = (

            filtered_df

            .groupby("Region_Target")["Revenue"]

            .sum()

            .reset_index()

        )

        fig = px.bar(

            region_revenue,

            x="Region_Target",

            y="Revenue",

            color="Revenue",

            text_auto=".2s",

            color_continuous_scale="Purples",

            title="Revenue by Region"

        )

        fig.update_layout(

            height=430,

            xaxis_title="",

            yaxis_title="Revenue",

            coloraxis_showscale=False

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.markdown("---")

    # =====================================================
    # MONTHLY REVENUE TREND
    # =====================================================

    if "Start_Date" in filtered_df.columns:

        trend_df = filtered_df.copy()

        trend_df["Start_Date"] = pd.to_datetime(

            trend_df["Start_Date"]

        )

        monthly = (

            trend_df

            .groupby(

                trend_df["Start_Date"]

                .dt.to_period("M")

                .astype(str)

            )["Revenue"]

            .sum()

            .reset_index()

        )

        fig = px.line(

            monthly,

            x="Start_Date",

            y="Revenue",

            markers=True,

            title="Monthly Revenue Trend"

        )

        fig.update_traces(

            line_width=4,

            marker_size=8

        )

        fig.update_layout(

            height=460,

            xaxis_title="Month",

            yaxis_title="Revenue"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    else:

        st.warning(

            "Start_Date column not found. Monthly trend cannot be generated."

        )

    st.markdown("---")

    # =====================================================
    # TOP PERFORMING CAMPAIGNS
    # =====================================================

    st.subheader("🏆 Top 10 Performing Campaigns")

    top_campaigns = (

        filtered_df

        .sort_values(
            "Revenue",
            ascending=False
        )

        [[
            "Campaign_Name",
            "Marketing_Channel",
            "Campaign_Type",
            "Region_Target",
            "Budget",
            "Spend",
            "Revenue",
            "ROI",
            "ROAS"
        ]]

        .head(10)

    )

    st.dataframe(

        top_campaigns,

        use_container_width=True,

        hide_index=True

    )

    st.markdown("---")

    # =====================================================
    # QUICK BUSINESS INSIGHTS
    # =====================================================

    st.subheader("📌 Quick Business Insights")

    st.markdown("""
    <style>

    .info-card{
        background:#111827;
        border-radius:18px;
        padding:20px;
        min-height:220px;
        border:1px solid #374151;
        box-shadow:0 6px 18px rgba(0,0,0,.25);
    }

    .blue{
        border-left:6px solid #2563EB;
    }

    .green{
        border-left:6px solid #10B981;
    }

    .orange{
        border-left:6px solid #F59E0B;
    }

    .big-text{
        font-size:42px;
        font-weight:800;
        color:white;
        line-height:1.2;
        margin-top:20px;
        margin-bottom:20px;
    }

    .small-text{
        color:#CBD5E1;
        font-size:16px;
    }

    .title{
        font-size:24px;
        font-weight:700;
        color:white;
    }

    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:

        with st.container(border=True):

            st.markdown("### 🏆 Best Marketing Channel")

            st.markdown(
                f"<h2 style='color:white;'>{best_channel}</h2>",
                unsafe_allow_html=True
            )

            st.caption("Highest Revenue Generated")

    with col2:

        with st.container(border=True):

            st.markdown("### 🌍 Best Region")

            st.markdown(
                f"<h2 style='color:white;'>{best_region}</h2>",
                unsafe_allow_html=True
            )

            st.caption("Highest Campaign Performance")

    with col3:

        with st.container(border=True):

            st.markdown("### 🚀 Best Campaign Type")

            st.markdown(
                f"<h2 style='color:white;'>{best_campaign}</h2>",
                unsafe_allow_html=True
            )

            st.caption("Highest Average ROI")
    

        st.markdown("---")

    # =====================================================
    # DOWNLOAD FILTERED DATA
    # =====================================================

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="📥 Download Dashboard Data",

        data=csv,

        file_name="Marketing_Dashboard.csv",

        mime="text/csv",

        use_container_width=True

    )
