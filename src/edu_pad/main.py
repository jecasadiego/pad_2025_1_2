from functions.scraper import fetch_books_from_page
from db.db import save_to_csv


def run(total_pages: int):
    all_books = []
    for page in range(1, total_pages + 1):
        print(f"🔎 Procesando página {page}...")
        books = fetch_books_from_page(page)
        all_books.extend(books)

    save_to_csv(all_books)


if __name__ == "__main__":
    try:
        pages = int(input("¿Cuántas páginas quieres scrapear? (Máximo 50): ").strip())
        if 1 <= pages <= 50:
            run(pages)
        else:
            print("❌ Número de páginas fuera de rango.")
    except ValueError:
        print("❌ Debes ingresar un número entero válido.")
