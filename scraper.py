import requests
from bs4 import BeautifulSoup
import json

url = "https://www.shl.com/solutions/products/product-catalog/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "lxml")

cards = soup.find_all("a")

catalog = []

seen = set()

for card in cards:

    name = card.get_text(strip=True)
    href = card.get("href")

    if not name or not href:
        continue

    if "/products/" not in href and "/product-catalog/" not in href:
        continue

    if href.startswith("/"):
        href = "https://www.shl.com" + href

    if href in seen:
        continue

    seen.add(href)

    item = {
        "name": name,
        "url": href,
        "description": name,
        "category": "SHL Assessment"
    }

    catalog.append(item)

with open("catalog.json", "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=4)

print(f"Saved {len(catalog)} assessments")