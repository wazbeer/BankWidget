from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 2),
        ("RUB", 1),
        ("EUR", 0),
    ],
)
def test_filter_by_currency_count(transactions_data: list[dict[str, Any]], currency: str, expected_count: int) -> None:
    """Проверка количества отфильтрованных транзакций по валюте."""
    filtered = filter_by_currency(transactions_data, currency)
    result = list(filtered)
    assert len(result) == expected_count


def test_filter_by_currency_next(transactions_data: list[dict[str, Any]]) -> None:
    """Проверка получения элементов по одному через next()."""
    usd_transactions = filter_by_currency(transactions_data, "USD")

    first = next(usd_transactions)
    assert first["id"] == 939719570

    second = next(usd_transactions)
    assert second["id"] == 142264268


def test_filter_by_currency_empty_list() -> None:
    """Проверка работы с пустым списком транзакций."""
    filtered = filter_by_currency([], "USD")
    assert list(filtered) == []


def test_transaction_descriptions(transactions_data: list[dict[str, Any]]) -> None:
    """Тест получения описаний транзакций."""
    descriptions = transaction_descriptions(transactions_data)

    # Превращаем генератор в список и сравниваем со списком ожидаемых строк
    expected = ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет"]
    assert list(descriptions) == expected


def test_transaction_descriptions_empty() -> None:
    """Тест описаний для пустого списка."""
    descriptions = transaction_descriptions([])
    assert list(descriptions) == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (5, 5, ["0000 0000 0000 0005"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list[str]) -> None:
    """Тест генерации номеров карт в диапазоне."""
    generator = card_number_generator(start, stop)
    assert list(generator) == expected


def test_card_number_generator_format() -> None:
    """Тест правильности формата номера карты (длина, пробелы)."""
    generator = card_number_generator(10, 10)
    card_number = next(generator)

    # Длина строки должна быть ровно 19 символов (16 цифр + 3 пробела)
    assert len(card_number) == 19
    # Должно быть ровно 3 пробела
    assert card_number.count(" ") == 3
