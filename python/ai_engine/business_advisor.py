"""
=========================================================
AI BUSINESS ADVISOR
AI Marketing Campaign Intelligence Platform
=========================================================
"""

import os
import joblib
import pandas as pd


class AIBusinessAdvisor:

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

        self.model_path = os.path.join(
            self.root,
            "python",
            "models",
            "campaign_success_model.pkl"
        )

        self.feature_path = os.path.join(
            self.root,
            "python",
            "models",
            "feature_importance.csv"
        )

        self.model = joblib.load(self.model_path)

        self.df = pd.read_csv(self.data_path)

        self.feature_importance = pd.read_csv(self.feature_path)

    # ---------------------------------------------------

    def dataset_summary(self):

        total_campaigns = len(self.df)

        successful = self.df["Campaign_Success"].sum()

        unsuccessful = total_campaigns - successful

        success_rate = round(
            successful / total_campaigns * 100,
            2
        )

        return {

            "Total Campaigns": total_campaigns,

            "Successful": int(successful),

            "Unsuccessful": int(unsuccessful),

            "Success Rate": success_rate

        }

    # ---------------------------------------------------

    def budget_analysis(self):

        avg_budget = round(

            self.df["Budget"].mean(),

            2

        )

        avg_revenue = round(

            self.df["Revenue"].mean(),

            2

        )

        avg_spend = round(

            self.df["Spend"].mean(),

            2

        )

        roi = round(

            self.df["ROI"].mean(),

            2

        )

        roas = round(

            self.df["ROAS"].mean(),

            2

        )

        return {

            "Average Budget": avg_budget,

            "Average Spend": avg_spend,

            "Average Revenue": avg_revenue,

            "Average ROI": roi,

            "Average ROAS": roas

        }

    # ---------------------------------------------------

    def top_channels(self):

        channel = (

            self.df

            .groupby("Marketing_Channel")["Revenue"]

            .mean()

            .sort_values(ascending=False)

        )

        return channel.head(5)

    # ---------------------------------------------------

    def top_regions(self):

        region = (

            self.df

            .groupby("Region_Target")["Revenue"]

            .mean()

            .sort_values(ascending=False)

        )

        return region.head(5)

    # ---------------------------------------------------

    def top_campaign_types(self):

        campaign = (

            self.df

            .groupby("Campaign_Type")["Revenue"]

            .mean()

            .sort_values(ascending=False)

        )

        return campaign.head(5)

    # ---------------------------------------------------

    def important_features(self):

        return self.feature_importance.head(10)

    # ---------------------------------------------------

    def recommendations(self):

        recommendations = []

        if self.df["ROI"].mean() < 100:

            recommendations.append(

                "Increase campaign optimization to improve ROI."

            )

        if self.df["ROAS"].mean() < 3:

            recommendations.append(

                "Improve targeting to increase ROAS."

            )

        if self.df["CTR"].mean() < 5:

            recommendations.append(

                "Creative quality should be improved."

            )

        if self.df["Conversion_Rate"].mean() < 4:

            recommendations.append(

                "Landing page optimization is recommended."

            )

        if self.df["Bounce_Rate"].mean() > 45:

            recommendations.append(

                "Reduce bounce rate by improving user experience."

            )

        if len(recommendations) == 0:

            recommendations.append(

                "Campaign performance is healthy."

            )

        return recommendations

    # ---------------------------------------------------

    def generate_report(self):

        print("\n")

        print("=" * 70)

        print("AI BUSINESS ADVISOR")

        print("=" * 70)

        print("\nDATASET SUMMARY\n")

        print(self.dataset_summary())

        print("\n")

        print("=" * 70)

        print("BUDGET INSIGHTS")

        print("=" * 70)

        print(self.budget_analysis())

        print("\n")

        print("=" * 70)

        print("TOP MARKETING CHANNELS")

        print("=" * 70)

        print(self.top_channels())

        print("\n")

        print("=" * 70)

        print("TOP REGIONS")

        print("=" * 70)

        print(self.top_regions())

        print("\n")

        print("=" * 70)

        print("TOP CAMPAIGN TYPES")

        print("=" * 70)

        print(self.top_campaign_types())

        print("\n")

        print("=" * 70)

        print("MOST IMPORTANT ML FEATURES")

        print("=" * 70)

        print(self.important_features())

        print("\n")

        print("=" * 70)

        print("AI RECOMMENDATIONS")

        print("=" * 70)

        for i, rec in enumerate(self.recommendations(), 1):

            print(f"{i}. {rec}")

        print("\n")

        print("=" * 70)

        print("BUSINESS ADVISOR COMPLETED")

        print("=" * 70)


if __name__ == "__main__":

    advisor = AIBusinessAdvisor()

    advisor.generate_report()