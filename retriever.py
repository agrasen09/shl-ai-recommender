import json

# Load catalog
with open("catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)


def search_assessments(query, top_k=5):

    query_words = query.lower().split()

    scored = []

    for item in catalog:

        score = 0

        text = (
            item["name"] + " " +
            item.get("description", "") + " " +
            item.get("category", "")
        ).lower()

        for word in query_words:
            if word in text:
                score += 1

        scored.append((score, item))

    scored.sort(key=lambda x: x[0], reverse=True)

    results = [item for score, item in scored[:top_k]]

    return results