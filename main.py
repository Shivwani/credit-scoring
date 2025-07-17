import json
import pandas as pd
import joblib
from src.feature_engineering import build_features

# Load the trained XGBoost model
model = joblib.load("models/credit_scoring_model.pkl")  # Adjust path

if __name__ == "__main__":
    # Load wallet JSON data
    with open("data/user-wallet-transactions.json") as f:
        wallets = json.load(f)

    # Build features
    features_df = build_features(wallets)

    # Save features to CSV for model training
    features_df.to_csv("engineered_features.csv", index=False)
    print("Feature engineering complete. Output saved to engineered_features.csv")


    """# Filter numeric columns only (XGBoost cannot handle strings/objects)
    X = features_df.select_dtypes(include=["number"])

    # Predict using the model
    raw_scores = model.predict(X)

    # Optionally stretch/scale scores to [0, 1000]
    scores = (raw_scores - raw_scores.min()) / (raw_scores.max() - raw_scores.min()) * 1000
    features_df["credit_score"] = scores.clip(0, 1000).astype(int)

    # Save to CSV
    features_df.to_csv("wallet_scores.csv", index=False)
    print("Scoring complete. Output saved to wallet_scores.csv")"""
