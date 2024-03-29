# # 综合分类数据集
# from numpy import where
# from sklearn.datasets import make_classification
# from matplotlib import pyplot
# # 定义数据集
# X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
# # 为每个类的样本创建散点图
# for class_value in range(2):
# # 获取此类的示例的行索引
#     row_ix = where(y == class_value)
#     # 创建这些样本的散布
#     pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
#     # 绘制散点图
# pyplot.show()
# # 亲和力传播聚类
# from numpy import unique
# from numpy import where
# from sklearn.datasets import make_classification
# from sklearn.cluster import AffinityPropagation
# from matplotlib import pyplot
# # 定义数据集
# X, _ = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
# # 定义模型
# model = AffinityPropagation(damping=0.9)
# # 匹配模型
# model.fit(X)
# # 为每个示例分配一个集群
# yhat = model.predict(X)
# # 检索唯一群集
# clusters = unique(yhat)
# # 为每个群集的样本创建散点图
# for cluster in clusters:
#     # 获取此群集的示例的行索引
#     row_ix = where(yhat == cluster)
#     # 创建这些样本的散布
#     pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
# # 绘制散点图
# pyplot.show()
#
# 聚合聚类
# from numpy import unique
# from numpy import where
# from sklearn.datasets import make_classification
# from sklearn.cluster import AgglomerativeClustering
# from matplotlib import pyplot
# # 定义数据集
# X, _ = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
# # 定义模型
# model = AgglomerativeClustering(n_clusters=2)
# # 模型拟合与聚类预测
# yhat = model.fit_predict(X)
# # 检索唯一群集
# clusters = unique(yhat)
# # 为每个群集的样本创建散点图
# for cluster in clusters:
#     # 获取此群集的示例的行索引
#     row_ix = where(yhat == cluster)
#     # 创建这些样本的散布
#     pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
# # 绘制散点图
# pyplot.show()
# k-means 聚类
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
from matplotlib import pyplot
from sklearn.tree import plot_tree
# 定义数据集
X, _ = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
print(len(X))
# 定义模型
model = KMeans(n_clusters=4)
# 模型拟合
model.fit(X)
# 为每个示例分配一个集群
yhat = model.predict(X)
# 检索唯一群集
clusters = unique(yhat)
print(yhat)
pyplot.figure(figsize=(10, 8))
plot_tree(model, filled=True)
pyplot.show()
# 为每个群集的样本创建散点图
for cluster in clusters:
    # 获取此群集的示例的行索引

    row_ix = where(yhat == cluster)
    # 创建这些样本的散布
    pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
    # 绘制散点图
pyplot.show()
