import pandas as pd
import os
from config import OUTPUT_PATH

def generate_channels():

    channels = [
        {
            "Channel_ID": 1,
            "Channel_Name": "Google Search Ads",
            "Platform": "Google",
            "Campaign_Type": "Search",
            "Avg_CPC": 25,
            "Avg_CTR": 6.5
        },
        {
            "Channel_ID": 2,
            "Channel_Name": "Google Display Ads",
            "Platform": "Google",
            "Campaign_Type": "Display",
            "Avg_CPC": 12,
            "Avg_CTR": 3.4
        },
        {
            "Channel_ID": 3,
            "Channel_Name": "Facebook Ads",
            "Platform": "Meta",
            "Campaign_Type": "Social Media",
            "Avg_CPC": 18,
            "Avg_CTR": 5.2
        },
        {
            "Channel_ID": 4,
            "Channel_Name": "Instagram Ads",
            "Platform": "Meta",
            "Campaign_Type": "Social Media",
            "Avg_CPC": 20,
            "Avg_CTR": 5.9
        },
        {
            "Channel_ID": 5,
            "Channel_Name": "YouTube Ads",
            "Platform": "Google",
            "Campaign_Type": "Video",
            "Avg_CPC": 15,
            "Avg_CTR": 4.1
        },
        {
            "Channel_ID": 6,
            "Channel_Name": "LinkedIn Ads",
            "Platform": "LinkedIn",
            "Campaign_Type": "Professional",
            "Avg_CPC": 40,
            "Avg_CTR": 2.8
        },
        {
            "Channel_ID": 7,
            "Channel_Name": "Email Marketing",
            "Platform": "Email",
            "Campaign_Type": "Email",
            "Avg_CPC": 3,
            "Avg_CTR": 8.5
        },
        {
            "Channel_ID": 8,
            "Channel_Name": "Affiliate Marketing",
            "Platform": "Affiliate",
            "Campaign_Type": "Referral",
            "Avg_CPC": 8,
            "Avg_CTR": 4.7
        }
    ]

    df = pd.DataFrame(channels)

    os.makedirs(OUTPUT_PATH, exist_ok=True)

    df.to_csv(
        os.path.join(OUTPUT_PATH, "channels.csv"),
        index=False
    )

    print("✅ channels.csv generated successfully!")

    return df