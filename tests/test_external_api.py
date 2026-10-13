from typing import Any
from unittest.mock import patch

from src.external_api import convert_currency

transaction = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    },
]


@patch("requests.get")
def test_rub(mock_get: Any) -> None:
    """тестирует получение словаря с рублём"""
    result = convert_currency(transaction[0])
    assert result == 31957.58
    mock_get.assert_not_called()


@patch("requests.request")
def test_convert_currency(mock_get: Any) -> None:
    """тестиурет получение словаря с любой другой валютой и обращением к серверу"""
    mock_get.return_value.json.return_value = {"result": 8221.37}
    assert convert_currency(transaction[1]) == 8221.37
    mock_get.assert_called_once()
