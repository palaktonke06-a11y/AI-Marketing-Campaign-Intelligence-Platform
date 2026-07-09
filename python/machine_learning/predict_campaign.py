from predictive_model import PredictiveModel


class CampaignPredictor:

    def __init__(self):
        self.model = PredictiveModel()

    def predict(self, campaign_data):

        result = self.model.predict(campaign_data)

        print("\n==============================")
        print("CAMPAIGN PREDICTION RESULT")
        print("==============================")
        print("Status:", result["status"])
        print("Success Probability:", result["success_probability"], "%")
        print("==============================\n")

        return result


if __name__ == "__main__":

    sample = {
        "Campaign_ID": 1,
        "Campaign_Name": "Test Campaign",
        "Campaign_Type": "Social",
        "Campaign_Objective": "Sales",
        "Product_ID": 101,
        "Marketing_Channel": "Instagram",
        "Industry": "Retail",
        "Target_Audience": "Young Adults",
        "Funnel_Stage": "Conversion",
        "Creative_Type": "Video",
        "Device_Target": "Mobile",
        "Region_Target": "North",
        "Bid_Strategy": "Maximize Conversions",
        "Budget": 50000,
        "Budget_Category": "Medium",
        "Campaign_Duration": 30,
        "Start_Date": "2026-01-01",
        "End_Date": "2026-01-30",
        "Campaign_Status": "Active",
        "AI_Campaign_Score": 85,
        "Success_Probability": 0,
        "Risk_Level": "Low",
        "Priority": "High",
        "Expected_ROI": 120,
        "Estimated_Revenue": 200000,
        "Expected_Conversions": 300,
        "Target_CPA": 50,
        "Target_ROAS": 3,
        "Audience_Size": 10000,
        "Optimization_Score": 80,
        "ROI": 120,
        "ROAS": 3.5,
        "Conversion_Rate": 4
    }

    predictor = CampaignPredictor()
    predictor.predict(sample)