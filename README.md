# 📚 Proyecto de Web Scraping de Libros con Python

Este proyecto permite extraer información comercial (título, precio, disponibilidad y calificación) del sitio [Books to Scrape](https://books.toscrape.com) utilizando tres métodos de scraping: **BeautifulSoup**, **Selenium** y **Scrapy**. Los resultados se guardan en un archivo `.csv` y una base de datos `.sqlite`.

---

## 🚀 Instalación y configuración

### 1. Clona el repositorio y accede a su carpeta

```bash
git clone https://github.com/jecasadiego/pad_2025_1_2.git
```

### 2. Crea y activa un entorno virtual dentro de pad_2025_1_2

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instala el proyecto

```bash
pip install -e .
```

Esto instalará automáticamente todas las dependencias necesarias.

---

## 🧪 Uso desde consola (modo CLI)

```bash
edu-pad-run
```

Este comando te preguntará:

- Qué método de scraping deseas usar:
  - `1` → BeautifulSoup
  - `2` → Selenium
  - `3` → Scrapy (solo muestra instrucciones)
- Cuántas páginas deseas scrapear (1–50)

Los datos se guardan automáticamente en:

- `src/edu_pad/db/books_data.csv`
- `src/edu_pad/db/books_data.sqlite`

---

## 🕷️ Uso con Scrapy directamente

### 1. Ve a la carpeta del proyecto Scrapy:

```bash
cd edu_scrapy
```

### 2. Ejecuta el spider indicando cuántas páginas scrapear:

```bash
scrapy crawl books -a pages=10
```

> Los archivos también se guardarán en `src/edu_pad/db/`.

---

## 🗂 Estructura del proyecto

```
src/
└── edu_pad/
    ├── db/
    │   ├── db.py               ← Funciones de guardado en CSV y SQLite
    ├── functions/
    │   └── scraper.py          ← Lógica del scraping con BeautifulSoup y Selenium
    └── static/
        └── main.py             ← Menú principal (CLI)
edu_scrapy/
└── edu_scrapy/spiders/books.py ← Spider Scrapy
```

---

## 📦 Dependencias principales

- `beautifulsoup4`
- `requests`
- `selenium`
- `webdriver-manager`
- `scrapy`
- `tqdm`

Todas se instalan con `pip install -e .` vía `setup.py`.

---

## ✍️ Autor

**Juan Esteban Casadiego Benavides**

---

## 📄 Licencia

Este proyecto es de uso educativo y libre bajo licencia MIT.