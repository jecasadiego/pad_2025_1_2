import scrapy
import json
from pathlib import Path
import sys
import os

# Agregar el path de 'src' para poder importar edu_pad
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))

from edu_pad.db.db import save_to_csv, save_to_sqlite


class BooksSpider(scrapy.Spider):
    name = "books"

    def __init__(self, pages=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.pages = min(max(int(pages), 1), 50)  # asegura 1 <= pages <= 50
        except ValueError:
            self.pages = 1
        self.data = []

    def start_requests(self):
        for i in range(1, self.pages + 1):
            url = f"https://books.toscrape.com/catalogue/page-{i}.html"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for book in response.css("article.product_pod"):
            title = book.css("h3 a::attr(title)").get()
            raw_price = book.css(".price_color::text").get()
            price = float(raw_price.replace("£", "").replace("Â", "").strip())
            availability = book.css(".availability::text").getall()[-1].strip()
            rating = book.css("p.star-rating::attr(class)").get().split()[-1]

            self.data.append({
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating
            })

    def close(self, reason):
        if self.data:
            print(f"🟢 Guardando {len(self.data)} libros extraídos...")
            save_to_csv(self.data)
            save_to_sqlite(self.data)
            self.logger.info(f"✅ {len(self.data)} libros guardados en CSV y SQLite")
        else:
            self.logger.warning("⚠️ No se extrajeron datos")
