from scraper import BookScraper

def run():
    print("=== MÉTODOS DE SCRAPING DISPONIBLES ===")
    print("1. BeautifulSoup")
    choice = input("Selecciona el método (1): ").strip()

    if choice == "1":
        try:
            pages = int(input("¿Cuántas páginas quieres scrapear? (1-50): ").strip())
            if not 1 <= pages <= 50:
                raise ValueError()
        except ValueError:
            print("❌ Número inválido.")
            return

        scraper = BookScraper(pages)
        scraper.scrape()
    else:
        print("❌ Opción no válida.")

if __name__ == "__main__":
    run()
