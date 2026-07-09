"""
=========================================================
AI INSIGHTS CENTER
AI Marketing Campaign Intelligence Platform
=========================================================
"""

import os
import sys
import pandas as pd
import streamlit as st
import plotly.express as px

# =========================================================
# PATH
# =========================================================

ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

PYTHON_FOLDER = os.path.join(ROOT, "python")

if PYTHON_FOLDER not in sys.path:
    sys.path.append(PYTHON_FOLDER)

from ai_engine.business_advisor import AIBusinessAdvisor
from ai_engine.campaign_health import CampaignHealthScore
from ai_engine.risk_detector import CampaignRiskDetector
from ai_engine.smart_alerts import SmartAlerts

# =========================================================
# MODERN CSS
# =========================================================

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
}

.metric-card{
    background:#111827;
    padding:18px;
    border-radius:18px;
    border:1px solid #374151;
    text-align:center;
    box-shadow:0px 6px 18px rgba(0,0,0,.25);
}

.summary-card{
    background:#111827;
    padding:22px;
    border-radius:18px;
    border-left:6px solid #3B82F6;
    margin-bottom:20px;
}

.ai-box{
    background:linear-gradient(90deg,#2563EB,#06B6D4);
    padding:30px;
    border-radius:20px;
    color:white;
    margin-bottom:25px;
}

div[data-testid="stMetric"]{
    background:#111827;
    padding:18px;
    border-radius:18px;
    border:1px solid #374151;
    box-shadow:0px 5px 15px rgba(0,0,0,.25);
    min-height:125px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# MAIN
# =========================================================

def show_ai_insights():

    st.title("🤖 AI Business Insights Center")

    st.caption(
        "AI Powered Business Intelligence, Campaign Health, Risk Detection & Smart Alerts."
    )

    st.markdown("---")

    # =====================================================
    # HERO
    # =====================================================

    st.markdown("""

<div class="ai-box">

<h2>🚀 AI Insights Center</h2>

<p style="font-size:18px">

Monitor campaign performance using Artificial Intelligence.

Get executive recommendations, health monitoring,
risk detection and smart alerts in one place.

</p>

</div>

""", unsafe_allow_html=True)

    # =====================================================
    # SIDEBAR
    # =====================================================

    with st.sidebar:

        st.subheader("🧠 AI Modules")

        st.success("✔ Business Advisor")
        st.success("✔ Campaign Health")
        st.success("✔ Risk Detection")
        st.success("✔ Smart Alerts")

        st.markdown("---")

        st.info("""
AI continuously analyzes campaign data and provides
real-time business recommendations.
""")

    # =====================================================
    # TABS
    # =====================================================

    tab1, tab2, tab3, tab4 = st.tabs([
        "🤖 Business Advisor",
        "❤️ Campaign Health",
        "⚠ Risk Detection",
        "🚨 Smart Alerts"
    ])

    # =====================================================
    # BUSINESS ADVISOR
    # =====================================================

    with tab1:

        advisor = AIBusinessAdvisor()

        summary = advisor.dataset_summary()

        budget = advisor.budget_analysis()

        feature_df = advisor.important_features()

        # ==========================================
        # KPI CARDS
        # ==========================================

        c1,c2,c3,c4 = st.columns(4)

        c1.metric(
            "📢 Campaigns",
            summary["Total Campaigns"]
        )

        c2.metric(
            "✅ Successful",
            summary["Successful"]
        )

        c3.metric(
            "❌ Failed",
            summary["Unsuccessful"]
        )

        c4.metric(
            "📈 Success Rate",
            f"{summary['Success Rate']}%"
        )

        st.markdown("---")

        # ==========================================
        # AI EXECUTIVE SUMMARY
        # ==========================================

        st.markdown(f"""

<div class="summary-card">

<h3>🤖 Executive Business Summary</h3>

<b>Total Campaigns :</b> {summary['Total Campaigns']}<br><br>

<b>Campaign Success Rate :</b> {summary['Success Rate']}%<br><br>

<b>Average ROI :</b> {budget['Average ROI']}%<br><br>

<b>Average ROAS :</b> {budget['Average ROAS']}<br><br>

<b>AI Recommendation</b>

<ul>

<li>Increase investment in high-performing campaigns.</li>

<li>Reduce budget on consistently low ROI campaigns.</li>

<li>Focus more on high ROAS marketing channels.</li>

</ul>

</div>

""", unsafe_allow_html=True)

        st.markdown("---")

        # ==========================================
        # CHARTS
        # ==========================================

        left,right = st.columns(2)

        with left:

            fig = px.bar(
                feature_df.head(10),
                x="Feature",
                y="Importance",
                color="Importance",
                title="Top Machine Learning Features"
            )

            fig.update_layout(
                height=430,
                xaxis_title="",
                yaxis_title="Importance"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with right:

            fig = px.pie(
                values=[
                    summary["Successful"],
                    summary["Unsuccessful"]
                ],
                names=[
                    "Successful",
                    "Failed"
                ],
                hole=.60,
                title="Campaign Success Distribution"
            )

            fig.update_layout(height=430)

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.markdown("---")

        # ==========================================
        # TABLES
        # ==========================================

        st.subheader("💰 Budget Insights")

        budget_df = pd.DataFrame(
            budget.items(),
            columns=["Metric", "Value"]
        )

        st.dataframe(
            budget_df,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("🏆 Feature Importance")

        st.dataframe(
            feature_df,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("🤖 AI Recommendations")

        for rec in advisor.recommendations():
            st.success(rec)

        csv = feature_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Feature Importance",
            csv,
            "feature_importance.csv",
            "text/csv"
        )

    # =====================================================
    # CAMPAIGN HEALTH
    # =====================================================

    with tab2:

        health = CampaignHealthScore()

        df = health.calculate_health()

        avg_health = round(df["Health_Score"].mean(), 2)
        best_health = round(df["Health_Score"].max(), 2)
        poor_campaigns = len(df[df["Health_Score"] < 50])

        # ==========================================
        # KPI CARDS
        # ==========================================

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "❤️ Average Health",
            f"{avg_health}%"
        )

        c2.metric(
            "🏆 Best Score",
            f"{best_health}%"
        )

        c3.metric(
            "⚠ Poor Campaigns",
            poor_campaigns
        )

        st.markdown("---")

        # ==========================================
        # AI EXECUTIVE SUMMARY
        # ==========================================

        if avg_health >= 80:

            status = "Excellent"

            recommendation = """
Continue scaling high-performing campaigns while
maintaining the current optimization strategy.
"""

        elif avg_health >= 60:

            status = "Stable"

            recommendation = """
Some campaigns require optimization.
Review ROI before increasing budget.
"""

        else:

            status = "Critical"

            recommendation = """
Several campaigns need immediate optimization.
Reduce spend on weak campaigns.
"""

        st.markdown(f"""

<div class="summary-card">

<h3>❤️ Campaign Health Summary</h3>

<b>Overall Health :</b> {status}<br><br>

<b>Average Health Score :</b> {avg_health}%<br><br>

<b>Best Campaign Score :</b> {best_health}%<br><br>

<b>Poor Campaigns :</b> {poor_campaigns}<br><br>

<b>AI Recommendation</b>

<p>

{recommendation}

</p>

</div>

""", unsafe_allow_html=True)

        st.markdown("---")

        # ==========================================
        # CHARTS
        # ==========================================

        left, right = st.columns(2)

        with left:

            fig = px.histogram(
                df,
                x="Health_Score",
                nbins=20,
                color_discrete_sequence=["#22C55E"],
                title="Campaign Health Distribution"
            )

            fig.update_layout(
                height=430,
                xaxis_title="Health Score",
                yaxis_title="Campaign Count"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with right:

            top_health = (
                df.sort_values(
                    "Health_Score",
                    ascending=False
                )
                .head(10)
            )

            fig = px.bar(
                top_health,
                x="Campaign_Name",
                y="Health_Score",
                color="Health_Score",
                text_auto=".1f",
                title="Top Healthy Campaigns"
            )

            fig.update_layout(
                height=430,
                xaxis_title="",
                yaxis_title="Health Score"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.markdown("---")

        # ==========================================
        # HEALTH TABLE
        # ==========================================

        st.subheader("📋 Campaign Health Report")

        st.dataframe(
            df.sort_values(
                "Health_Score",
                ascending=False
            ),
            use_container_width=True,
            hide_index=True
        )

        # ==========================================
        # TOP 5 HEALTHY CAMPAIGNS
        # ==========================================

        st.subheader("🏆 Top 5 Healthy Campaigns")

        st.dataframe(
            top_health.head(5),
            use_container_width=True,
            hide_index=True
        )

        # ==========================================
        # DOWNLOAD
        # ==========================================

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Campaign Health Report",
            csv,
            "campaign_health_report.csv",
            "text/csv"
        )

    # =====================================================
    # RISK DETECTION
    # =====================================================

    with tab3:

        risk = CampaignRiskDetector()

        risk_df = risk.detect()

        avg_risk = round(
            risk_df["Risk_Score"].mean(),
            2
        )

        highest_risk = round(
            risk_df["Risk_Score"].max(),
            2
        )

        risky_campaigns = len(
            risk_df[
                risk_df["Risk_Score"] >= 70
            ]
        )

        # ==========================================
        # KPI CARDS
        # ==========================================

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "⚠ Average Risk",
            f"{avg_risk}%"
        )

        c2.metric(
            "🔥 Highest Risk",
            f"{highest_risk}%"
        )

        c3.metric(
            "🚨 High Risk Campaigns",
            risky_campaigns
        )

        st.markdown("---")

        # ==========================================
        # AI EXECUTIVE SUMMARY
        # ==========================================

        if avg_risk <= 30:

            status = "🟢 LOW"

            recommendation = """
Current campaigns are performing safely.
Continue scaling high ROI campaigns.
"""

        elif avg_risk <= 60:

            status = "🟡 MODERATE"

            recommendation = """
Closely monitor ROI,
CTR and Conversion Rate before increasing budget.
"""

        else:

            status = "🔴 HIGH"

            recommendation = """
Reduce spend on risky campaigns immediately
and optimize audience targeting.
"""

        st.markdown(f"""

<div class="summary-card">

<h3>⚠ AI Risk Assessment</h3>

<b>Overall Risk Status :</b> {status}<br><br>

<b>Average Risk Score :</b> {avg_risk}%<br><br>

<b>Highest Risk Score :</b> {highest_risk}%<br><br>

<b>High Risk Campaigns :</b> {risky_campaigns}<br><br>

<b>AI Recommendation</b>

<p>

{recommendation}

</p>

</div>

""", unsafe_allow_html=True)

        st.markdown("---")

        # ==========================================
        # CHARTS
        # ==========================================

        left, right = st.columns(2)

        with left:

            top_risk = (

                risk_df
                .sort_values(
                    "Risk_Score",
                    ascending=False
                )
                .head(10)

            )

            fig = px.bar(

                top_risk,

                x="Campaign_Name",

                y="Risk_Score",

                color="Risk_Score",

                text_auto=".1f",

                title="Top 10 Highest Risk Campaigns"

            )

            fig.update_layout(

                height=430,

                xaxis_title="",

                yaxis_title="Risk Score"

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with right:

            fig = px.histogram(

                risk_df,

                x="Risk_Score",

                nbins=20,

                color_discrete_sequence=["#EF4444"],

                title="Risk Score Distribution"

            )

            fig.update_layout(

                height=430,

                xaxis_title="Risk Score",

                yaxis_title="Campaign Count"

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.markdown("---")

        # ==========================================
        # TOP RISK CAMPAIGNS
        # ==========================================

        st.subheader("🚨 Top 10 Risky Campaigns")

        st.dataframe(

            top_risk,

            use_container_width=True,

            hide_index=True

        )

        st.markdown("---")

        # ==========================================
        # COMPLETE RISK REPORT
        # ==========================================

        st.subheader("📋 Complete Risk Report")

        st.dataframe(

            risk_df.sort_values(
                "Risk_Score",
                ascending=False
            ),

            use_container_width=True,

            hide_index=True

        )

        # ==========================================
        # DOWNLOAD
        # ==========================================

        csv = risk_df.to_csv(index=False).encode("utf-8")

        st.download_button(

            "📥 Download Risk Report",

            csv,

            "campaign_risk_report.csv",

            "text/csv"

        )

    # =====================================================
    # SMART ALERTS
    # =====================================================

    with tab4:

        alerts = SmartAlerts()

        alert_df = alerts.generate_alerts()

        total_alerts = len(alert_df)

        if total_alerts == 0:

            high_alerts = 0
            medium_alerts = 0

        else:

            if "Severity" in alert_df.columns:

                high_alerts = len(
                    alert_df[
                        alert_df["Severity"].astype(str).str.upper() == "HIGH"
                    ]
                )

                medium_alerts = len(
                    alert_df[
                        alert_df["Severity"].astype(str).str.upper() == "MEDIUM"
                    ]
                )

            else:

                high_alerts = 0
                medium_alerts = total_alerts

        # ==========================================
        # KPI CARDS
        # ==========================================

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "🚨 Total Alerts",
            total_alerts
        )

        c2.metric(
            "🔴 High Priority",
            high_alerts
        )

        c3.metric(
            "🟡 Medium Priority",
            medium_alerts
        )

        st.markdown("---")

        # ==========================================
        # AI SUMMARY
        # ==========================================

        if total_alerts == 0:

            st.markdown("""

<div class="summary-card">

<h3>🚨 Smart Alert Summary</h3>

<b>Status :</b> Excellent ✅

<p>

No active alerts detected.

All campaigns are operating within acceptable
performance thresholds.

</p>

</div>

""", unsafe_allow_html=True)

        else:

            st.markdown(f"""

<div class="summary-card">

<h3>🚨 Smart Alert Summary</h3>

<b>Total Alerts :</b> {total_alerts}<br><br>

<b>High Priority :</b> {high_alerts}<br><br>

<b>Medium Priority :</b> {medium_alerts}<br><br>

<b>AI Recommendation</b>

<p>

Resolve High Priority alerts immediately.

Monitor ROI, CTR, Conversion Rate and campaign
spending regularly to avoid future risks.

</p>

</div>

""", unsafe_allow_html=True)

        st.markdown("---")

        # ==========================================
        # ALERT TABLE
        # ==========================================

        if total_alerts > 0:

            st.subheader("🚨 Active Campaign Alerts")

            st.dataframe(
                alert_df,
                use_container_width=True,
                hide_index=True
            )

            csv = alert_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "📥 Download Alert Report",
                csv,
                "campaign_alerts.csv",
                "text/csv"
            )

        else:

            st.success("🎉 No Smart Alerts Available.")

    # =====================================================
    # EXECUTIVE AI CONCLUSION
    # =====================================================

    st.markdown("---")

    st.subheader("📌 Executive AI Conclusion")

    left, right = st.columns(2)

    with left:

        st.markdown("""

<div class="summary-card">

<h3>✅ Strengths</h3>

✔ Campaign health monitored continuously.<br><br>

✔ AI identifies best-performing campaigns.<br><br>

✔ Budget allocation optimized automatically.<br><br>

✔ Marketing performance improving consistently.

</div>

""", unsafe_allow_html=True)

    with right:

        st.markdown("""

<div class="summary-card">

<h3>⚠ Focus Areas</h3>

Monitor high-risk campaigns.<br><br>

Improve CTR & Conversion Rate.<br><br>

Reduce spend on poor ROI campaigns.<br><br>

Resolve Smart Alerts quickly.

</div>

""", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""

<div class="summary-card">

<h2>🚀 Final AI Recommendation</h2>

Based on the complete campaign analysis, the AI engine
recommends increasing investment in high-performing
marketing channels while gradually reducing spending on
low ROI campaigns.

Continue monitoring Campaign Health,
Risk Score and Smart Alerts to maximize
overall marketing profitability.

</div>

""", unsafe_allow_html=True)

    st.markdown("---")

    st.success("✅ AI Insights Center Loaded Successfully")