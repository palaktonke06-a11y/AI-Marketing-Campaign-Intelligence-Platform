"""
Generate Campaign Dimension Table
---------------------------------
Creates realistic marketing campaign data for the
AI Marketing Campaign Intelligence Platform.
"""

import os
import random
import logging

import pandas as pd

from config import OUTPUT_PATH, NUM_CAMPAIGNS

from constants import (
    CAMPAIGN_TYPES,
    CAMPAIGN_OBJECTIVES,
    MARKETING_CHANNELS,
    INDUSTRIES,
    TARGET_AUDIENCE,
    CREATIVE_TYPES,
    BID_STRATEGIES,
    DEVICE_TARGETS,
    REGION_TARGETS,
    CAMPAIGN_STATUS
)

from helpers import (
    get_budget_category,
    generate_ai_score,
    generate_success_probability,
    get_risk_level,
    get_priority,
    generate_expected_roi,
    generate_campaign_duration,
    generate_campaign_dates
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s : %(message)s"
)

logger = logging.getLogger(__name__)

def generate_campaign_name(campaign_id, objective):

    objective = objective.replace(" ", "_")

    return f"CMP_{campaign_id:04}_{objective}"


def get_funnel_stage(campaign_type):

    if campaign_type == "Retargeting":
        return "BOFU"

    elif campaign_type == "Lead Generation":
        return "MOFU"

    return "TOFU"


def generate_budget():
    """Generate a realistic campaign budget."""

    return random.randint(50000, 1500000)

# ==========================================================
# Main Function
# ==========================================================

def generate_campaigns():

    logger.info("Generating Campaigns...")

    campaigns = []

    # Load Product IDs
    products = pd.read_csv(
        os.path.join(
            OUTPUT_PATH,
            "products.csv"
        )
    )


    product_ids = products["Product_ID"].tolist()    

    for campaign_id in range(1, NUM_CAMPAIGNS + 1):
        campaign_type = random.choice(CAMPAIGN_TYPES)

        objective = random.choice(CAMPAIGN_OBJECTIVES)

        campaign_name = generate_campaign_name(
            campaign_id,
            objective
        )

        product_id = random.choice(product_ids)

        marketing_channel = random.choice(
            MARKETING_CHANNELS
        )

        industry = random.choice(
            INDUSTRIES
        )

        target_audience = random.choice(
            TARGET_AUDIENCE
        )

        funnel_stage = get_funnel_stage(
            campaign_type
        )

        creative_type = random.choice(
            CREATIVE_TYPES
        )

        device_target = random.choice(
            DEVICE_TARGETS
        )

        region_target = random.choice(
            REGION_TARGETS
        )

        bid_strategy = random.choice(
            BID_STRATEGIES
        )

        budget = generate_budget()

        duration = generate_campaign_duration()

        campaign_status = random.choice(
            CAMPAIGN_STATUS
        )

        start_date, end_date = generate_campaign_dates(
            campaign_status,
            duration
        )

        ai_score = generate_ai_score(
            budget
        )

        success_probability = (
            generate_success_probability(
                ai_score
            )
        )

        risk_level = get_risk_level(
            ai_score
        )

        priority = get_priority(
            ai_score
        )

        budget_category = get_budget_category(
            budget
        )

        expected_roi = generate_expected_roi(
            ai_score
        )
        
        estimated_revenue = int(
            budget * (1 + expected_roi / 100)
        )

        expected_conversions = random.randint(
            100,
            5000
        )

        target_cpa = round(
            budget / expected_conversions,
            2
        )

        target_roas = round(
            estimated_revenue / budget,
            2
        )

        audience_size = random.randint(
            50000,
            5000000
        )

        optimization_score = random.randint(
            60,
            100
        )

        impressions = random.randint(
            50000,
            5000000
        )

        ctr = round(
            random.uniform(0.8, 12.0),
            2
        )

        clicks = int(
            impressions * ctr / 100
        )

        conversion_rate = round(
            random.uniform(1.5, 18.0),
            2
        )

        conversions = int(
            clicks * conversion_rate / 100
        )

        cpc = round(
            budget / max(clicks, 1),
            2
        )

        cpm = round(
            budget / max(impressions, 1) * 1000,
            2
        )

        spend = budget

        revenue = int(
            spend * (1 + expected_roi / 100)
        )

        campaigns.append({

            "Campaign_ID": campaign_id,
            "Campaign_Name": campaign_name,
            "Campaign_Type": campaign_type,
            "Campaign_Objective": objective,

            "Product_ID": product_id,

            "Marketing_Channel": marketing_channel,
            "Industry": industry,
            "Target_Audience": target_audience,

            "Funnel_Stage": funnel_stage,
            "Creative_Type": creative_type,

            "Device_Target": device_target,
            "Region_Target": region_target,

            "Bid_Strategy": bid_strategy,

            "Budget": budget,
            "Budget_Category": budget_category,

            "Campaign_Duration": duration,

            "Start_Date": start_date,
            "End_Date": end_date,

            "Campaign_Status": campaign_status,

            "AI_Campaign_Score": ai_score,
            "Success_Probability": success_probability,
            "Risk_Level": risk_level,
            "Priority": priority,

            "Expected_ROI": expected_roi,
            "Estimated_Revenue": estimated_revenue,

            "Expected_Conversions": expected_conversions,
            "Target_CPA": target_cpa,
            "Target_ROAS": target_roas,

            "Audience_Size": audience_size,
            "Optimization_Score": optimization_score,

            "Impressions": impressions,
            "CTR": ctr,
            "Clicks": clicks,
            "Conversion_Rate": conversion_rate,
            "Conversions": conversions,
            "CPC": cpc,
            "CPM": cpm,
            "Spend": spend,
            "Revenue": revenue

        })

    # ======================================================
    # Convert to DataFrame
    # ======================================================

    df = pd.DataFrame(campaigns)

    logger.info(f"{len(df)} campaigns generated successfully.")

    # ======================================================
    # Save CSV
    # ======================================================

    os.makedirs(OUTPUT_PATH, exist_ok=True)

    output_file = os.path.join(
        OUTPUT_PATH,
        "campaigns.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    logger.info("campaigns.csv saved successfully.")

    return df

# ==========================================================
# Run Independently
# ==========================================================

if __name__ == "__main__":
    generate_campaigns()