import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score

import os
os.environ["LOKY_MAX_CPU_COUNT"] = "1" 


# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Drop CustomerID
df.drop(columns=["CustomerID"], inplace=True)

# Encode Gender
df["Gender"] = LabelEncoder().fit_transform(df["Gender"])

# Define preprocessing pipeline
preprocessing_pipeline = Pipeline([
    ("scaler", StandardScaler())
])

df_scaled = preprocessing_pipeline.fit_transform(df)

# K-Means Clustering Pipeline
kmeans_pipeline = Pipeline([
    ("kmeans", KMeans(n_clusters=5, random_state=42, n_init=10))
])
kmeans_labels = kmeans_pipeline.fit_predict(df_scaled)

# DBSCAN Clustering Pipeline
dbscan_pipeline = Pipeline([
    ("dbscan", DBSCAN(eps=1.5, min_samples=5))
])
dbscan_labels = dbscan_pipeline.fit_predict(df_scaled)

# Evaluate Clustering Performance
silhouette_kmeans = silhouette_score(df_scaled, kmeans_labels)
davies_kmeans = davies_bouldin_score(df_scaled, kmeans_labels)

silhouette_dbscan = silhouette_score(df_scaled, dbscan_labels) if len(set(dbscan_labels)) > 1 else -1
davies_dbscan = davies_bouldin_score(df_scaled, dbscan_labels) if len(set(dbscan_labels)) > 1 else -1

print("Performance Metrics:")
print(f"K-Means - Silhouette Score: {silhouette_kmeans:.4f}, Davies-Bouldin Index: {davies_kmeans:.4f}")
print(f"DBSCAN - Silhouette Score: {silhouette_dbscan:.4f}, Davies-Bouldin Index: {davies_dbscan:.4f}")

# Visualizing Clusters (K-Means)
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df_scaled[:, 2], y=df_scaled[:, 3], hue=kmeans_labels, palette='viridis', s=50)
plt.title("K-Means Clustering")
plt.xlabel("Annual Income (scaled)")
plt.ylabel("Spending Score (scaled)")
plt.show()

# Visualizing Clusters (DBSCAN)
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df_scaled[:, 2], y=df_scaled[:, 3], hue=dbscan_labels, palette='coolwarm', s=50)
plt.title("DBSCAN Clustering")
plt.xlabel("Annual Income (scaled)")
plt.ylabel("Spending Score (scaled)")
plt.show()
