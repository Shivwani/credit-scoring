import pandas as pd

def compute_score(df):
    df = df.copy()

    # Normalize features to [0, 1] for scoring
    def norm(col):
        return (col - col.min()) / (col.max() - col.min() + 1e-9)

    df['score'] = (
        norm(df['repay_ratio']) * 0.3 +
        (1 - norm(df['liquidation_count'])) * 0.2 +
        (1 - norm(df['borrow_deposit_ratio'])) * 0.2 +
        norm(df['tx_per_day']) * 0.15 +
        norm(df['unique_assets']) * 0.15
    ) * 1000

    df['score'] = df['score'].clip(0, 1000)
    return df[['wallet', 'score']]


