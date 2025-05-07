# ✅ Correcto
from edu_pad.functions.scraper import fetch_books_from_page
from edu_pad.db.db import save_to_csv


def main_run(total_pages: int):
    all_books = []
    for page in range(1, total_pages + 1):
        print(f"🔎 Procesando página {page}...")
        books = fetch_books_from_page(page)
        all_books.extend(books)

    save_to_csv(all_books)

def run():  # Esta es la que setup.py debe apuntar
    try:
        pages = int(input("¿Cuántas páginas quieres scrapear? (Máximo 50): ").strip())
        if 1 <= pages <= 50:
            main_run(pages)
        else:
            print("❌ Número de páginas fuera de rango.")
    except ValueError:
        print("❌ Debes ingresar un número entero válido.")

if __name__ == "__main__":
    run()
