"""
=========================================================
COMPETITOR BENCHMARK
AI Marketing Campaign Intelligence Platform
=========================================================
"""

import os
import pandas as pd


class CompetitorBenchmark:

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

    def create_market_benchmark(self):

        benchmark = {

            "ROI": self.df["ROI"].median(),

            "ROAS": self.df["ROAS"].median(),

            "CTR": self.df["CTR"].median(),

            "Conversion_Rate": self.df["Conversion_Rate"].median(),

            "CPC": self.df["CPC"].median(),

            "CPM": self.df["CPM"].median(),

            "Engagement_Rate": self.df["Engagement_Rate"].median(),

            "Bounce_Rate": self.df["Bounce_Rate"].median()

        }

        return benchmark

    # ---------------------------------------------------------

    def compare(self):

        benchmark = self.create_market_benchmark()

        report = pd.DataFrame({

            "Metric": [
                "ROI",
                "ROAS",
                "CTR",
                "Conversion Rate",
                "CPC",
                "CPM",
                "Engagement Rate",
                "Bounce Rate"
            ],

            "Your Performance": [

                round(self.df["ROI"].mean(), 2),
                round(self.df["ROAS"].mean(), 2),
                round(self.df["CTR"].mean(), 2),
                round(self.df["Conversion_Rate"].mean(), 2),
                round(self.df["CPC"].mean(), 2),
                round(self.df["CPM"].mean(), 2),
                round(self.df["Engagement_Rate"].mean(), 2),
                round(self.df["Bounce_Rate"].mean(), 2)

            ],

            "Market Benchmark": [

                round(benchmark["ROI"], 2),
                round(benchmark["ROAS"], 2),
                round(benchmark["CTR"], 2),
                round(benchmark["Conversion_Rate"], 2),
                round(benchmark["CPC"], 2),
                round(benchmark["CPM"], 2),
                round(benchmark["Engagement_Rate"], 2),
                round(benchmark["Bounce_Rate"], 2)

            ]

        })

        report["Status"] = report.apply(

            lambda row:
            "Above Market"
            if row["Your Performance"] >= row["Market Benchmark"]
            else "Below Market",

            axis=1

        )

        report["Benchmark Score"] = (
            report["Your Performance"]
            / report["Market Benchmark"] * 100
        ).round(2)

        return report

# ---------------------------------------------------------

    def generate_report(self):

        report = self.compare()

        print("\n")
        print("=" * 75)
        print("COMPETITOR BENCHMARK")
        print("=" * 75)

        print("\n")

        print(report)

        print("\n")

        above = len(

            report[

                report["Status"] == "Above Market"

            ]

        )

        below = len(

            report[

                report["Status"] == "Below Market"

            ]

        )

        print("=" * 75)
        print("SUMMARY")
        print("=" * 75)

        print(f"Metrics Above Market : {above}")
        print(f"Metrics Below Market : {below}")

        if above > below:

            print("\nOverall Performance : Strong")

        elif above == below:

            print("\nOverall Performance : Competitive")

        else:

            print("\nOverall Performance : Needs Improvement")

        print("\n")

        print("=" * 75)
        print("COMPETITOR BENCHMARK COMPLETED")
        print("=" * 75)

        return report


if __name__ == "__main__":

    benchmark = CompetitorBenchmark()

    benchmark.generate_report()