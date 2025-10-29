
# EXPERIMENT NO: 05
# AIM: Implement filling missing values, removing outliers, and performing association rule mining

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# -----------------------------
# PART 1 — Filling Missing Values
# -----------------------------

print("=== PART 1: Filling Missing Values ===")

# Load dataset (replace 'breast-cancer.csv' with actual path)
try:
    df1 = pd.read_csv("breast-cancer.csv")
    print("Original Data with Missing Values:")
    print(df1.head())

    # Fill missing numeric values with mean, categorical with mode
    df1 = df1.fillna(df1.mean(numeric_only=True))
    df1 = df1.fillna(df1.mode().iloc[0])

    # Save cleaned data
    df1.to_csv("breast-cancer_cleaned.csv", index=False)
    print("\nCleaned Data Saved as 'breast-cancer_cleaned.csv'")
except FileNotFoundError:
    print("File 'breast-cancer.csv' not found. Please place the dataset in the same directory.")

# -----------------------------
# PART 2 — Removing Outliers
# -----------------------------

print("\n=== PART 2: Removing Outliers ===")

# Load dataset (replace 'diabetes.csv' with actual path)
try:
    df2 = pd.read_csv("diabetes.csv")
    print("Original Data:")
    print(df2.describe())

    # Calculate IQR
    Q1 = df2.quantile(0.25)
    Q3 = df2.quantile(0.75)
    IQR = Q3 - Q1

    # Remove outliers
    filtered_df = df2[~((df2 < (Q1 - 1.5 * IQR)) | (df2 > (Q3 + 1.5 * IQR))).any(axis=1)]
    filtered_df.to_csv("diabetes_no_outliers.csv", index=False)

    print("\nOutliers removed. Cleaned data saved as 'diabetes_no_outliers.csv'")
except FileNotFoundError:
    print("File 'diabetes.csv' not found. Please place the dataset in the same directory.")

# -----------------------------
# PART 3 — Association Rule Mining
# -----------------------------

print("\n=== PART 3: Association Rule Mining (Apriori) ===")

# Load dataset (replace 'supermarket.csv' with actual path)
try:
    data = pd.read_csv("supermarket.csv")
    print("Dataset Loaded for Association Rule Mining.")

    # Convert categorical data to one-hot encoding
    transactions = pd.get_dummies(data)

    # Generate frequent itemsets using Apriori algorithm
    frequent_itemsets = apriori(transactions, min_support=0.1, use_colnames=True)

    # Generate association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.9)

    # Display top 10 rules
    print("\nTop 10 Association Rules:")
    print(rules.head(10))

    # Save rules to CSV
    rules.to_csv("association_rules.csv", index=False)
    print("\nRules saved as 'association_rules.csv'")
except FileNotFoundError:
    print("File 'supermarket.csv' not found. Please place the dataset in the same directory.")
