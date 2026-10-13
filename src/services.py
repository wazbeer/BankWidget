import collections
import re


def desc_search(transaction_list: list[dict], word: str) -> list[dict]:
    """Принимает словарь с транзакциями и ключевое слово, возвращает отфильтрованный по ключевому слову список"""
    result = []
    for transaction in transaction_list:
        descriptions = transaction.get("description", "")
        if re.search(word, descriptions, flags=re.IGNORECASE):
            result.append(transaction)
    return result


def count_desc(transaction_list: list[dict], categories: list) -> dict:
    """Принимает словарь транзакций и словарь описаний для подсчёта, возвращает словарь с подсчитанными значениями"""
    categories_list = []
    for transaction in transaction_list:
        categories_list.append(transaction.get("description", ""))
    count = collections.Counter(categories_list)
    result = {}
    for category in categories:
        result[category] = count[category]
    return result
