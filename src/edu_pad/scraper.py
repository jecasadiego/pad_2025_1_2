import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from storage import Storage

class BookScraper:
    def __init__(self, pages=1):
        self.pages = pages
        self.storage = Storage()

    def scrape(self):
        print("📘 Scraping con BeautifulSoup...")
        data = []
        for page in tqdm(range(1, self.pages + 1), desc="Scrapeando páginas (BS4)", unit="página"):
            url = f"https://books.toscrape.com/catalogue/page-{page}.html"
            response = requests.get(url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            books = soup.select("article.product_pod")
            for book in books:
                raw_price = book.select_one(".price_color").text
                price = float(raw_price.replace('£', '').replace('Â', '').strip())
                data.append({
                    "title": book.h3.a['title'],
                    "price": price,
                    "availability": book.select_one(".availability").text.strip(),
                    "rating": book.select_one("p.star-rating")["class"][1]
                })
        self.storage.save_data(data)
