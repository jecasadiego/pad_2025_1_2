from edu_pad.functions.scraper import (
    scrape_with_bs4,
    scrape_with_selenium,
    show_scrapy_instruction
)

def run():
    print("=== MÉTODOS DE SCRAPING DISPONIBLES ===")
    print("1. BeautifulSoup")
    print("2. Selenium")
    print("3. Scrapy")
    choice = input("Selecciona el método (1-3): ").strip()

    if choice in ["1", "2"]:
        try:
            pages = int(input("¿Cuántas páginas quieres scrapear? (1-50): ").strip())
            if not 1 <= pages <= 50:
                raise ValueError()
        except ValueError:
            print("❌ Número inválido.")
            return

        if choice == "1":
            scrape_with_bs4(pages)
        elif choice == "2":
            scrape_with_selenium(pages)

    elif choice == "3":
        show_scrapy_instruction()
    else:
        print("❌ Opción no válida.")

if __name__ == "__main__":
    run()
