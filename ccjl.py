import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs

# 生成随机数据
X, y = make_blobs(n_samples=300, centers=4, random_state=42)

# 使用层次聚类算法
Z = linkage(X, method='ward')

# 画出树状图
plt.figure(figsize=(15, 10))
dendrogram(Z)
plt.show()
