"""
=========================================================
SMART ALERTS
AI Marketing Campaign Intelligence Platform
=========================================================
"""

import os
import pandas as pd


class SmartAlerts:

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

    def generate_alerts(self):

        alerts = []

        for _, row in self.df.iterrows():

            campaign = row["Campaign_Name"]

            if row["ROI"] < 50:

                alerts.append({
                    "Campaign": campaign,
                    "Priority": "High",
                    "Alert": "Very Low ROI",
                    "Recommendation": "Optimize campaign or pause immediately."
                })

            if row["ROAS"] < 2:

                alerts.append({
                    "Campaign": campaign,
                    "Priority": "High",
                    "Alert": "Low ROAS",
                    "Recommendation": "Improve audience targeting."
                })

            if row["CTR"] < 2:

                alerts.append({
                    "Campaign": campaign,
                    "Priority": "Medium",
                    "Alert": "Low CTR",
                    "Recommendation": "Improve creatives and ad copy."
                })

            if row["Conversion_Rate"] < 2:

                alerts.append({
                    "Campaign": campaign,
                    "Priority": "Medium",
                    "Alert": "Low Conversion Rate",
                    "Recommendation": "Optimize landing page."
                })

            if row["Bounce_Rate"] > 60:

                alerts.append({
                    "Campaign": campaign,
                    "Priority": "Medium",
                    "Alert": "High Bounce Rate",
                    "Recommendation": "Improve website experience."
                })

            if row["Spend"] > row["Budget"]:

                alerts.append({
                    "Campaign": campaign,
                    "Priority": "Critical",
                    "Alert": "Budget Overspent",
                    "Recommendation": "Reduce spending immediately."
                })

        return pd.DataFrame(alerts)

    # ---------------------------------------------------------

    def summary(self):

        alerts = self.generate_alerts()

        print("\n")
        print("=" * 75)
        print("SMART ALERTS")
        print("=" * 75)

        if alerts.empty:

            print("\nNo critical alerts detected.\n")

        else:

            print("\nTotal Alerts :", len(alerts))

            print("\nPriority Distribution\n")

            print(
                alerts["Priority"]
                .value_counts()
            )

            print("\nLatest Alerts\n")

            print(alerts.head(20))

        print("\n")
        print("=" * 75)
        print("SMART ALERTS COMPLETED")
        print("=" * 75)

        return alerts


if __name__ == "__main__":

    smart = SmartAlerts()

    smart.summary()