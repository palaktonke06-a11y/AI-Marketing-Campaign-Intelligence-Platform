"""
=========================================================
MARKETING STRATEGY SIMULATOR
AI Marketing Campaign Intelligence Platform
=========================================================
"""

import os
import pandas as pd


class MarketingStrategySimulator:

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

    def simulate_budget_increase(self):

        df = self.df.copy()

        df["New_Budget"] = (df["Budget"] * 1.20).round(2)
        df["Expected_Revenue"] = (df["Revenue"] * 1.15).round(2)
        df["Expected_ROI"] = (
            ((df["Expected_Revenue"] - df["Spend"]) / df["Spend"]) * 100
        ).round(2)

        return df

    # ---------------------------------------------------------

    def simulate_budget_decrease(self):

        df = self.df.copy()

        df["New_Budget"] = (df["Budget"] * 0.80).round(2)
        df["Expected_Revenue"] = (df["Revenue"] * 0.90).round(2)
        df["Expected_ROI"] = (
            ((df["Expected_Revenue"] - df["Spend"]) / df["Spend"]) * 100
        ).round(2)

        return df

    # ---------------------------------------------------------

    def simulate_channel_change(self):

        df = self.df.copy()

        best_channel = (
            df.groupby("Marketing_Channel")["Revenue"]
            .mean()
            .idxmax()
        )

        df["Suggested_Channel"] = best_channel
        df["Expected_Revenue"] = (df["Revenue"] * 1.10).round(2)

        return df

    # ---------------------------------------------------------

    def compare_strategies(self):

        increase = self.simulate_budget_increase()
        decrease = self.simulate_budget_decrease()
        channel = self.simulate_channel_change()

        summary = pd.DataFrame({

            "Strategy": [
                "Increase Budget",
                "Decrease Budget",
                "Best Marketing Channel"
            ],

            "Average Revenue": [
                round(increase["Expected_Revenue"].mean(), 2),
                round(decrease["Expected_Revenue"].mean(), 2),
                round(channel["Expected_Revenue"].mean(), 2)
            ],

            "Average ROI": [
                round(increase["Expected_ROI"].mean(), 2),
                round(decrease["Expected_ROI"].mean(), 2),
                round(self.df["ROI"].mean(), 2)
            ]

        })

        return summary

    # ---------------------------------------------------------

    def generate_report(self):

        print("\n")
        print("=" * 70)
        print("MARKETING STRATEGY SIMULATOR")
        print("=" * 70)

        print("\nCurrent Average Revenue :",
              round(self.df["Revenue"].mean(), 2))

        print("Current Average ROI :",
              round(self.df["ROI"].mean(), 2))

        print("\n")

        print("=" * 70)
        print("SIMULATION RESULTS")
        print("=" * 70)

        print(self.compare_strategies())

        print("\n")

        best = self.compare_strategies().sort_values(
            "Average Revenue",
            ascending=False
        ).iloc[0]

        print("=" * 70)
        print("BEST STRATEGY")
        print("=" * 70)

        print("Recommended Strategy :", best["Strategy"])
        print("Expected Average Revenue :", best["Average Revenue"])
        print("Expected ROI :", best["Average ROI"])

        print("\n")

        print("=" * 70)
        print("STRATEGY SIMULATION COMPLETED")
        print("=" * 70)


if __name__ == "__main__":

    simulator = MarketingStrategySimulator()

    simulator.generate_report()