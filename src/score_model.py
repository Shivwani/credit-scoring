import numpy as np

def compute_heuristic_score(wallet):
    # Raw features
    tx_count = wallet.get("transaction_count", 0)
    total_volume = wallet.get("total_volume_eth", 0.0)
    avg_tx_size = wallet.get("average_transaction_size", 0.0)
    stablecoin_ratio = wallet.get("stablecoin_volume_ratio", 0.0)
    unique_tokens = wallet.get("unique_tokens_transacted", 0)

    # Extract actions and compute ratios
    deposit = wallet.get("deposit", 0.0)
    borrow = wallet.get("borrow", 0.0)
    repay = wallet.get("repay", 0.0)
    redeem = wallet.get("redeemunderlying", 0.0)
    liquidation = wallet.get("liquidationcall", 0.0)

    total_actions = deposit + borrow + repay + redeem + liquidation
    borrow_ratio = borrow / total_actions if total_actions else 0
    repay_ratio = repay / total_actions if total_actions else 0
    supply_ratio = deposit / total_actions if total_actions else 0

    # Normalize
    norm_tx_count = min(tx_count / 300, 1.0)
    norm_volume = min(total_volume / 500, 1.0)
    norm_avg_tx_size = min(avg_tx_size / 50, 1.0)
    norm_stablecoin_ratio = min(stablecoin_ratio, 1.0)
    norm_borrow_ratio = min(borrow_ratio, 1.0)
    norm_repay_ratio = min(repay_ratio, 1.0)
    norm_supply_ratio = min(supply_ratio, 1.0)
    norm_unique_tokens = min(unique_tokens / 20, 1.0)

    # Weighted raw score
    raw_score = (
        0.15 * norm_tx_count +
        0.20 * norm_volume +
        0.10 * norm_avg_tx_size +
        0.10 * norm_stablecoin_ratio +
        0.10 * norm_borrow_ratio +
        0.10 * norm_repay_ratio +
        0.15 * norm_supply_ratio +
        0.10 * norm_unique_tokens
    ) * 100

    # Apply stretching
    stretched_score = int(raw_score*10)
    return min(stretched_score, 1000)


def compute_score(df):
    df["credit_score"] = df.apply(lambda row: compute_heuristic_score(row.to_dict()), axis=1)
    return df
