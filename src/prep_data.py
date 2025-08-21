import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("data/heart.csv")

# Basic cleaning (drop duplicates, reset index)
df = df.drop_duplicates().reset_index(drop=True)

# Features (X) and target (y)
X = df.drop("target", axis=1)
y = df["target"]

# Scale numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert back to DataFrame for saving
X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)

# Combine scaled features with target
processed = pd.concat([X_scaled_df, y], axis=1)

# Save processed dataset
processed.to_csv("data/processed_heart.csv", index=False)

print("✅ Data processed and saved to data/processed_heart.csv")
