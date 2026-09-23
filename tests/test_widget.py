import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_mask_account_card(input_data: str, expected: str) -> None:
    """"Тестиурет маску вместе с именем карты"""
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2001-12-10T02:31:26.453075", "10.12.2001"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
    ],
)
def test_get_date(input_data: str, expected: str) -> None:
    """Тестирует форматирование даты под РУ формат""""
    assert get_date(input_data) == expected
