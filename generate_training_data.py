# generate_training_data.py

from src.feature_engineering import build_features
from src.heuristic_score import compute_heuristic_score  # We'll create this
import json
import pandas as pd

if __name__ == "__main__":
    with open("data/user-wallet-transactions.json") as f:
        raw_data = json.load(f)

    features_df = build_features(raw_data)

    # Apply your current rule-based scoring logic
    features_df = compute_heuristic_score(features_df)

    # Save for model training
    features_df.to_csv("data/engineered_features_with_scores.csv", index=False)
    print("Saved training dataset with pseudo-labels to data/engineered_features_with_scores.csv")


print("Shape of features_df:", features_df.shape)
print("Columns in features_df:", features_df.columns)
