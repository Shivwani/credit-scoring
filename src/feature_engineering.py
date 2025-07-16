import pandas as pd
from collections import defaultdict
from datetime import datetime

def build_features(raw_data):
    df = pd.DataFrame(raw_data)

    df['wallet'] = df['userWallet']
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df['action_type'] = df['action'].str.lower()

    # Group by wallet
    grouped = df.groupby('wallet')

    features = pd.DataFrame()
    features['deposit_count'] = grouped.apply(lambda x: (x['action_type'] == 'deposit').sum())
    features['borrow_count'] = grouped.apply(lambda x: (x['action_type'] == 'borrow').sum())
    features['repay_count'] = grouped.apply(lambda x: (x['action_type'] == 'repay').sum())
    features['liquidation_count'] = grouped.apply(lambda x: (x['action_type'] == 'liquidationcall').sum())

    # Total borrowed and repaid
    def sum_usd(action_type, x):
        mask = x['action_type'] == action_type
        amounts = x.loc[mask, 'actionData'].apply(lambda a: float(a.get('amount', 0)) * float(a.get('assetPriceUSD', 1)))
        return amounts.sum()

    features['borrow_usd'] = grouped.apply(lambda x: sum_usd('borrow', x))
    features['repay_usd'] = grouped.apply(lambda x: sum_usd('repay', x))

    # Repay ratio
    features['repay_ratio'] = features['repay_usd'] / (features['borrow_usd'] + 1e-6)

    # Asset diversity
    features['asset_diversity'] = grouped['actionData'].apply(lambda x: x.apply(lambda a: a.get('assetSymbol')).nunique())

    # Activity span (days between first and last tx)
    features['activity_span_days'] = grouped['timestamp'].apply(lambda x: (x.max() - x.min()).days + 1)

    features.reset_index(inplace=True)
    return features