"""
=========================================================
AI OPTIMIZATION CENTER
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
    page_title="AI Optimization Center",
    page_icon="💰",
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

from ai_engine.budget_optimizer import BudgetOptimizer
from ai_engine.strategy_simulator import MarketingStrategySimulator
from ai_engine.performance_forecast import PerformanceForecast

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.block-container{

    padding-top:2rem;

}

div[data-testid="stMetric"]{

    background:#111827;
    border-radius:16px;
    padding:18px;
    border:1px solid #374151;
    box-shadow:0 6px 16px rgba(0,0,0,.25);
    min-height:130px;

}

.optimize-box{

    background:#111827;
    border-left:6px solid #2563EB;
    padding:22px;
    border-radius:16px;
    margin-bottom:20px;

}

</style>
""", unsafe_allow_html=True)

# =========================================================
# MAIN
# =========================================================

def show_optimization():

    st.title("💰 AI Campaign Optimization Center")

    st.caption(
        "Optimize budgets, compare strategies and forecast campaign performance using AI."
    )

    st.markdown("---")

    # =====================================================
    # SIDEBAR
    # =====================================================

    with st.sidebar:

        st.subheader("⚙ AI Optimization")

        st.success("✔ Budget Optimizer")

        st.success("✔ Strategy Simulator")

        st.success("✔ Performance Forecast")

        st.markdown("---")

        st.info(
            """
### 💡 Optimization Tips

• Increase budget gradually

• Focus on high ROI campaigns

• Monitor ROAS every week

• Scale profitable campaigns only

• Compare strategies before deployment
"""
        )

    # =====================================================
    # OVERVIEW
    # =====================================================

    st.markdown(
        """
<div class="optimize-box">

<h3>🚀 AI Optimization Overview</h3>

This module helps you:

✔ Optimize Marketing Budget

✔ Compare Multiple Strategies

✔ Forecast Revenue & ROI

✔ Improve ROAS

✔ Maximize Profit

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("---")

    # =====================================================
    # TABS
    # =====================================================

    tab1, tab2, tab3 = st.tabs(
        [
            "💰 Budget Optimizer",
            "🎯 Strategy Simulator",
            "📈 Performance Forecast"
        ]
    )

    # =====================================================
    # TAB 1
    # =====================================================

    with tab1:

        optimizer = BudgetOptimizer()

        df = optimizer.optimize()

        st.subheader("💰 Budget Optimization Dashboard")

        # =====================================================
        # KPI CARDS
        # =====================================================

        total_budget = df["Budget"].sum()
        total_spend = df["Spend"].sum()
        total_revenue = df["Revenue"].sum()
        total_profit = df["Profit"].sum()

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "💰 Total Budget",
            f"${total_budget:,.0f}"
        )

        c2.metric(
            "💸 Total Spend",
            f"${total_spend:,.0f}"
        )

        c3.metric(
            "📈 Total Revenue",
            f"${total_revenue:,.0f}"
        )

        c4.metric(
            "💵 Total Profit",
            f"${total_profit:,.0f}"
        )

        st.markdown("")

        avg_roi = (
            (df["Profit"] / df["Spend"]) * 100
        ).mean()

        avg_efficiency = df["Budget_Efficiency"].mean()

        best_channel = (
            df.groupby("Marketing_Channel")["Profit"]
            .sum()
            .idxmax()
        )

        best_campaign = (
            df.sort_values(
                "Profit",
                ascending=False
            )
            .iloc[0]["Campaign_Name"]
        )

        c5, c6, c7, c8 = st.columns(4)

        c5.metric(
            "📊 Avg ROI",
            f"{avg_roi:.2f}%"
        )

        c6.metric(
            "⚡ Budget Efficiency",
            f"{avg_efficiency:.2f}%"
        )

        c7.metric(
            "🏆 Best Channel",
            best_channel
        )

        c8.metric(
            "🚀 Best Campaign",
            best_campaign
        )

        st.markdown("---")

        # =====================================================
        # AI SUMMARY
        # =====================================================

        st.info(f"""
### 🤖 AI Budget Optimization Summary

🏆 **Best Campaign:** {best_campaign}

📢 **Top Marketing Channel:** {best_channel}

💰 **Total Profit:** ${total_profit:,.0f}

📈 **Average Budget Efficiency:** {avg_efficiency:.2f}%

### AI Recommendation

Increase investment in **{best_channel}** campaigns because they are generating the highest overall profit while maintaining strong budget efficiency.
""")

        st.markdown("---")

        # =====================================================
        # CHART ROW 1
        # =====================================================

        left, right = st.columns(2)

        with left:

            fig = px.scatter(

                df,

                x="Budget",

                y="Revenue",

                size="Profit",

                color="Marketing_Channel",

                hover_name="Campaign_Name",

                title="Budget vs Revenue"

            )

            fig.update_layout(height=430)

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with right:

            top_budget = (

                df.sort_values(
                    "Recommended_Budget",
                    ascending=False
                )

                .head(10)

            )

            fig = px.bar(

                top_budget,

                x="Campaign_Name",

                y="Recommended_Budget",

                color="Recommended_Budget",

                title="Top Recommended Budgets"

            )

            fig.update_layout(height=430)

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # =====================================================
        # CHART ROW 2
        # =====================================================

        profit_df = (

            df.groupby("Marketing_Channel")["Profit"]

            .sum()

            .reset_index()

        )

        fig = px.bar(

            profit_df,

            x="Marketing_Channel",

            y="Profit",

            color="Profit",

            title="Profit by Marketing Channel"

        )

        fig.update_layout(height=430)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # =====================================================
        # OPTIMIZATION TABLE
        # =====================================================

        st.subheader("📋 Optimization Details")

        st.dataframe(

            df[
                [
                    "Campaign_Name",
                    "Marketing_Channel",
                    "Budget",
                    "Spend",
                    "Revenue",
                    "Profit",
                    "Budget_Efficiency",
                    "Recommendation",
                    "Recommended_Budget"
                ]
            ],

            use_container_width=True,

            hide_index=True

        )

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(

            label="📥 Download Budget Optimization Report",

            data=csv,

            file_name="Budget_Optimization_Report.csv",

            mime="text/csv",

            use_container_width=True

        )

    # =====================================================
    # TAB 2 : STRATEGY SIMULATOR
    # =====================================================

    with tab2:

        simulator = MarketingStrategySimulator()

        comparison = simulator.compare_strategies()

        st.subheader("🎯 AI Strategy Simulator")

        # =====================================================
        # KPI CARDS
        # =====================================================

        best = comparison.sort_values(
            "Average Revenue",
            ascending=False
        ).iloc[0]

        avg_revenue = comparison["Average Revenue"].mean()
        avg_roi = comparison["Average ROI"].mean()

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "🏆 Best Strategy",
            best["Strategy"]
        )

        c2.metric(
            "📈 Avg Revenue",
            f"${avg_revenue:,.0f}"
        )

        c3.metric(
            "💹 Avg ROI",
            f"{avg_roi:.2f}%"
        )

        st.markdown("---")

        # =====================================================
        # AI SUMMARY
        # =====================================================

        st.success(f"""
### 🤖 AI Strategy Recommendation

🏆 **Best Strategy:** {best['Strategy']}

💰 **Expected Revenue:** ${best['Average Revenue']:,.0f}

📈 **Expected ROI:** {best['Average ROI']:.2f}%

### Recommendation

Increase investment in **{best['Strategy']}** because it currently delivers the highest expected revenue and return on investment.
""")

        st.markdown("---")

        # =====================================================
        # CHARTS
        # =====================================================

        left, right = st.columns(2)

        with left:

            fig = px.bar(

                comparison,

                x="Strategy",

                y="Average Revenue",

                color="Average Revenue",

                title="Average Revenue by Strategy"

            )

            fig.update_layout(height=430)

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with right:

            fig = px.bar(

                comparison,

                x="Strategy",

                y="Average ROI",

                color="Average ROI",

                title="Average ROI by Strategy"

            )

            fig.update_layout(height=430)

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # =====================================================
        # STRATEGY TABLE
        # =====================================================

        st.subheader("📋 Strategy Comparison")

        st.dataframe(

            comparison,

            use_container_width=True,

            hide_index=True

        )

        csv = comparison.to_csv(index=False).encode("utf-8")

        st.download_button(

            label="📥 Download Strategy Report",

            data=csv,

            file_name="Strategy_Simulation_Report.csv",

            mime="text/csv",

            use_container_width=True

        )

    # =====================================================
    # TAB 3 : PERFORMANCE FORECAST
    # =====================================================

    with tab3:

        forecast = PerformanceForecast()

        forecast.train_models()

        st.subheader("📈 AI Performance Forecast")

        avg_budget = int(
            forecast.df["Budget"].mean()
        )

        budget = st.slider(

            "💰 Select Forecast Budget",

            min_value=int(avg_budget * 0.5),

            max_value=int(avg_budget * 2),

            value=avg_budget,

            step=1000

        )

        result = forecast.forecast(budget)

        # =====================================================
        # KPI CARDS
        # =====================================================

        c1, c2 = st.columns(2)

        c1.metric(
            "💰 Expected Revenue",
            f"${result['Expected Revenue']:,.0f}"
        )

        c2.metric(
            "📈 Expected ROI",
            f"{result['Expected ROI']:.2f}%"
        )

        c3, c4 = st.columns(2)

        c3.metric(
            "🎯 Expected ROAS",
            f"{result['Expected ROAS']:.2f}"
        )

        c4.metric(
            "⚡ Conversion Rate",
            f"{result['Expected Conversion Rate']:.2f}%"
        )

        st.markdown("---")

        # =====================================================
        # AI FORECAST SUMMARY
        # =====================================================

        roi = result["Expected ROI"]

        if roi >= 150:

            recommendation = "🚀 Aggressively scale this campaign."

        elif roi >= 100:

            recommendation = "📈 Increase budget gradually."

        elif roi >= 50:

            recommendation = "⚠ Optimize before scaling."

        else:

            recommendation = "❌ Reduce spend and improve campaign quality."

        st.info(f"""
### 🤖 AI Forecast Summary

💰 **Forecast Budget:** ${budget:,.0f}

📈 **Expected Revenue:** ${result['Expected Revenue']:,.0f}

🚀 **Expected ROI:** {result['Expected ROI']:.2f}%

🎯 **Expected ROAS:** {result['Expected ROAS']:.2f}

### AI Recommendation

{recommendation}
""")

        st.markdown("---")

        # =====================================================
        # FORECAST CHART
        # =====================================================

        forecast_df = forecast.scenario_analysis()

        fig = px.line(

            forecast_df,

            x=forecast_df.columns[0],

            y=forecast_df.columns[1],

            markers=True,

            title="Revenue Forecast Scenario"

        )

        fig.update_layout(height=430)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # =====================================================
        # SCENARIO TABLE
        # =====================================================

        st.subheader("📋 Scenario Analysis")

        st.dataframe(

            forecast_df,

            use_container_width=True,

            hide_index=True

        )

        # =====================================================
        # DOWNLOAD
        # =====================================================

        csv = forecast_df.to_csv(index=False).encode("utf-8")

        st.download_button(

            label="📥 Download Forecast Report",

            data=csv,

            file_name="Performance_Forecast_Report.csv",

            mime="text/csv",

            use_container_width=True

        )

    # =====================================================
    # FINAL AI SUMMARY
    # =====================================================

    st.markdown("---")

    st.success("""
✅ AI Optimization Analysis Completed Successfully

✔ Budget Optimization Completed

✔ Strategy Comparison Completed

✔ Performance Forecast Generated

✔ AI Recommendations Ready
""")


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    show_optimization()