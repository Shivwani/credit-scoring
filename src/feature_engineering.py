import pandas as pd
from collections import defaultdict

DECIMALS = {
    "USDC": 6,
    "USDT": 6,
    "DAI": 18,
    "WMATIC": 18,
    "ETH": 18,
}

STABLECOINS = {"USDC", "USDT", "DAI"}

def normalize_amount(symbol, raw_amount):
    decimals = DECIMALS.get(symbol.upper(), 18)
    return raw_amount / (10 ** decimals)

def build_features(data):
    wallets = defaultdict(list)

    # Group transactions by wallet address
    for tx in data:
        address = tx.get("userWallet") or tx.get("actionData", {}).get("userId")
        if address:
            wallets[address].append(tx)

    wallet_features = []

    for address, txs in wallets.items():
        tx_count = len(txs)
        total_volume = 0
        stablecoin_volume = 0
        asset_symbols = set()

        # Action counters
        borrow_count = 0
        repay_count = 0
        supply_count = 0
        redeem_count = 0
        liquidation_count = 0

        for tx in txs:
            action_data = tx.get("actionData", {})
            symbol = action_data.get("assetSymbol", "").upper()
            asset_symbols.add(symbol)

            # Volume handling
            try:
                raw_amount = float(action_data.get("amount", 0))
                amount = normalize_amount(symbol, raw_amount)
            except Exception:
                amount = 0

            total_volume += amount

            if symbol in STABLECOINS:
                stablecoin_volume += amount

            # Detect action types
            action = tx.get("action", "").lower()
            if action == "borrow":
                borrow_count += 1
            elif action == "repay":
                repay_count += 1
            elif action in ["supply", "deposit"]:
                supply_count += 1
            elif action == "redeemunderlying":
                redeem_count += 1
            elif action == "liquidationcall":
                liquidation_count += 1

        # Ratios
        stablecoin_tx_ratio = stablecoin_volume / total_volume if total_volume > 0 else 0
        borrow_ratio = borrow_count / tx_count if tx_count > 0 else 0
        repay_ratio = repay_count / tx_count if tx_count > 0 else 0
        supply_ratio = supply_count / tx_count if tx_count > 0 else 0
        avg_tx_size = total_volume / tx_count if tx_count > 0 else 0


        wallet_features.append({
            "wallet_address": address,
            "transaction_count": tx_count,
            "total_volume_eth": total_volume,
            "average_transaction_size": avg_tx_size,
            "stablecoin_volume_ratio": stablecoin_tx_ratio,
            "borrow_ratio": borrow_ratio,
            "repay_ratio": repay_ratio,
            "supply_ratio": supply_ratio,
            "unique_tokens_transacted": len(asset_symbols),
        })

    return pd.DataFrame(wallet_features)
