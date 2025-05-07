import csv
import os
from typing import List, Dict

CSV_FILE = "books_data.csv"


def save_to_csv(data: List[Dict]):
    if not data:
        print("⚠️ No hay libros para guardar.")
        return

    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        if not file_exists:
            writer.writeheader()
        writer.writerows(data)

    print(f"✅ {len(data)} libros guardados en '{CSV_FILE}'")
