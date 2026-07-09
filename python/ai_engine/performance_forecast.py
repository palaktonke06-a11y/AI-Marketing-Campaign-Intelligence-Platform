"""
=========================================================
PERFORMANCE FORECAST
AI Marketing Campaign Intelligence Platform
=========================================================
"""

import os
import pandas as pd
from sklearn.linear_model import LinearRegression


class PerformanceForecast:

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

    def train_models(self):

        X = self.df[["Budget"]]

        self.revenue_model = LinearRegression()
        self.revenue_model.fit(X, self.df["Revenue"])

        self.roi_model = LinearRegression()
        self.roi_model.fit(X, self.df["ROI"])

        self.roas_model = LinearRegression()
        self.roas_model.fit(X, self.df["ROAS"])

        self.conversion_model = LinearRegression()
        self.conversion_model.fit(X, self.df["Conversion_Rate"])

    # ---------------------------------------------------------

    def forecast(self, budget):

        revenue = self.revenue_model.predict([[budget]])[0]
        roi = self.roi_model.predict([[budget]])[0]
        roas = self.roas_model.predict([[budget]])[0]
        conversion = self.conversion_model.predict([[budget]])[0]

        return {

            "Forecast Budget": round(budget, 2),

            "Expected Revenue": round(revenue, 2),

            "Expected ROI": round(roi, 2),

            "Expected ROAS": round(roas, 2),

            "Expected Conversion Rate": round(conversion, 2)

        }

    # ---------------------------------------------------------

    def scenario_analysis(self):

        avg_budget = self.df["Budget"].mean()

        scenarios = [

            avg_budget * 0.75,

            avg_budget,

            avg_budget * 1.25,

            avg_budget * 1.50

        ]

        results = []

        for budget in scenarios:

            results.append(

                self.forecast(budget)

            )

        return pd.DataFrame(results)

    # ---------------------------------------------------------

    def generate_report(self):

        self.train_models()

        report = self.scenario_analysis()

        print("\n")
        print("=" * 70)
        print("PERFORMANCE FORECAST")
        print("=" * 70)

        print("\nCurrent Average Budget :",
              round(self.df["Budget"].mean(), 2))

        print("Current Average Revenue :",
              round(self.df["Revenue"].mean(), 2))

        print("Current Average ROI :",
              round(self.df["ROI"].mean(), 2))

        print("\n")

        print(report)

        best = report.sort_values(
            "Expected Revenue",
            ascending=False
        ).iloc[0]

        print("\n")

        print("=" * 70)
        print("BEST FORECAST")
        print("=" * 70)

        print("Recommended Budget :", best["Forecast Budget"])
        print("Expected Revenue :", best["Expected Revenue"])
        print("Expected ROI :", best["Expected ROI"])
        print("Expected ROAS :", best["Expected ROAS"])
        print("Expected Conversion Rate :",
              best["Expected Conversion Rate"])

        print("\n")

        print("=" * 70)
        print("FORECAST COMPLETED")
        print("=" * 70)

        return report


if __name__ == "__main__":

    forecast = PerformanceForecast()

    forecast.generate_report()