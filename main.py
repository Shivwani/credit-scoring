import json
import pandas as pd
from src.feature_engineering import build_features
from src.score_model import compute_score

if __name__ == "__main__":
    # Load wallet JSON data
    with open("data/user-wallet-transactions.json") as f:
        wallets = json.load(f)

    # Build features
    features_df = build_features(wallets)

    # Compute credit scores
    scored_df = compute_score(features_df)

    # Save to CSV
    scored_df.to_csv("wallet_scores.csv", index=False)
    print("Scoring complete. Output saved to wallet_scores.csv")
