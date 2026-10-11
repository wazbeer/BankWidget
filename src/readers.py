import pandas as pd
import csv

def csv_reader(csv_path: str) -> list[dict]:
    """Принимает на вход путь к csv файлу транзакций и возвращает лист"""
    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            return list(reader)
    except (FileNotFoundError):
        return []

def excel_reader(excel_path: str) -> list[dict]:
    """Принимает на вход путь к xlsx файлу транзакций и возвращает лист"""
    try:
        df = pd.read_excel(excel_path)
        df = df.fillna("")
        df = df.to_dict(orient='records')
        return df
    except (FileNotFoundError):
        return []