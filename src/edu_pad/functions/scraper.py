import requests
from bs4 import BeautifulSoup
from typing import List, Dict


def fetch_books_from_page(page: int) -> List[Dict]:
    BASE_URL = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(BASE_URL)
    if response.status_code != 200:
        print(f"❌ No se pudo acceder a la página {page}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.select("article.product_pod")

    books = []
    for article in articles:
        title = article.h3.a["title"]
        price = article.select_one(".price_color").text.strip().replace("£", "")
        availability = article.select_one(".availability").text.strip()
        rating = article.select_one("p.star-rating")["class"][1]

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating
        })

    return books
