import os
import joblib
import pandas as pd


ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

MODEL_PATH = os.path.join(ROOT_DIR, "python", "models")


class PredictiveModel:

    def __init__(self):

        self.model = joblib.load(
            os.path.join(MODEL_PATH, "campaign_success_model.pkl")
        )

        self.encoders = joblib.load(
            os.path.join(MODEL_PATH, "encoders.pkl")
        )

    def encode(self, df):

        for col, encoder in self.encoders.items():

            if col in df.columns:

                try:
                    df[col] = encoder.transform(df[col].astype(str))
                except:
                    df[col] = 0

        return df

    def predict(self, input_data):

        df = pd.DataFrame([input_data])

        df = self.encode(df)

        pred = self.model.predict(df)[0]

        prob = self.model.predict_proba(df)[0][1]

        return {
            "prediction": int(pred),
            "status": "Successful" if pred == 1 else "Unsuccessful",
            "success_probability": round(prob * 100, 2)
        }