# credit-scoring/src/train_model.py

import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


# Load aggregated features with pseudo-labels (score from your current logic)
features_df = pd.read_csv("data/engineered_features_with_scores.csv")  # make sure this exists

# Split features and target
X = features_df.drop(columns=['wallet', 'score'])
y = features_df['score']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = RandomForestRegressor(n_estimators=100, max_depth=6, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE:", rmse)
print("R2 Score:", r2_score(y_test, y_pred))

# Save model
joblib.dump(model, "models/credit_scoring_model.pkl")
print("Model saved to models/credit_scoring_model.pkl")


