from typing import Any


def filter_by_state(operation: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция принимает лист операций и возвращает отсортированный список по состоянию(Executed по умолчанию)"""
    filtered_list = []
    for item in operation:
        if item["state"] == state:
            filtered_list.append(item)
    return filtered_list


def sort_by_date(operation: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция принимает лист операций и возвращает отсортированный список по времени операции"""
    filtered_date = sorted(operation, key=lambda x: x["date"], reverse=reverse)
    return filtered_date