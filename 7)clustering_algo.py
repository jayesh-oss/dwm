
# EXPERIMENT NO: 07
# AIM: Implementation of a Clustering Algorithm (K-Means) using Python

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# -----------------------------
# Step 1: Load dataset
# -----------------------------
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
print("Dataset Loaded Successfully")
print("Features:", X.columns.tolist())

# -----------------------------
# Step 2: Preprocessing (Standardize Data)
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# Step 3: Apply K-Means Clustering
# -----------------------------
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)
labels = kmeans.labels_

# -----------------------------
# Step 4: Evaluate Model
# -----------------------------
print("\nCluster Centers (scaled):")
print(kmeans.cluster_centers_)

print("\nInertia (Within-cluster sum of squares):", kmeans.inertia_)
print("Silhouette Score:", silhouette_score(X_scaled, labels))

# -----------------------------
# Step 5: Visualize Clusters
# -----------------------------
plt.figure(figsize=(8,6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis', s=50)
plt.title("K-Means Clustering Visualization")
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
plt.show()

# -----------------------------
# Step 6: Compare with Actual Labels (Optional)
# -----------------------------
print("\nActual vs Predicted Cluster Comparison:")
comparison = pd.DataFrame({'Actual': data.target, 'Cluster': labels})
print(comparison.head(10))
