"""
=========================================================
CAMPAIGN RISK DETECTOR
AI Marketing Campaign Intelligence Platform
=========================================================
"""

import os
import pandas as pd


class CampaignRiskDetector:

    def __init__(self):

        self.root = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                ".."
            )
        )

        self.data_path = os.path.join(
            self.root,
            "python",
            "data_generation",
            "data",
            "processed",
            "campaign_dashboard_dataset.csv"
        )

        self.df = pd.read_csv(self.data_path)

    # ---------------------------------------------------------

    def calculate_risk_score(self):

        df = self.df.copy()

        roi_risk = (
            1 - (df["ROI"] / df["ROI"].max())
        ) * 30

        roas_risk = (
            1 - (df["ROAS"] / df["ROAS"].max())
        ) * 25

        ctr_risk = (
            1 - (df["CTR"] / df["CTR"].max())
        ) * 15

        conversion_risk = (
            1 - (
                df["Conversion_Rate"] /
                df["Conversion_Rate"].max()
            )
        ) * 15

        bounce_risk = (
            df["Bounce_Rate"] /
            df["Bounce_Rate"].max()
        ) * 10

        spend_risk = (
            df["Spend"] /
            df["Spend"].max()
        ) * 5

        df["Risk_Score"] = (

            roi_risk +

            roas_risk +

            ctr_risk +

            conversion_risk +

            bounce_risk +

            spend_risk

        ).round(2)

        return df

    # ---------------------------------------------------------

    def risk_level(self, score):

        if score >= 75:
            return "Critical"

        elif score >= 60:
            return "High"

        elif score >= 40:
            return "Medium"

        elif score >= 20:
            return "Low"

        else:
            return "Very Low"

    # ---------------------------------------------------------

    def recommendation(self, level):

        recommendations = {

            "Critical":
                "Pause campaign and investigate immediately.",

            "High":
                "Reduce budget and optimize targeting.",

            "Medium":
                "Improve creatives and landing page.",

            "Low":
                "Monitor campaign performance regularly.",

            "Very Low":
                "Campaign is healthy. Continue scaling."

        }

        return recommendations[level]

    # ---------------------------------------------------------

    def detect(self):

        df = self.calculate_risk_score()

        df["Risk_Level"] = df["Risk_Score"].apply(
            self.risk_level
        )

        df["Recommendation"] = df["Risk_Level"].apply(
            self.recommendation
        )

        return df

    # ---------------------------------------------------------

    def generate_report(self):

        df = self.detect()

        print("\n")
        print("=" * 70)
        print("CAMPAIGN RISK DETECTOR")
        print("=" * 70)

        print("\nAverage Risk Score :",
              round(df["Risk_Score"].mean(), 2))

        print("\nRisk Distribution\n")

        print(
            df["Risk_Level"]
            .value_counts()
        )

        print("\nHighest Risk Campaigns\n")

        cols = [

            "Campaign_ID",

            "Campaign_Name",

            "Marketing_Channel",

            "ROI",

            "ROAS",

            "CTR",

            "Conversion_Rate",

            "Bounce_Rate",

            "Risk_Score",

            "Risk_Level",

            "Recommendation"

        ]

        print(

            df[cols]

            .sort_values(

                "Risk_Score",

                ascending=False

            )

            .head(10)

        )

        print("\nLowest Risk Campaigns\n")

        print(

            df[cols]

            .sort_values(

                "Risk_Score"

            )

            .head(10)

        )

        print("\n")

        print("=" * 70)
        print("RISK DETECTION COMPLETED")
        print("=" * 70)

        return df


if __name__ == "__main__":

    detector = CampaignRiskDetector()

    detector.generate_report()