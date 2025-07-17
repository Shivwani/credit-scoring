import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Load data ---
data_path = "wallet_scores.csv"
if not os.path.exists(data_path):
    raise FileNotFoundError(f"File not found: {data_path}")
df = pd.read_csv(data_path)

# --- Rename score column for convenience ---
df['score'] = df['credit_score'].clip(0, 1000).round().astype(int)

# --- Score distribution buckets ---
bins = list(range(0, 1101, 100))
df['score_bucket'] = pd.cut(df['score'], bins=bins, right=False)
distribution = df['score_bucket'].value_counts().sort_index()

# --- Plotting ---
plt.figure(figsize=(10, 6))
distribution.plot(kind='bar', color='cornflowerblue')
plt.xlabel("Score Range")
plt.ylabel("Number of Wallets")
plt.title("Wallet Credit Score Distribution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("score_distribution.png")
plt.close()

# --- Top 5 Wallets ---
top_wallets = df.sort_values(by='score', ascending=False).head(5)[
    ['wallet_address', 'transaction_count', 'total_volume_eth', 'average_transaction_size',
     'borrow_ratio', 'repay_ratio', 'supply_ratio', 'unique_tokens_transacted', 'score']
]

# --- Bottom 5 Wallets ---
bottom_wallets = df.sort_values(by='score').head(5)[
    ['wallet_address', 'transaction_count', 'total_volume_eth', 'average_transaction_size',
     'borrow_ratio', 'repay_ratio', 'supply_ratio', 'unique_tokens_transacted', 'score']
]

# --- Write analysis.md ---
with open("analysis.md", "w", encoding="utf-8") as f:
    f.write("# 📊 Credit Score Analysis Report\n\n")

    f.write("## Score Distribution\n\n")
    f.write("| Score Range | Wallet Count |\n")
    f.write("|-------------|---------------|\n")
    for bucket, count in distribution.items():
        f.write(f"| {bucket} | {count} |\n")

    f.write("\n![Score Distribution](score_distribution.png)\n\n")

    f.write("## 🥇 Top 5 Wallets (High Scores)\n\n")
    f.write("These wallets demonstrate strong on-chain behavior across multiple indicators such as repayment ratio and consistent usage.\n\n")
    f.write(top_wallets.to_markdown(index=False))
    f.write("\n\n")

    f.write("## 🚨 Bottom 5 Wallets (Low Scores)\n\n")
    f.write("These wallets may exhibit weaker creditworthiness due to indicators like low repay ratios or minimal activity.\n\n")
    f.write(bottom_wallets.to_markdown(index=False))
    f.write("\n\n")

    f.write("## Summary Observations\n\n")
    f.write("- The score is distributed across the full 0–1000 range, indicating model expressiveness.\n")
    f.write("- High scoring wallets tend to be more active and better at repaying borrowed amounts.\n")
    f.write("- Low scoring wallets often transact infrequently or show signs of high borrow-to-repay imbalance.\n")

print("✅ analysis.md and score_distribution.png generated.")
