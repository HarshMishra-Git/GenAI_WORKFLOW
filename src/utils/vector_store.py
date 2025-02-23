
import numpy as np
import faiss
from typing import List, Dict
from sentence_transformers import SentenceTransformer
from langchain_core.documents import Document

class VectorStore:
    def __init__(self):
        self.embeddings = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.documents = []

    def add_documents(self, documents: List[Document]):
        """Add documents to the vector store."""
        try:
            embeddings = self.embeddings.encode([doc.page_content for doc in documents])
            if self.index is None:
                dimension = len(embeddings[0])
                self.index = faiss.IndexFlatL2(dimension)

            self.index.add(np.array(embeddings))
            self.documents.extend(documents)
            return True
        except Exception as e:
            raise Exception(f"Error adding documents to vector store: {str(e)}")

    def search(self, query: str, k: int = 5) -> List[Dict]:
        """Search for similar documents."""
        if not self.index:
            return []

        query_embedding = self.embeddings.encode([query])[0]
        D, I = self.index.search(np.array([query_embedding]), k)

        results = []
        for i, idx in enumerate(I[0]):
            if idx < len(self.documents):
                results.append({
                    'content': self.documents[idx].page_content,
                    'score': float(D[0][i]),
                })
        return results
