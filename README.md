# Results:
## Performance Metrics:
K-Means - Silhouette Score: 0.3041, Davies-Bouldin Index: 1.1672  
DBSCAN - Silhouette Score: 0.2776, Davies-Bouldin Index: 1.6117  

# Conclusion:
The DBSCAN and K-Means methods seemed to have pretty comparable scores, with K-Means winning on silhouette score, and DBSCAN winning on Davies-Bouldin. The evaluation results indicate that K-Means clustering performed better than DBSCAN for segmenting the mall customers. The Silhouette Score of 0.3041 for K-Means suggests that the clusters are moderately well-separated, while the Davies-Bouldin Index of 1.1672 implies relatively compact and distinct clusters. In contrast, DBSCAN achieved a lower Silhouette Score of 0.2776 and a higher Davies-Bouldin Index of 1.6117, indicating that its clusters were less well-defined. This suggests that K-Means was more effective in grouping customers based on their demographics and spending behavior. The segmentation likely reveals distinct customer groups, such as high-income frequent spenders, budget-conscious shoppers, and average consumers with balanced spending.
