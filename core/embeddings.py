# core/embeddings.py
from sentence_transformers import SentenceTransformer
from functools import lru_cache
from typing import List
import numpy as np

@lru_cache(maxsize=1)
def get_embedding_model():
    # Change model name if you like
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    return SentenceTransformer(model_name)


def embed_texts(texts: List[str]) -> np.ndarray:
    """
    Returns a 2D numpy array of embeddings for a list of texts.
    """
    model = get_embedding_model()
    embeddings = model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
    return embeddings
