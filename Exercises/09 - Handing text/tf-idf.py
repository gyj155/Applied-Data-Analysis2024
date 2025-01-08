from sklearn.feature_extraction.text import TfidfVectorizer

# 示例文档
documents = [
    "I love programming and data analysis",
    "Data analysis and machine learning are amazing",
    "Machine learning is a fascinating field"
]

# 初始化 TfidfVectorizer
vectorizer = TfidfVectorizer()

# 生成 TF-IDF 矩阵
tfidf_matrix = vectorizer.fit_transform(documents)

# 输出特征名称（词汇表）
print("Feature Names:", vectorizer.get_feature_names_out())

# 转换为稀疏矩阵形式
print("TF-IDF Matrix:")
print(tfidf_matrix.toarray())
""" 
Feature Names: ['amazing' 'analysis' 'and' 'are' 'data' 'fascinating' 'field' 'is'
 'learning' 'love' 'machine' 'programming']
TF-IDF Matrix:
[[0.         0.3935112  0.3935112  0.         0.3935112  0.
  0.         0.         0.         0.51741994 0.         0.51741994]
 [0.45212331 0.34385143 0.34385143 0.45212331 0.34385143 0.
  0.         0.         0.34385143 0.         0.34385143 0.        ]
 [0.         0.         0.         0.         0.         0.49047908
  0.49047908 0.49047908 0.37302199 0.         0.37302199 0.        ]]

"""