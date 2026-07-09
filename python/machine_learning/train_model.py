"""
=========================================================
AI MARKETING CAMPAIGN INTELLIGENCE PLATFORM
Machine Learning - Model Training
=========================================================
"""

import os
import joblib
import pandas as pd

from preprocess import preprocess

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

MODEL_PATH = os.path.join(
    ROOT_DIR,
    "python",
    "models"
)

os.makedirs(MODEL_PATH, exist_ok=True)


class CampaignTrainer:

    def __init__(self):

        self.model = RandomForestClassifier(

            n_estimators=300,

            max_depth=12,

            min_samples_leaf=2,

            min_samples_split=5,

            random_state=42,

            n_jobs=-1

        )

    # ---------------------------------------------------

    def train(self):

        X_train, X_test, y_train, y_test = preprocess()

        self.model.fit(

            X_train,

            y_train

        )

        prediction = self.model.predict(

            X_test

        )

        probability = self.model.predict_proba(

            X_test

        )

        accuracy = accuracy_score(

            y_test,

            prediction

        )

        precision = precision_score(

            y_test,

            prediction

        )

        recall = recall_score(

            y_test,

            prediction

        )

        f1 = f1_score(

            y_test,

            prediction

        )

        print("\n")

        print("=" * 70)

        print("MODEL TRAINING COMPLETED")

        print("=" * 70)

        print(f"Accuracy  : {accuracy:.4f}")

        print(f"Precision : {precision:.4f}")

        print(f"Recall    : {recall:.4f}")

        print(f"F1 Score  : {f1:.4f}")

        print("\n")

        print(classification_report(

            y_test,

            prediction

        ))

        print("\n")

        print(confusion_matrix(

            y_test,

            prediction

        ))

        joblib.dump(

            self.model,

            os.path.join(

                MODEL_PATH,

                "campaign_success_model.pkl"

            )

        )

        feature_importance = pd.DataFrame({

            "Feature": X_train.columns,

            "Importance": self.model.feature_importances_

        })

        feature_importance = feature_importance.sort_values(

            by="Importance",

            ascending=False

        )

        feature_importance.to_csv(

            os.path.join(

                MODEL_PATH,

                "feature_importance.csv"

            ),

            index=False

        )

        print("\n")

        print("Model Saved Successfully")

        print("Feature Importance Saved")

        print("=" * 70)

        return self.model


def train_model():

    trainer = CampaignTrainer()

    return trainer.train()


if __name__ == "__main__":

    train_model()
