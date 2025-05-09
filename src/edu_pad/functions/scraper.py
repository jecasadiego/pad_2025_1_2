import requests
from bs4 import BeautifulSoup
from edu_pad.db.db import save_to_csv, save_to_sqlite
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tqdm import tqdm  # NUEVO: progreso

# Rutas de salida en carpeta /db
BASE_PATH = os.path.join(os.path.dirname(__file__), '..', 'db')
CSV_PATH = os.path.join(BASE_PATH, 'books_data.csv')
DB_PATH = os.path.join(BASE_PATH, 'books_data.sqlite')

# ========================
# FUNCIONES DE SCRAPING
# ========================

def scrape_with_bs4(pages=1):
    print("📘 Scraping con BeautifulSoup...")
    data = []

    for page in tqdm(range(1, pages + 1), desc="Scrapeando páginas (BS4)", unit="página"):
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
    save_data(data)


def scrape_with_selenium(pages=1):
    print("📗 Scraping con Selenium...")
    data = []
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    for page in tqdm(range(1, pages + 1), desc="Scrapeando páginas (Selenium)", unit="página"):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        driver.get(url)
        books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
        for book in books:
            title = book.find_element(By.TAG_NAME, "h3").text
            raw_price = book.find_element(By.CLASS_NAME, "price_color").text
            price = float(raw_price.replace('£', '').replace('Â', '').strip())
            availability = book.find_element(By.CLASS_NAME, "availability").text.strip()
            rating = book.find_element(By.CSS_SELECTOR, "p.star-rating").get_attribute("class").split()[1]
            data.append({
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating
            })

    driver.quit()
    save_data(data)


def show_scrapy_instruction():
    print("📙 Scrapy se ejecuta desde consola:")
    print("  scrapy crawl books -o books_data.json")
    print("Puedes luego convertirlo a CSV o SQLite si lo deseas.")

# ========================
# FUNCIONES DE GUARDADO
# ========================

def save_data(data):
    if not data:
        print("❌ No hay datos para guardar.")
        return
    os.makedirs(BASE_PATH, exist_ok=True)
    save_to_csv(data)
    save_to_sqlite(data)
    print("✅ Datos guardados en CSV y SQLite.")