"""
=========================================================
AI CAMPAIGN PREDICTION
AI Marketing Campaign Intelligence Platform
=========================================================
"""

import os
import joblib
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Campaign Prediction",
    page_icon="🎯",
    layout="wide"
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

MODEL_PATH = os.path.join(
    ROOT,
    "python",
    "models",
    "campaign_success_model.pkl"
)

ENCODER_PATH = os.path.join(
    ROOT,
    "python",
    "models",
    "encoders.pkl"
)

FEATURE_PATH = os.path.join(
    ROOT,
    "python",
    "models",
    "feature_columns.pkl"
)

# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load(MODEL_PATH)
encoders = joblib.load(ENCODER_PATH)
feature_columns = joblib.load(FEATURE_PATH)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.block-container{
    padding-top:1.5rem;
}

/* Metric Cards */

div[data-testid="stMetric"]{

    background:#111827;
    border-radius:18px;
    padding:18px;
    border:1px solid #374151;
    box-shadow:0px 8px 18px rgba(0,0,0,.25);
    min-height:120px;

}

/* Predict Button */

.stButton>button{

    width:100%;
    height:55px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
    background:#2563EB;
    color:white;

}

/* Input Card */

.pred-box{

    background:#111827;
    padding:20px;
    border-radius:18px;
    border-left:6px solid #2563EB;
    margin-bottom:20px;

}

/* Result Card */

.result-box{

    background:#0F172A;
    padding:20px;
    border-radius:18px;
    border:1px solid #334155;

}

</style>

""", unsafe_allow_html=True)

# =========================================================
# MAIN
# =========================================================

def show_prediction():

    st.title("🎯 AI Campaign Success Prediction")

    st.caption(
        "Predict campaign performance using Artificial Intelligence and Machine Learning."
    )

    st.markdown("---")

    # =====================================================
    # INPUT CARD
    # =====================================================

    st.markdown("""

<div class="pred-box">

<h3>📝 Campaign Information</h3>

Enter campaign metrics below and click
<b>Predict Campaign Success</b>.

</div>

""", unsafe_allow_html=True)

    left, right = st.columns(2)

    # =====================================================
    # LEFT SIDE
    # =====================================================

    with left:

        budget = st.number_input(
            "💰 Budget ($)",
            min_value=1000.0,
            max_value=10000000.0,
            value=50000.0,
            step=1000.0
        )

        impressions = st.number_input(
            "👀 Impressions",
            min_value=1000,
            max_value=100000000,
            value=500000,
            step=1000
        )

        clicks = st.number_input(
            "🖱 Clicks",
            min_value=0,
            max_value=5000000,
            value=15000,
            step=100
        )

        spend = st.number_input(
            "💸 Spend ($)",
            min_value=1000.0,
            max_value=10000000.0,
            value=35000.0,
            step=1000.0
        )

        revenue = st.number_input(
            "📈 Revenue ($)",
            min_value=1000.0,
            max_value=50000000.0,
            value=90000.0,
            step=1000.0
        )

    # =====================================================
    # RIGHT SIDE
    # =====================================================

    with right:

        ctr = st.number_input(
            "📊 CTR (%)",
            min_value=0.0,
            max_value=100.0,
            value=5.5
        )

        conversion = st.number_input(
            "🎯 Conversion Rate (%)",
            min_value=0.0,
            max_value=100.0,
            value=4.5
        )

        roi = st.number_input(
            "📈 ROI (%)",
            min_value=-100.0,
            max_value=1000.0,
            value=120.0
        )

        roas = st.number_input(
            "💹 ROAS",
            min_value=0.0,
            max_value=20.0,
            value=3.5
        )

        engagement = st.number_input(
            "❤️ Engagement Rate (%)",
            min_value=0.0,
            max_value=100.0,
            value=25.0
        )

    st.write("")

    predict = st.button(
        "🚀 Predict Campaign Success"
    )

    # =====================================================
    # PREDICTION
    # =====================================================

    if predict:

        input_df = pd.DataFrame({

            "Budget":[budget],
            "Impressions":[impressions],
            "Clicks":[clicks],
            "Spend":[spend],
            "Revenue":[revenue],
            "CTR":[ctr],
            "Conversion_Rate":[conversion],
            "ROI":[roi],
            "ROAS":[roas],
            "Engagement_Rate":[engagement]

        })

        # ---------------------------------------
        # Prepare Model Input
        # ---------------------------------------

        for col in feature_columns:

            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[feature_columns]

        prediction = model.predict(input_df)[0]

        probability = float(
            model.predict_proba(input_df)[0][1]
        )

        success_score = round(
            probability * 100,
            2
        )

        # ---------------------------------------
        # Campaign Grade
        # ---------------------------------------

        if success_score >= 90:

            grade = "A+"
            health = "Excellent"

        elif success_score >= 80:

            grade = "A"
            health = "Very Good"

        elif success_score >= 70:

            grade = "B"
            health = "Good"

        elif success_score >= 50:

            grade = "C"
            health = "Average"

        else:

            grade = "D"
            health = "Poor"

        st.markdown("---")

        # ---------------------------------------
        # Prediction Result
        # ---------------------------------------

        st.markdown('<div class="result-box">', unsafe_allow_html=True)

        if prediction == 1:

            st.success(
                "✅ Campaign is likely to be SUCCESSFUL"
            )

        else:

            st.error(
                "❌ Campaign is likely to FAIL"
            )

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("---")

        # =====================================================
        # KPI CARDS
        # =====================================================

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "🎯 Success Probability",
                f"{success_score:.2f}%"
            )

        with c2:

            st.metric(
                "🏅 Campaign Grade",
                grade
            )

        st.write("")

        c3, c4 = st.columns(2)

        with c3:

            st.metric(
                "❤️ Campaign Health",
                health
            )

        with c4:

            st.metric(
                "📈 Expected ROI",
                f"{roi:.2f}%"
            )

        st.markdown("---")

        # =====================================================
        # AI SUCCESS GAUGE
        # =====================================================

        fig = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=success_score,

                number={"suffix": "%"},

                title={

                    "text": "AI Campaign Success Score"

                },

                gauge={

                    "axis": {

                        "range": [0, 100]

                    },

                    "bar": {

                        "color": "#2563EB"

                    },

                    "steps": [

                        {
                            "range": [0, 50],
                            "color": "#EF4444"
                        },

                        {
                            "range": [50, 70],
                            "color": "#FACC15"
                        },

                        {
                            "range": [70, 90],
                            "color": "#3B82F6"
                        },

                        {
                            "range": [90, 100],
                            "color": "#22C55E"
                        }

                    ]

                }

            )

        )

        fig.update_layout(

            height=380,

            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            )

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

        st.markdown("---")

        # =====================================================
        # AI SCORE INTERPRETATION
        # =====================================================

        st.subheader("🤖 AI Performance Analysis")

        if success_score >= 90:

            st.success(
                "🔥 Outstanding campaign performance predicted. This campaign has a very high probability of success."
            )

        elif success_score >= 80:

            st.success(
                "🚀 Strong campaign performance expected with excellent business potential."
            )

        elif success_score >= 70:

            st.info(
                "👍 Campaign looks good. Minor optimizations can further improve performance."
            )

        elif success_score >= 50:

            st.warning(
                "⚠️ Campaign has average success probability. Consider optimizing targeting and budget allocation."
            )

        else:

            st.error(
                "🚨 High risk campaign detected. Significant optimization is recommended before launch."
            )

        st.markdown("---")

        # =====================================================
        # AI RECOMMENDATIONS
        # =====================================================

        st.subheader("🤖 AI Recommendations")

        recommendations = []

        if roi < 100:
            recommendations.append(
                "📈 Increase ROI by improving audience targeting and campaign creatives."
            )

        if roas < 2:
            recommendations.append(
                "💰 Reduce acquisition cost to improve ROAS."
            )

        if ctr < 5:
            recommendations.append(
                "🖱 Improve ad creatives and CTA to increase CTR."
            )

        if conversion < 5:
            recommendations.append(
                "🎯 Optimize landing pages to improve conversion rate."
            )

        if engagement < 20:
            recommendations.append(
                "❤️ Publish more engaging content to improve audience interaction."
            )

        if spend > budget:
            recommendations.append(
                "⚠ Campaign spend has exceeded the allocated budget."
            )

        if revenue < spend:
            recommendations.append(
                "❌ Revenue is lower than spend. Immediate optimization is recommended."
            )

        if len(recommendations) == 0:

            st.success(
                "🎉 Excellent Campaign! AI recommends continuing the current strategy."
            )

        else:

            for rec in recommendations:

                st.info(rec)

        st.markdown("---")

        # =====================================================
        # CAMPAIGN INPUT SUMMARY
        # =====================================================

        st.subheader("📋 Campaign Summary")

        summary_df = pd.DataFrame({

            "Metric": [

                "Budget",

                "Spend",

                "Revenue",

                "Impressions",

                "Clicks",

                "CTR",

                "Conversion Rate",

                "ROI",

                "ROAS",

                "Engagement Rate"

            ],

            "Value": [

                f"${budget:,.0f}",

                f"${spend:,.0f}",

                f"${revenue:,.0f}",

                f"{impressions:,}",

                f"{clicks:,}",

                f"{ctr:.2f}%",

                f"{conversion:.2f}%",

                f"{roi:.2f}%",

                f"{roas:.2f}",

                f"{engagement:.2f}%"

            ]

        })

        st.dataframe(

            summary_df,

            use_container_width=True,

            hide_index=True

        )

        st.markdown("---")

        # =====================================================
        # DOWNLOAD REPORT
        # =====================================================

        report = pd.DataFrame({

            "Prediction": [

                "Successful" if prediction == 1 else "Failed"

            ],

            "Success Probability (%)": [

                success_score

            ],

            "Campaign Grade": [

                grade

            ],

            "Campaign Health": [

                health

            ],

            "Budget": [

                budget

            ],

            "Spend": [

                spend

            ],

            "Revenue": [

                revenue

            ],

            "ROI (%)": [

                roi

            ],

            "ROAS": [

                roas

            ],

            "CTR (%)": [

                ctr

            ],

            "Conversion Rate (%)": [

                conversion

            ],

            "Engagement Rate (%)": [

                engagement

            ]

        })

        csv = report.to_csv(index=False).encode("utf-8")

        st.download_button(

            label="📥 Download Prediction Report",

            data=csv,

            file_name="AI_Campaign_Prediction_Report.csv",

            mime="text/csv",

            use_container_width=True

        )

        st.markdown("---")

        st.success("✅ AI Prediction Completed Successfully")


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    show_prediction()