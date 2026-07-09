"""
==========================================================
AI MARKETING CAMPAIGN INTELLIGENCE PLATFORM
Machine Learning - Preprocessing Module (FINAL FIX)
==========================================================
"""

import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# -------------------------------------------------------
# PATHS
# -------------------------------------------------------

ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

RAW_DATA = os.path.join(
    ROOT_DIR,
    "python",
    "data_generation",
    "data",
    "raw"
)

PROCESSED_DATA = os.path.join(
    ROOT_DIR,
    "python",
    "data_generation",
    "data",
    "processed"
)

MODEL_PATH = os.path.join(
    ROOT_DIR,
    "python",
    "models"
)

os.makedirs(PROCESSED_DATA, exist_ok=True)
os.makedirs(MODEL_PATH, exist_ok=True)


# -------------------------------------------------------
# PREPROCESSOR CLASS
# -------------------------------------------------------

class CampaignPreprocessor:

    def __init__(self):

        self.encoders = {}

    # ---------------------------------------------------

    def load_dataset(self):

        campaigns = pd.read_csv(
            os.path.join(RAW_DATA, "campaigns.csv")
        )

        performance = pd.read_csv(
            os.path.join(RAW_DATA, "campaign_performance.csv")
        )

        return campaigns, performance

    # ---------------------------------------------------

    def merge_dataset(self):

        campaigns, performance = self.load_dataset()

        drop_cols = [
            "Impressions",
            "CTR",
            "Clicks",
            "Conversion_Rate",
            "Conversions",
            "CPC",
            "CPM",
            "Spend",
            "Revenue"
        ]

        campaigns = campaigns.drop(columns=drop_cols, errors="ignore")

        df = campaigns.merge(
            performance,
            on="Campaign_ID",
            how="inner"
        )

        return df

    # ---------------------------------------------------

    def clean_dataset(self, df):

        df = df.copy()
        df.drop_duplicates(inplace=True)
        df.fillna(0, inplace=True)

        if "Performance_ID" in df.columns:
            df.drop(columns=["Performance_ID"], inplace=True)

        return df

    # ---------------------------------------------------

    def create_target(self, df):

        df["Campaign_Success"] = (
            (
                df["ROI"] >= df["ROI"].median()
            ) |
            (
                df["ROAS"] >= df["ROAS"].median()
            ) |
            (
                df["Conversion_Rate"] >= df["Conversion_Rate"].median()
            )
        ).astype(int)

        return df

    # ---------------------------------------------------

    def encode_data(self, df):

        categorical = df.select_dtypes(include=["object" , "string"]).columns

        for col in categorical:

            le = LabelEncoder()

            df[col] = le.fit_transform(df[col].astype(str))

            self.encoders[col] = le

        return df

    # ---------------------------------------------------

    def feature_selection(self, df):

        remove_cols = [
            "Campaign_Name",
            "Start_Date",
            "End_Date",
            "ROI",
            "ROAS",
            "Conversion_Rate"
        ]

        df.drop(columns=remove_cols, errors="ignore", inplace=True)

        return df

    # ---------------------------------------------------

    def save_processed_dataset(self, train_df, dashboard_df):

        train_df.to_csv(
            os.path.join(PROCESSED_DATA, "campaign_training_dataset.csv"),
            index=False
        )

        dashboard_df.to_csv(
            os.path.join(PROCESSED_DATA, "campaign_dashboard_dataset.csv"),
            index=False
        )

    # ---------------------------------------------------

    def save_encoders(self):

        joblib.dump(
            self.encoders,
            os.path.join(MODEL_PATH, "encoders.pkl")
        )

    # ---------------------------------------------------

    def save_feature_columns(self, X):

        joblib.dump(
            X.columns.tolist(),
            os.path.join(MODEL_PATH, "feature_columns.pkl")
        )

    # ---------------------------------------------------

    def preprocess(self):

        df = self.merge_dataset()
        df = self.clean_dataset(df)
        df = self.create_target(df)

        # dashboard dataset (AI + Streamlit)
        dashboard_df = df.copy()

        # ML dataset
        train_df = df.copy()
        train_df = self.feature_selection(train_df)
        train_df = self.encode_data(train_df)

        # save datasets
        self.save_processed_dataset(train_df, dashboard_df)

        # encoders
        self.save_encoders()

        # split
        X = train_df.drop(columns=["Campaign_Success"])
        y = train_df["Campaign_Success"]

        # feature columns save
        self.save_feature_columns(X)

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

        print("\nCampaign Success Distribution:")
        print(train_df["Campaign_Success"].value_counts())

        return X_train, X_test, y_train, y_test


# -------------------------------------------------------
# PUBLIC FUNCTION
# -------------------------------------------------------

def preprocess():

    processor = CampaignPreprocessor()
    return processor.preprocess()


# -------------------------------------------------------
# MAIN
# -------------------------------------------------------

if __name__ == "__main__":

    X_train, X_test, y_train, y_test = preprocess()

    print("=" * 60)
    print("PREPROCESSING COMPLETED SUCCESSFULLY")
    print("=" * 60)
    print("Train shape:", X_train.shape)
    print("Test shape :", X_test.shape)
    print("=" * 60)