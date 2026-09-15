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


operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]


if __name__ == "__main__":
    print(filter_by_state(operations, "EXECUTED"))
    print(filter_by_state(operations, "CANCELED"))
    print(sort_by_date(operations))
