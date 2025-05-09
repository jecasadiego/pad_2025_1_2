import os
import csv
import sqlite3

# Ruta absoluta a la carpeta actual del archivo
BASE_PATH = os.path.abspath(os.path.dirname(__file__))
CSV_PATH = os.path.join(BASE_PATH, 'books_data.csv')
DB_PATH = os.path.join(BASE_PATH, 'books_data.sqlite')


def save_to_csv(data):
    os.makedirs(BASE_PATH, exist_ok=True)  # 🔒 crea la carpeta si no existe
    file_exists = os.path.isfile(CSV_PATH)
    with open(CSV_PATH, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        if not file_exists:
            writer.writeheader()
        writer.writerows(data)


def save_to_sqlite(data):
    os.makedirs(BASE_PATH, exist_ok=True)  # 🔒 asegura existencia
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL,
            availability TEXT,
            rating TEXT
        )
    ''')
    for book in data:
        cursor.execute('''
            INSERT INTO books (title, price, availability, rating)
            VALUES (?, ?, ?, ?)
        ''', (book['title'], book['price'], book['availability'], book['rating']))
    conn.commit()
    conn.close()
