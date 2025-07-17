
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

```
credit-scoring/
├── data/
│   ├── user-wallet-transactions.json
│   └── engineered_features_with_scores.csv
├── models/
│   └── credit_scoring_model.pkl
├── src/
│   ├── feature_engineering.py
│   ├── score_model.py
│   ├── train_model.py
├── main.py
├── generate_training_data.py
├── generate_analysis.py
├── analysis.md
├── score_distribution.png
├── README.md
└── requirements.txt

```

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

📄 File: `src/score_model.py`

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

### 5. Score Analysis
- Generates `analysis.md` with:
  - Score distribution insights
  - Summary statistics
  - Top and bottom scoring wallets
- Also saves a score distribution plot (`score_distribution.png`).

📄 File: `src/generate_analysis.py`

---

## 📈 Evaluation

- Final model: **XGBoost Regressor**
- Best Hyperparameters:
  - `n_estimators`: 200
  - `max_depth`: 3
  - `learning_rate`: 0.1
  - `subsample`: 0.8
  - `colsample_bytree`: 0.7
- Metrics:
  - **RMSE:** 4.26
  - **R² Score:** 0.9995
- Indicates excellent predictive power for behavioral credit scoring.

---

## ▶️ How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Shivwani/credit-scoring.git
   cd credit-scoring

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Generate training data with heuristic scores:

   ```bash
   python generate_training_data.py
   ```

4. Train the ML model:

   ```bash
   python src/train_model.py
   ```

5. Score wallets using:

   ```bash
   python main.py
   ```

6. Generate score analysis:

   ```bash
   python src/generate_analysis.py
   ```

---

## 📊 Score Analysis

See [`analysis.md`](analysis.md) for:

* Score distribution histogram
* Behavioral patterns of high vs. low scoring wallets
* Summary observations and top/bottom wallet examples
* Visual chart: `score_distribution.png`

---


