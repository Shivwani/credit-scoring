import pandas as pd
import numpy as np

def compute_score(features_df: pd.DataFrame) -> pd.DataFrame:
    # Normalize features to 0–1 scale
    def normalize(col):
        return (col - col.min()) / (col.max() - col.min() + 1e-8)

    features_df['repay_ratio_norm'] = normalize(features_df['repay_ratio'])
    features_df['deposit_count_norm'] = normalize(features_df['deposit_count'])
    features_df['asset_diversity_norm'] = normalize(features_df['asset_diversity'])
    features_df['activity_span_days_norm'] = normalize(features_df['activity_span_days'])

    # Liquidation is risky → inverse normalized score
    features_df['liquidation_count_norm'] = 1 - normalize(features_df['liquidation_count'])

    # Weighted scoring formula (feel free to tweak weights)
    features_df['score'] = (
        0.35 * features_df['repay_ratio_norm'] +
        0.20 * features_df['deposit_count_norm'] +
        0.15 * features_df['asset_diversity_norm'] +
        0.15 * features_df['activity_span_days_norm'] +
        0.15 * features_df['liquidation_count_norm']
    )

    # Scale score to 0–1000
    features_df['score'] = (features_df['score'] * 1000).clip(0, 1000)

    return features_df[['wallet', 'score']]
