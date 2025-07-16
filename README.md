# 🏦 DeFi Wallet Credit Scoring System

This project implements a machine learning-based credit scoring engine for wallets interacting with the Aave V2 protocol on the Polygon network. Given raw user transaction data in JSON format, the system assigns a **credit score between 0 and 1000** to each wallet, reflecting the wallet’s reliability and responsible DeFi usage.

---

## 📌 Problem Statement

You are provided with 100K+ transaction records from the Aave V2 protocol. Each record captures actions such as `deposit`, `borrow`, `repay`, `redeemunderlying`, and `liquidationcall`.

Your goal is to:
- Engineer meaningful behavioral features.
- Assign credit scores to each wallet using a robust ML model.
- Make the pipeline reproducible, explainable, and extensible.

---

## 🔧 Project Structure

credit-scoring/
├── data/
│ └── user-wallet-transactions.json
│ └── engineered_features_with_scores.csv
├── models/
│ └── credit_scoring_model.pkl
├── src/
│ ├── feature_engineering.py
│ ├── heuristic_score.py
│ ├── score_model.py
│ └── train_model.py
├── main.py
├── generate_training_data.py
├── analysis.md
├── README.md
└── requirements.txt


---

## 🛠️ How It Works

### 1. Feature Engineering
- Parses raw transaction logs.
- Aggregates behavior per wallet:
  - `deposit_count`, `borrow_count`, `repay_count`
  - `repay_ratio`, `liquidation_count`
  - `asset_diversity`, `activity_span_days`
- Output: DataFrame with 9+ behavioral features per wallet.

📄 File: `src/feature_engineering.py`

---

### 2. Pseudo-Labeling with Heuristic Scoring
- A rule-based logic assigns an initial score to each wallet.
- Score combines good actions (deposit/repay) and penalizes liquidations.

📄 File: `src/heuristic_score.py`

---

### 3. Model Training
- Uses XGBoost regression model.
- Trained on heuristic scores (`engineered_features_with_scores.csv`) as pseudo-labels.
- Tuned using `GridSearchCV` for optimal hyperparameters.

📄 File: `src/train_model.py`

---

### 4. Inference Pipeline
- Accepts a new JSON file with wallet transactions.
- Applies the same feature engineering.
- Predicts a credit score between 0 and 1000 for each wallet.

📄 File: `main.py`

---

## 📈 Evaluation

- Final model: **XGBoost Regressor**
- Metrics:
  - **RMSE:** 21.65
  - **R² Score:** 0.72
- Indicates good predictive power for behavioral credit scoring.

---

## 📊 Score Analysis

See [`analysis.md`](analysis.md) for:
- Score distribution histogram
- Behavioral patterns of high vs. low scoring wallets
- Summary observations and top/bottom wallet examples

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/credit-scoring.git
   cd credit-scoring

2. Install dependencies:
   
   pip install -r requirements.txt
   
3. Generate training data with heuristic scores:
   
   python generate_training_data.py
   
4. Train the ML model:
   
   python src/train_model.py

5. Score wallets using:
   
   python main.py

