import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load catalog
with open("catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("shl_index.faiss")


def search_assessments(query, top_k=10):

    # Query embedding
    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding).astype("float32")

    # Search
    distances, indices = index.search(query_embedding, top_k)

    scored_results = []

    query_lower = query.lower()

    for idx in indices[0]:

        item = catalog[idx]

        score = 0

        name = item["name"].lower()

        # Skill boosting
        if "technical" in query_lower or "developer" in query_lower:
            if "technical" in name or "skills" in name:
                score += 3

        if "personality" in query_lower:
            if "personality" in name:
                score += 3

        if "leadership" in query_lower:
            if "leadership" in name:
                score += 3

        if "communication" in query_lower:
            if "business" in name:
                score += 2

        scored_results.append((score, item))

    # Sort by boosted score
    scored_results.sort(key=lambda x: x[0], reverse=True)

    # Return top results
    final_results = [item for score, item in scored_results[:5]]

    return final_results