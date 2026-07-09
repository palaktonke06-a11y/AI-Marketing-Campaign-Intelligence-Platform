"""
Generate Location Dimension Table
"""

import os
import logging
import pandas as pd

from config import OUTPUT_PATH

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s : %(message)s"
)

logger = logging.getLogger(__name__)


LOCATIONS = [

    ("Bhopal","Madhya Pradesh","Central"),
    ("Indore","Madhya Pradesh","Central"),
    ("Jabalpur","Madhya Pradesh","Central"),
    ("Mumbai","Maharashtra","West"),
    ("Pune","Maharashtra","West"),
    ("Nagpur","Maharashtra","West"),
    ("Delhi","Delhi","North"),
    ("Noida","Uttar Pradesh","North"),
    ("Lucknow","Uttar Pradesh","North"),
    ("Jaipur","Rajasthan","North"),
    ("Ahmedabad","Gujarat","West"),
    ("Surat","Gujarat","West"),
    ("Bengaluru","Karnataka","South"),
    ("Mysuru","Karnataka","South"),
    ("Hyderabad","Telangana","South"),
    ("Chennai","Tamil Nadu","South"),
    ("Coimbatore","Tamil Nadu","South"),
    ("Kochi","Kerala","South"),
    ("Kolkata","West Bengal","East"),
    ("Bhubaneswar","Odisha","East")

]


def generate_locations():

    logger.info("Generating Locations...")

    rows = []

    for idx, location in enumerate(LOCATIONS, start=1):

        city, state, region = location

        rows.append({

            "Location_ID": idx,
            "City": city,
            "State": state,
            "Region": region,
            "Country": "India"

        })

    df = pd.DataFrame(rows)

    os.makedirs(OUTPUT_PATH, exist_ok=True)

    df.to_csv(
        os.path.join(OUTPUT_PATH, "locations.csv"),
        index=False
    )

    logger.info("locations.csv saved successfully.")
    logger.info(f"{len(df)} locations generated successfully.")

    return df


if __name__ == "__main__":
    generate_locations()