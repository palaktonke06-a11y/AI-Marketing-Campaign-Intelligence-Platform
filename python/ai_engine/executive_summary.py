"""
=========================================================
EXECUTIVE SUMMARY
AI Marketing Campaign Intelligence Platform
=========================================================
"""

import os
import pandas as pd


class ExecutiveSummary:

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

    def generate_kpis(self):

        total_campaigns = len(self.df)

        total_budget = round(self.df["Budget"].sum(), 2)

        total_spend = round(self.df["Spend"].sum(), 2)

        total_revenue = round(self.df["Revenue"].sum(), 2)

        total_profit = round(total_revenue - total_spend, 2)

        avg_roi = round(self.df["ROI"].mean(), 2)

        avg_roas = round(self.df["ROAS"].mean(), 2)

        avg_ctr = round(self.df["CTR"].mean(), 2)

        avg_conversion = round(
            self.df["Conversion_Rate"].mean(), 2
        )

        success_rate = round(
            self.df["Campaign_Success"].mean() * 100,
            2
        )

        return {
            "Total Campaigns": total_campaigns,
            "Total Budget": total_budget,
            "Total Spend": total_spend,
            "Total Revenue": total_revenue,
            "Total Profit": total_profit,
            "Average ROI": avg_roi,
            "Average ROAS": avg_roas,
            "Average CTR": avg_ctr,
            "Average Conversion Rate": avg_conversion,
            "Campaign Success Rate": success_rate
        }

    # ---------------------------------------------------------

    def best_channel(self):

        channel = (

            self.df

            .groupby("Marketing_Channel")["Revenue"]

            .mean()

            .sort_values(ascending=False)

        )

        return channel.head(5)

    # ---------------------------------------------------------

    def best_region(self):

        region = (

            self.df

            .groupby("Region_Target")["Revenue"]

            .mean()

            .sort_values(ascending=False)

        )

        return region.head(5)

    # ---------------------------------------------------------

    def best_campaign_type(self):

        campaign = (

            self.df

            .groupby("Campaign_Type")["Revenue"]

            .mean()

            .sort_values(ascending=False)

        )

        return campaign.head(5)

    # ---------------------------------------------------------

    def generate_report(self):

        print("\n")

        print("=" * 75)

        print("EXECUTIVE SUMMARY")

        print("=" * 75)

        print("\nKEY PERFORMANCE INDICATORS\n")

        for key, value in self.generate_kpis().items():

            print(f"{key:<30}: {value}")

        print("\n")

        print("=" * 75)
        print("TOP MARKETING CHANNELS")
        print("=" * 75)

        print(self.best_channel())

        print("\n")

        print("=" * 75)
        print("TOP REGIONS")
        print("=" * 75)

        print(self.best_region())

        print("\n")

        print("=" * 75)
        print("TOP CAMPAIGN TYPES")
        print("=" * 75)

        print(self.best_campaign_type())

        print("\n")

        print("=" * 75)
        print("EXECUTIVE INSIGHTS")
        print("=" * 75)

        if self.df["ROI"].mean() > 100:
            print("✔ ROI performance is strong.")
        else:
            print("✖ ROI requires optimization.")

        if self.df["ROAS"].mean() > 3:
            print("✔ ROAS is healthy.")
        else:
            print("✖ Improve ad targeting.")

        if self.df["CTR"].mean() > 5:
            print("✔ Ad creatives are performing well.")
        else:
            print("✖ Improve creatives and copy.")

        if self.df["Conversion_Rate"].mean() > 4:
            print("✔ Conversion performance is good.")
        else:
            print("✖ Landing page optimization recommended.")

        print("\n")

        print("=" * 75)
        print("EXECUTIVE SUMMARY COMPLETED")
        print("=" * 75)


if __name__ == "__main__":

    summary = ExecutiveSummary()

    summary.generate_report()