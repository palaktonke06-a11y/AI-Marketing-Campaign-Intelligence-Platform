"""
Generate Customer Journey Table
--------------------------------
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


def generate_customer_journey():

    logger.info("Generating Customer Journey...")

    customers = pd.read_csv(
        os.path.join(
            OUTPUT_PATH,
            "customers.csv"
        )
    )

    campaigns = pd.read_csv(
        os.path.join(
            OUTPUT_PATH,
            "campaigns.csv"
        )
    )

    journey = []

    journey_id = 1

    stages = [
        "Awareness",
        "Interest",
        "Consideration",
        "Purchase",
        "Retention"
    ]

    devices = [
        "Android",
        "iPhone",
        "Desktop",
        "Laptop",
        "Tablet"
    ]

    for _, customer in customers.iterrows():

        campaign = campaigns.sample(1).iloc[0]

        stage = random.choice(stages)

        session_duration = random.randint(20, 900)

        pages_visited = random.randint(1, 20)

        bounced = random.choice(["Yes", "No"])

        converted = random.choice(["Yes", "No"])

        journey.append({

            "Journey_ID": journey_id,
            "Customer_ID": customer["Customer_ID"],
            "Campaign_ID": campaign["Campaign_ID"],

            "Journey_Date": random.choice(
                pd.date_range(
                    "2023-01-01",
                    "2025-12-31"
                )
            ),

            "Journey_Stage": stage,

            "Device": random.choice(
                devices
            ),

            "Pages_Visited": pages_visited,

            "Session_Duration": session_duration,

            "Bounce": bounced,

            "Converted": converted

        })

        journey_id += 1

    # ======================================================
    # Convert to DataFrame
    # ======================================================

    df = pd.DataFrame(journey)

    logger.info(
        f"{len(df)} customer journey records generated successfully."
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
        "customer_journey.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    logger.info(
        "customer_journey.csv saved successfully."
    )

    return df


# ==========================================================
# Run Independently
# ==========================================================

if __name__ == "__main__":
    generate_customer_journey()