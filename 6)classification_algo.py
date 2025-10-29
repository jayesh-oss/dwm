
# EXPERIMENT NO: 06
# AIM: Implementation of a Classification Algorithm (Decision Tree) using Python

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Load dataset
# -----------------------------
# Using the Iris dataset for demonstration
from sklearn.datasets import load_iris
data = load_iris()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

print("Dataset Loaded Successfully")
print("Features:", X.columns.tolist())
print("Target classes:", data.target_names)

# -----------------------------
# Step 2: Split into train and test sets
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("\nData split into training and testing sets")

# -----------------------------
# Step 3: Train Decision Tree Classifier
# -----------------------------
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf.fit(X_train, y_train)
print("\nDecision Tree Model Trained Successfully")

# -----------------------------
# Step 4: Make Predictions
# -----------------------------
y_pred = clf.predict(X_test)

# -----------------------------
# Step 5: Evaluate Model
# -----------------------------
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=data.target_names))

# -----------------------------
# Step 6: Visualize Decision Tree (Optional)
# -----------------------------
plt.figure(figsize=(12,8))
plot_tree(clf, filled=True, feature_names=data.feature_names, class_names=data.target_names)
plt.title("Decision Tree Visualization")
plt.show()
