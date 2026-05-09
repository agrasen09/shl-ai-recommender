import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load catalog
with open("catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

texts = []

for item in catalog:

    text = f"""
    Name: {item['name']}
    Description: {item['description']}
    Category: {item['category']}
    """

    texts.append(text)

# Create embeddings
embeddings = model.encode(texts)

embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# Save index
faiss.write_index(index, "shl_index.faiss")

print("Improved embeddings created successfully")
print(f"Indexed assessments: {len(texts)}")