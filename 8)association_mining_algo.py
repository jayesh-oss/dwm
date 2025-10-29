
# EXPERIMENT NO: 08
# AIM: Implementation of an Association Rule Mining Algorithm (Apriori) using Python

# Import required libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# -----------------------------
# Step 1: Create / Load Dataset
# -----------------------------
# Example market basket dataset
dataset = [
    ['milk', 'bread', 'butter'],
    ['bread', 'jam', 'milk'],
    ['milk', 'bread'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter', 'jam'],
    ['bread', 'jam']
]

# Convert list of transactions into a DataFrame
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
print("Dataset Loaded and One-Hot Encoded:")
print(df.head())

# -----------------------------
# Step 2: Apply Apriori Algorithm
# -----------------------------
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)
print("\nFrequent Itemsets:")
print(frequent_itemsets)

# -----------------------------
# Step 3: Generate Association Rules
# -----------------------------
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)
print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# -----------------------------
# Step 4: Sort and Display Top Rules
# -----------------------------
top_rules = rules.sort_values(by='lift', ascending=False)
print("\nTop 5 Rules Sorted by Lift:")
print(top_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(5))

# -----------------------------
# Step 5: Save Results
# -----------------------------
rules.to_csv("association_rules_output.csv", index=False)
print("\nRules saved as 'association_rules_output.csv'")
