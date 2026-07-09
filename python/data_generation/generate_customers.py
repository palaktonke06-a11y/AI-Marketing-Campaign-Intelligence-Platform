"""
Generate Customer Dimension Table
---------------------------------
Creates realistic customer data for the AI Marketing
Campaign Intelligence Platform.
"""

import os
import random
import logging

import pandas as pd

from config import (
    OUTPUT_PATH,
    fake,
    NUM_CUSTOMERS,
    NUM_LOCATIONS
)


# ==========================================================
# Logging Configuration
# ==========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s : %(message)s"
)

logger = logging.getLogger(__name__)


# ==========================================================
# Customer Master Lists
# ==========================================================

OCCUPATIONS = [
    "Student",
    "Software Engineer",
    "Doctor",
    "Teacher",
    "Business Owner",
    "Marketing Manager",
    "Sales Executive",
    "Chartered Accountant",
    "Designer",
    "Freelancer",
    "Government Employee",
    "Data Analyst",
    "HR Manager",
    "Consultant"
]

INCOME_LEVELS = [
    "Low",
    "Lower Middle",
    "Middle",
    "Upper Middle",
    "High"
]

DEVICE_TYPES = [
    "Android",
    "iPhone",
    "Laptop",
    "Desktop",
    "Tablet"
]

LOYALTY_LEVELS = [
    "Bronze",
    "Silver",
    "Gold",
    "Platinum"
]

CUSTOMER_SEGMENTS = [
    "New",
    "Returning",
    "Premium",
    "Student",
    "Corporate"
]

PREFERRED_CHANNELS = [
    "Google Search Ads",
    "Google Display Ads",
    "Facebook Ads",
    "Instagram Ads",
    "YouTube Ads",
    "LinkedIn Ads",
    "Email Marketing",
    "Affiliate Marketing"
]

# ==========================================================
# Helper Function
# ==========================================================

def get_age_group(age: int) -> str:
    """Return age group based on customer age."""

    if age < 18:
        return "Under 18"
    elif age <= 25:
        return "18-25"
    elif age <= 35:
        return "26-35"
    elif age <= 45:
        return "36-45"
    elif age <= 60:
        return "46-60"
    else:
        return "60+"


# ==========================================================
# Main Function
# ==========================================================

def generate_customers(num_customers: int = NUM_CUSTOMERS) -> pd.DataFrame:
    """Generate realistic customer data."""

    logger.info("Generating Customers...")

    customers = []

    for customer_id in range(1, num_customers + 1):

        gender = random.choice(["Male", "Female"])

        if gender == "Male":
            first_name = fake.first_name_male()
        else:
            first_name = fake.first_name_female()

        last_name = fake.last_name()

        age = random.randint(18, 60)

        age_group = get_age_group(age)

        email = (
            f"{first_name.lower()}."
            f"{last_name.lower()}"
            f"{customer_id}@gmail.com"
        )

        phone = fake.phone_number()

        occupation = random.choice(OCCUPATIONS)

        income = random.choices(
            INCOME_LEVELS,
            weights=[10, 20, 35, 25, 10],
            k=1
        )[0]

        device = random.choices(
            DEVICE_TYPES,
            weights=[45, 20, 20, 10, 5],
            k=1
        )[0]

        segment = random.choices(
            CUSTOMER_SEGMENTS,
            weights=[25, 35, 15, 15, 10],
            k=1
        )[0]

        loyalty = random.choices(
            LOYALTY_LEVELS,
            weights=[40, 30, 20, 10],
            k=1
        )[0]

        preferred_channel = random.choice(PREFERRED_CHANNELS)

        registration_date = fake.date_between(
            start_date="-3y",
            end_date="today"
        )

        is_active = random.choices(
            ["Yes", "No"],
            weights=[85, 15],
            k=1
        )[0]

        total_orders = random.randint(1, 40)

        total_spend = total_orders * random.randint(800, 45000)

        location_id = random.randint(1, NUM_LOCATIONS)

        customers.append({

            "Customer_ID": customer_id,
            "First_Name": first_name,
            "Last_Name": last_name,
            "Gender": gender,
            "Age": age,
            "Age_Group": age_group,
            "Email": email,
            "Phone": phone,
            "Location_ID": location_id,
            "Occupation": occupation,
            "Income_Level": income,
            "Device_Type": device,
            "Customer_Segment": segment,
            "Loyalty_Level": loyalty,
            "Preferred_Channel": preferred_channel,
            "Registration_Date": registration_date,
            "Is_Active": is_active,
            "Total_Orders": total_orders,
            "Total_Spend": total_spend

        })

    # ======================================================
    # Convert to DataFrame
    # ======================================================

    df = pd.DataFrame(customers)

    logger.info(f"{len(df)} customers generated successfully.")

    # ======================================================
    # Save CSV
    # ======================================================

    os.makedirs(OUTPUT_PATH, exist_ok=True)

    output_file = os.path.join(
        OUTPUT_PATH,
        "customers.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    logger.info("customers.csv saved successfully.")

    return df


# ==========================================================
# Run Independently
# ==========================================================

if __name__ == "__main__":
    generate_customers()