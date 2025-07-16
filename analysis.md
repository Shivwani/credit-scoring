# 📊 Credit Score Analysis Report

## Score Distribution

| Score Range | Wallet Count |
|-------------|---------------|
| (0, 100] | 3480 |
| (100, 200] | 12 |
| (200, 300] | 2 |
| (300, 400] | 0 |
| (400, 500] | 1 |
| (500, 600] | 0 |
| (600, 700] | 0 |
| (700, 800] | 0 |
| (800, 900] | 0 |
| (900, 1000] | 1 |

![Score Distribution](score_distribution.png)

## 🥇 Top 5 Wallets (High Scores)

These wallets demonstrate consistent and responsible behavior based on features like repay ratio, asset diversity, and minimal liquidations.

| wallet                                     |   deposit_count |   borrow_count |   repay_count |   liquidation_count |   borrow_usd |   repay_usd |   repay_ratio |   asset_diversity |   activity_span_days |    score |
|:-------------------------------------------|----------------:|---------------:|--------------:|--------------------:|-------------:|------------:|--------------:|------------------:|---------------------:|---------:|
| 0x01b8f7ef9c12841ca94ee6652f0d5e9646a1168f |             110 |              1 |            65 |                   0 |  8.0093e+09  | 4.2128e+09  |     0.525989  |                 5 |                   99 | 1000     |
| 0x031c7807637ecec27d158bd4156c954e682a2f54 |              26 |              3 |            59 |                   0 |  4.12709e+11 | 4.16165e+11 |     1.00837   |                 4 |                   30 |  455.577 |
| 0x0168459886bd2aa322c18ed0b209887095afcacb |               4 |              1 |            14 |                   0 |  2.98328e+21 | 3.08964e+21 |     1.03565   |                 4 |                   50 |  218.744 |
| 0x01cb1826cd50f7f15626a1283ae812ad0a273388 |              94 |              8 |            61 |                   0 |  9.55362e+10 | 5.55462e+09 |     0.0581415 |                 5 |                   64 |  217.343 |
| 0x02e07cc7e01b1ca69c0a6de55bfd9b99a8f0af3a |              20 |              2 |            19 |                   0 |  2.91023e+10 | 2.93626e+10 |     1.00894   |                 5 |                   86 |  199.436 |

## 🚨 Bottom 5 Wallets (Low Scores)

These wallets are flagged for risky behavior like high liquidation rates, poor repay history, or abrupt activity.

| wallet                                     |   deposit_count |   borrow_count |   repay_count |   liquidation_count |       borrow_usd |   repay_usd |   repay_ratio |   asset_diversity |   activity_span_days |   score |
|:-------------------------------------------|----------------:|---------------:|--------------:|--------------------:|-----------------:|------------:|--------------:|------------------:|---------------------:|--------:|
| 0x04288d0b8bc6298a7cc26f367f42932d71c79d9a |              11 |              9 |             0 |                  11 |      4.17002e+20 |           0 |             0 |                 6 |                   97 | 0       |
| 0x051ba1cf67593ea9e697a1039c549cc94660c4b2 |               9 |              8 |             0 |                   7 |      4.5061e+21  |           0 |             0 |                 4 |                   23 | 2.21877 |
| 0x012fefa16a3baad884834385a0988378852d00bc |               2 |              1 |             0 |                   4 |      1.12792e+07 |           0 |             0 |                 3 |                   51 | 3.55575 |
| 0x02bcb5d5a59ec3350ec2bed6c7ffcd5d566d9574 |               6 |              4 |             0 |                   4 |      3.4221e+08  |           0 |             0 |                 5 |                   46 | 3.79364 |
| 0x003be39433bde975b12411fbc3025d49d813a84f |               0 |              1 |             0 |                   3 | 732132           |           0 |             0 |                 2 |                   33 | 4.02123 |

## Summary Observations

- The scoring model captures a clear behavioral signal.
- Low scoring wallets tend to lack repayment behavior or face frequent liquidations.
- High scoring wallets show long-term participation and diversified usage.
