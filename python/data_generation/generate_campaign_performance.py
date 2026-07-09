"""
Generate Campaign Performance Fact Table
----------------------------------------
"""

import os
import random
import logging

import pandas as pd

from config import OUTPUT_PATH

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s : %(message)s"
)

logger = logging.getLogger(__name__)


def generate_campaign_performance():

    logger.info("Generating Campaign Performance...")

    campaigns = pd.read_csv(
        os.path.join(
            OUTPUT_PATH,
            "campaigns.csv"
        )
    )

    performance = []

    performance_id = 1

    for _, row in campaigns.iterrows():

        impressions = row["Impressions"]

        clicks = row["Clicks"]

        conversions = row["Conversions"]

        spend = row["Spend"]

        revenue = row["Revenue"]

        ctr = round(
            clicks / max(impressions, 1) * 100,
            2
        )

        conversion_rate = round(
            conversions / max(clicks, 1) * 100,
            2
        )

        cpc = round(
            spend / max(clicks, 1),
            2
        )

        cpm = round(
            spend / max(impressions, 1) * 1000,
            2
        )

        roas = round(
            revenue / max(spend, 1),
            2
        )

        roi = round(
            (revenue - spend) / max(spend, 1) * 100,
            2
        )

        engagement_rate = round(
            random.uniform(2, 18),
            2
        )

        bounce_rate = round(
            random.uniform(20, 70),
            2
        )

        avg_session_duration = random.randint(
            30,
            500
        )

        performance.append({

            "Performance_ID": performance_id,
            "Campaign_ID": row["Campaign_ID"],

            "Impressions": impressions,
            "Clicks": clicks,
            "Conversions": conversions,

            "CTR": ctr,
            "Conversion_Rate": conversion_rate,

            "Spend": spend,
            "Revenue": revenue,

            "CPC": cpc,
            "CPM": cpm,

            "ROAS": roas,
            "ROI": roi,

            "Engagement_Rate": engagement_rate,
            "Bounce_Rate": bounce_rate,
            "Avg_Session_Duration": avg_session_duration

        })

        performance_id += 1

    # ======================================================
    # Convert to DataFrame
    # ======================================================

    df = pd.DataFrame(performance)

    logger.info(
        f"{len(df)} campaign performance records generated successfully."
    )

    # ======================================================
    # Save CSV
    # ======================================================

    os.makedirs(
        OUTPUT_PATH,
        exist_ok=True
    )

    output_file = os.path.join(
        OUTPUT_PATH,
        "campaign_performance.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    logger.info(
        "campaign_performance.csv saved successfully."
    )

    return df


# ==========================================================
# Run Independently
# ==========================================================

if __name__ == "__main__":
    generate_campaign_performance()