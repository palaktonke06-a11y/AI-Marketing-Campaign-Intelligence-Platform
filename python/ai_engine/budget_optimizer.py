"""
=========================================================
BUDGET OPTIMIZER
AI Marketing Campaign Intelligence Platform
=========================================================
"""

import os
import pandas as pd


class BudgetOptimizer:

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

    def calculate_efficiency(self):

        df = self.df.copy()

        df["Budget_Efficiency"] = (
            df["Revenue"] / df["Budget"]
        ).round(2)

        df["Profit"] = (
            df["Revenue"] - df["Spend"]
        ).round(2)

        return df

    # ---------------------------------------------------------

    def budget_action(self, row):

        if row["Budget_Efficiency"] >= 4:
            return "Increase Budget"

        elif row["Budget_Efficiency"] >= 2:
            return "Maintain Budget"

        elif row["Budget_Efficiency"] >= 1:
            return "Optimize Campaign"

        else:
            return "Reduce Budget"

    # ---------------------------------------------------------

    def recommended_budget(self, row):

        current = row["Budget"]

        action = row["Recommendation"]

        if action == "Increase Budget":
            return round(current * 1.20, 2)

        elif action == "Maintain Budget":
            return round(current, 2)

        elif action == "Optimize Campaign":
            return round(current * 0.90, 2)

        else:
            return round(current * 0.75, 2)

    # ---------------------------------------------------------

    def optimize(self):

        df = self.calculate_efficiency()

        df["Recommendation"] = df.apply(
            self.budget_action,
            axis=1
        )

        df["Recommended_Budget"] = df.apply(
            self.recommended_budget,
            axis=1
        )

        df["Budget_Change"] = (
            df["Recommended_Budget"] - df["Budget"]
        ).round(2)

        return df

    # ---------------------------------------------------------

    def summary(self):

        df = self.optimize()

        print("\n")
        print("=" * 70)
        print("AI BUDGET OPTIMIZER")
        print("=" * 70)

        print("\nAverage Budget :",
              round(df["Budget"].mean(), 2))

        print("Average Revenue :",
              round(df["Revenue"].mean(), 2))

        print("Average Spend :",
              round(df["Spend"].mean(), 2))

        print("Average Profit :",
              round(df["Profit"].mean(), 2))

        print("\nRecommendation Distribution\n")

        print(
            df["Recommendation"]
            .value_counts()
        )

        print("\nTop Budget Performing Campaigns\n")

        cols = [

            "Campaign_ID",

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

        print(

            df[cols]

            .sort_values(

                "Budget_Efficiency",

                ascending=False

            )

            .head(10)

        )

        print("\nLowest Performing Campaigns\n")

        print(

            df[cols]

            .sort_values(

                "Budget_Efficiency"

            )

            .head(10)

        )

        print("\n")
        print("=" * 70)
        print("BUDGET OPTIMIZATION COMPLETED")
        print("=" * 70)

        return df


if __name__ == "__main__":

    optimizer = BudgetOptimizer()

    optimizer.summary()