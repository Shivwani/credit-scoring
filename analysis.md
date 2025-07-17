# 📊 Credit Score Analysis Report

## Score Distribution

| Score Range | Wallet Count |
|-------------|---------------|
| [0, 100) | 880 |
| [100, 200) | 705 |
| [200, 300) | 156 |
| [300, 400) | 53 |
| [400, 500) | 68 |
| [500, 600) | 303 |
| [600, 700) | 481 |
| [700, 800) | 658 |
| [800, 900) | 123 |
| [900, 1000) | 69 |
| [1000, 1100) | 1 |

![Score Distribution](score_distribution.png)

## 🥇 Top 5 Wallets (High Scores)

These wallets demonstrate strong on-chain behavior across multiple indicators such as repayment ratio and consistent usage.

| wallet_address                             |   transaction_count |   total_volume_eth |   average_transaction_size |   borrow_ratio |   repay_ratio |   supply_ratio |   unique_tokens_transacted |   score |
|:-------------------------------------------|--------------------:|-------------------:|---------------------------:|---------------:|--------------:|---------------:|---------------------------:|--------:|
| 0x047a96ef72d7ee6a3f193bdb92e998fb300265df |                 820 |        1.53946e+06 |                  1877.39   |      0.243902  |     0.252439  |       0.218293 |                          8 |    1000 |
| 0x05c18ffc1c74cb67cb26bb5222aaf3355b74bbc3 |                 584 |        2.41923e+06 |                  4142.52   |      0.0462329 |     0.0256849 |       0.561644 |                          9 |     999 |
| 0x00aac20f271c4731591cca07913e994d6f1075c0 |                 633 |    97300           |                   153.712  |      0.1406    |     0.278041  |       0.456556 |                          8 |     998 |
| 0x05404b6f8990a4108150366adb572a870b137edc |                 473 |    71535           |                   151.237  |      0.124736  |     0.150106  |       0.490486 |                          8 |     997 |
| 0x04d9f6ecd792e48a09fa5dc2138baed8e628a7e5 |                1089 |   102353           |                    93.9876 |      0.163453  |     0.267218  |       0.37741  |                          8 |     997 |

## 🚨 Bottom 5 Wallets (Low Scores)

These wallets may exhibit weaker creditworthiness due to indicators like low repay ratios or minimal activity.

| wallet_address                             |   transaction_count |   total_volume_eth |   average_transaction_size |   borrow_ratio |   repay_ratio |   supply_ratio |   unique_tokens_transacted |   score |
|:-------------------------------------------|--------------------:|-------------------:|---------------------------:|---------------:|--------------:|---------------:|---------------------------:|--------:|
| 0x00418b8ea6c6e2d5676f651bf76a368adb845e91 |                   1 |          0.5       |                  0.5       |              0 |             0 |              1 |                          1 |       0 |
| 0x05b02f5f36da0730785f75086d55444239a8089d |                   1 |          0.8       |                  0.8       |              0 |             0 |              1 |                          1 |       0 |
| 0x05c52cd5d423ee6f17334ff54ade74291d89f678 |                   1 |          0.5       |                  0.5       |              0 |             0 |              1 |                          1 |       0 |
| 0x03ffb5f525be3ca2431cb97415c509566bc42b8a |                   1 |          0.1086    |                  0.1086    |              0 |             0 |              1 |                          1 |       1 |
| 0x0466c8e551c53ea1d554ea1dbfd32f154ab7f089 |                   1 |          0.0774721 |                  0.0774721 |              0 |             0 |              1 |                          1 |       1 |

## Summary Observations

- The score is distributed across the full 0–1000 range, indicating model expressiveness.
- High scoring wallets tend to be more active and better at repaying borrowed amounts.
- Low scoring wallets often transact infrequently or show signs of high borrow-to-repay imbalance.
