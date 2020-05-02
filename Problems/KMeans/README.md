# K Means
Kmeans algorithm is an iterative algorithm that tries to partition the dataset into Kpre-defined distinct non-overlapping subgroups (clusters) where each data point belongs to only one group.
t tries to make the intra-cluster data points as similar as possible while also keeping the clusters as different (far) as possible.

#### Objective Function:
![equation](https://miro.medium.com/max/1096/1*myXqNCTZH80uvO2QyU6F5Q.png)
Where `wik` is the normalization parameter and `uk` is the mean of along the column.

#### Stop Condition
The iterations has to be ended when there is no change in the `K` centroid positions.

#### Reference
1. [K-means Clustering: Algorithm, Applications, Evaluation Methods, and Drawbacks](https://towardsdatascience.com/k-means-clustering-algorithm-applications-evaluation-methods-and-drawbacks-aa03e644b48a)