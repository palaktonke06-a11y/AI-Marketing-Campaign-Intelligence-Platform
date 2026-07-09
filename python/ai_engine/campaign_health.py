"""
=========================================================
CAMPAIGN HEALTH SCORE
AI Marketing Campaign Intelligence Platform
=========================================================
"""

import os
import pandas as pd


class CampaignHealthScore:

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

    def calculate_health(self):

        df = self.df.copy()

        roi_score = (df["ROI"] / df["ROI"].max()) * 30

        roas_score = (df["ROAS"] / df["ROAS"].max()) * 25

        ctr_score = (df["CTR"] / df["CTR"].max()) * 15

        conversion_score = (
            df["Conversion_Rate"] /
            df["Conversion_Rate"].max()
        ) * 15

        engagement_score = (
            df["Engagement_Rate"] /
            df["Engagement_Rate"].max()
        ) * 10

        bounce_score = (
            1 -
            (df["Bounce_Rate"] /
             df["Bounce_Rate"].max())
        ) * 5

        df["Health_Score"] = (

            roi_score +

            roas_score +

            ctr_score +

            conversion_score +

            engagement_score +

            bounce_score

        ).round(2)

        return df

    # ---------------------------------------------------------

    def health_status(self, score):

        if score >= 85:
            return "Excellent"

        elif score >= 70:
            return "Good"

        elif score >= 55:
            return "Average"

        elif score >= 40:
            return "Poor"

        else:
            return "Critical"

    # ---------------------------------------------------------

    def generate_report(self):

        df = self.calculate_health()

        df["Health_Status"] = df["Health_Score"].apply(
            self.health_status
        )

        print("\n")
        print("=" * 70)
        print("CAMPAIGN HEALTH REPORT")
        print("=" * 70)

        print("\nAverage Health Score :",
              round(df["Health_Score"].mean(), 2))

        print("\nHealth Distribution\n")

        print(
            df["Health_Status"]
            .value_counts()
        )

        print("\nTop 10 Healthy Campaigns\n")

        cols = [

            "Campaign_ID",

            "Campaign_Name",

            "Marketing_Channel",

            "ROI",

            "ROAS",

            "CTR",

            "Conversion_Rate",

            "Health_Score",

            "Health_Status"

        ]

        print(

            df[cols]

            .sort_values(

                "Health_Score",

                ascending=False

            )

            .head(10)

        )

        print("\nBottom 10 Campaigns\n")

        print(

            df[cols]

            .sort_values(

                "Health_Score"

            )

            .head(10)

        )

        print("\n")

        print("=" * 70)

        print("HEALTH SCORE COMPLETED")

        print("=" * 70)

        return df


if __name__ == "__main__":

    health = CampaignHealthScore()

    health.generate_report()