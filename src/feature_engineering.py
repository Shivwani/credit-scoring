import pandas as pd
from collections import defaultdict
from datetime import datetime

def build_features(transactions):
    wallet_data = defaultdict(list)
    
    for tx in transactions:
        wallet = tx['userWallet']
        action = tx['action'].lower()
        timestamp = tx['timestamp']
        action_data = tx.get('actionData', {})

        try:
            amount = float(action_data.get('amount', 0)) / 1e18  # assuming 18 decimals
            asset = action_data.get('assetSymbol', 'UNKNOWN')
        except:
            amount = 0
            asset = 'UNKNOWN'

        wallet_data[wallet].append({
            'action': action,
            'timestamp': timestamp,
            'amount': amount,
            'asset': asset
        })

    feature_rows = []

    for wallet, txs in wallet_data.items():
        df = pd.DataFrame(txs)
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

        features = {
            'wallet': wallet,
            'total_tx_count': len(df),
            'unique_assets': df['asset'].nunique(),
            'active_days': (df['timestamp'].max() - df['timestamp'].min()).days + 1,
            'deposit_total': df[df['action'] == 'deposit']['amount'].sum(),
            'borrow_total': df[df['action'] == 'borrow']['amount'].sum(),
            'repay_total': df[df['action'] == 'repay']['amount'].sum(),
            'redeem_total': df[df['action'] == 'redeemunderlying']['amount'].sum(),
            'liquidation_count': (df['action'] == 'liquidationcall').sum(),
        }

        # Derived metrics
        features['repay_ratio'] = features['repay_total'] / features['borrow_total'] if features['borrow_total'] > 0 else 0
        features['borrow_deposit_ratio'] = features['borrow_total'] / features['deposit_total'] if features['deposit_total'] > 0 else 0
        features['tx_per_day'] = features['total_tx_count'] / features['active_days']

        feature_rows.append(features)

    return pd.DataFrame(feature_rows)