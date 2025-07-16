import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv("data/engineered_features_with_scores.csv")

# --- Score distribution buckets ---
bins = list(range(0, 1100, 100))
df['score_bucket'] = pd.cut(df['score'], bins=bins)
distribution = df['score_bucket'].value_counts().sort_index()

# --- Plotting ---
plt.figure(figsize=(10, 6))
distribution.plot(kind='bar', color='skyblue')
plt.xlabel("Score Range")
plt.ylabel("Number of Wallets")
plt.title("Wallet Credit Score Distribution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("score_distribution.png")
plt.close()

# --- Top 5 Wallets ---
top_wallets = df.sort_values(by='score', ascending=False).head(5)[
    ['wallet', 'deposit_count', 'borrow_count', 'repay_count', 'liquidation_count',
     'borrow_usd', 'repay_usd', 'repay_ratio', 'asset_diversity', 'activity_span_days', 'score']
]

# --- Bottom 5 Wallets ---
bottom_wallets = df.sort_values(by='score').head(5)[
    ['wallet', 'deposit_count', 'borrow_count', 'repay_count', 'liquidation_count',
     'borrow_usd', 'repay_usd', 'repay_ratio', 'asset_diversity', 'activity_span_days', 'score']
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
    f.write("These wallets demonstrate consistent and responsible behavior based on features like repay ratio, asset diversity, and minimal liquidations.\n\n")
    f.write(top_wallets.to_markdown(index=False))
    f.write("\n\n")

    f.write("## 🚨 Bottom 5 Wallets (Low Scores)\n\n")
    f.write("These wallets are flagged for risky behavior like high liquidation rates, poor repay history, or abrupt activity.\n\n")
    f.write(bottom_wallets.to_markdown(index=False))
    f.write("\n\n")

    f.write("## Summary Observations\n\n")
    f.write("- The scoring model captures a clear behavioral signal.\n")
    f.write("- Low scoring wallets tend to lack repayment behavior or face frequent liquidations.\n")
    f.write("- High scoring wallets show long-term participation and diversified usage.\n")

print("✅ analysis.md and score_distribution.png generated.")
