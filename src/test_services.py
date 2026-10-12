from typing import Any

import pytest

from src.services import count_desc, desc_search


@pytest.fixture
def sample_data_for_search() -> list[dict[str, Any]]:
    """Фикстура с тестовыми транзакциями для поиска и подсчета."""
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"},
        {"id": 3, "description": "Открытие вклада"},
    ]


@pytest.mark.parametrize(
    "search_word, expected_count",
    [
        ("Перевод", 2),  # Должен найти 2 перевода
        ("перевод", 2),  # Регистронезависимый поиск
        ("вклада", 1),  # Должен найти 1 вклад
        ("Такси", 0),  # Такого слова нет -> 0
    ],
)
def test_desc_search_found(
    sample_data_for_search: list[dict[str, Any]], search_word: str, expected_count: int
) -> None:
    """Тест поиска по регулярным выражениям с разным регистром и словами."""
    result = desc_search(sample_data_for_search, search_word)
    assert len(result) == expected_count


def test_desc_search_empty_list() -> None:
    """Тест поиска в пустом списке транзакций."""
    result = desc_search([], "Перевод")
    assert result == []


def test_count_desc_success(sample_data_for_search: list[dict[str, Any]]) -> None:
    """Тест успешного подсчета операций по заданным категориям."""
    categories = ["Перевод организации", "Открытие вклада", "Такси"]
    expected = {
        "Перевод организации": 1,
        "Открытие вклада": 1,
        "Такси": 0,
    }
    result = count_desc(sample_data_for_search, categories)
    assert result == expected


def test_count_desc_empty_transactions() -> None:
    """Тест подсчета категорий при пустом списке транзакций."""
    categories = ["Перевод организации", "Открытие вклада"]
    expected = {
        "Перевод организации": 0,
        "Открытие вклада": 0,
    }
    result = count_desc([], categories)
    assert result == expected


def test_count_desc_empty_categories(sample_data_for_search: list[dict[str, Any]]) -> None:
    """Тест подсчета при пустом списке категорий."""
    result = count_desc(sample_data_for_search, [])
    assert result == {}
