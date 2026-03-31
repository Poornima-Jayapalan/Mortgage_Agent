"""
Test embedding generation and visualize using PCA.
"""

from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

texts = [
    "interest rate clause",
    "payment schedule",
    "escrow details",
    "late fee policy"
]

embedder = FastEmbedEmbeddings()
vectors = embedder.embed_documents(texts)

pca = PCA(n_components=2)
points = pca.fit_transform(vectors)

plt.scatter(points[:, 0], points[:, 1])

for i, label in enumerate(texts):
    plt.annotate(label, (points[i, 0], points[i, 1]))

plt.title("Embedding Visualization (PCA)")
plt.show()
