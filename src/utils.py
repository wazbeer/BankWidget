import json


def get_financial_transactions(path: str) -> list[dict]:
    """Функция принимает Json фпйл и возвращает в python читаемый словарь"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return []

    except FileNotFoundError:
        print("File not found")
        return []
