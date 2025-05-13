import os
import csv
import sqlite3

class Storage:
    def __init__(self, base_path: str = None):
        self.base_path = base_path or os.path.abspath(os.path.dirname(__file__))
        self.csv_path = os.path.join(self.base_path, '..', 'books_data.csv')
        self.db_path = os.path.join(self.base_path, '..', 'books_data.sqlite')
        os.makedirs(os.path.dirname(self.csv_path), exist_ok=True)

    def save_to_csv(self, data):
        file_exists = os.path.isfile(self.csv_path)
        with open(self.csv_path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            if not file_exists:
                writer.writeheader()
            writer.writerows(data)

    def save_to_sqlite(self, data):
        conn = sqlite3.connect(self.db_path)
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

    def save_data(self, data):
        if not data:
            print("❌ No hay datos para guardar.")
            return
        self.save_to_csv(data)
        self.save_to_sqlite(data)
        print("✅ Datos guardados en CSV y SQLite.")
