from typing import Any

import pytest


@pytest.fixture
def sample_operations() -> list[dict[str, Any]]:
    """Фикстура, возвращающая стандартный список операций."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


@pytest.fixture
def same_dates_operations() -> list[dict[str, Any]]:
    """Одинаковые даты для проверки сортировки"""
    return [
        {"id": 435946, "state": "EXECUTED", "date": "2020-01-01T00:00:00.000000"},
        {"id": 438759, "state": "EXECUTED", "date": "2020-01-01T00:00:00.000000"},
    ]


@pytest.fixture
def empty_operations() -> list[dict[str, Any]]:
    """Пустой список"""
    return []
