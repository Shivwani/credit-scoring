# src/heuristic_score.py

def compute_heuristic_score(df):
    # Normalize a few behavior patterns to simulate a score
    df['deposit_score'] = df['deposit_count'] / df['deposit_count'].max()
    df['repay_score'] = df['repay_count'] / (df['borrow_count'] + 1)
    df['liquidation_penalty'] = df['liquidation_count'] / df['liquidation_count'].max()

    # Composite score logic
    df['score'] = (
        0.4 * df['deposit_score'] +
        0.4 * df['repay_score'] -
        0.2 * df['liquidation_penalty']
    )

    # Normalize to 0–1000 scale
    df['score'] = (df['score'] - df['score'].min()) / (df['score'].max() - df['score'].min()) * 1000

    return df
