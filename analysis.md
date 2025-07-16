# Credit Score Analysis Report

## Score Distribution

| Score Range | Wallet Count |
|-------------|---------------|
| (0, 100] | 0 |
| (100, 200] | 2304 |
| (200, 300] | 772 |
| (300, 400] | 346 |
| (400, 500] | 67 |
| (500, 600] | 8 |
| (600, 700] | 0 |
| (700, 800] | 0 |
| (800, 900] | 0 |
| (900, 1000] | 0 |

![Score Distribution](score_distribution.png)

## Behavior of Low-Scoring Wallets (0–300)

- Frequent borrow actions with little or no repayment
- Liquidation events are common
- Limited asset diversity (often 1–2 assets)
- May be bots or one-time exploitative interactions
- Inactive or abrupt transaction history

## Behavior of High-Scoring Wallets (700–1000)

- High repay-to-borrow ratios
- Active participation in both deposits and repayments
- Low or zero liquidation events
- Longer activity spans with diverse assets
- Consistent and responsible on-chain behavior

## Summary Observations

- The scoring system effectively distinguishes responsible vs. risky wallets
- Behavior aligns with intuitive financial trustworthiness
- Could be enhanced further by integrating ML models or multiple protocols

## Example Top 5 Wallets

- 0x0476f3ee277eb20568ee2369b337f3ce55bc558a
- 0x005f16f017aa933bb41965b52848ceb8ee48b171
- 0x05c18ffc1c74cb67cb26bb5222aaf3355b74bbc3
- 0x04ee10fd378f7cad5ac5751d7cd0f42b13ee3b76
- 0x04d9f6ecd792e48a09fa5dc2138baed8e628a7e5

## Example Bottom 5 Wallets

- 0x05faaeec0c95c706fca67b25cbbfb21a783a0a34
- 0x0020c5222a24e4a96b720c06b803fb8d34adc0af
- 0x040b97d0bb1de0b75b3a55b7307288df69817cd2
- 0x0413d439285764e6469c06af90a2dcdc68a0ffca
- 0x03fde9f49e46f4b0518a26bfc8bd29569dbc40c2