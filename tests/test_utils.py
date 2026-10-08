from unittest.mock import mock_open, patch

from src.utils import get_financial_transactions


def test_happy_path() -> None:
    """ "тестирует успешную передачу файлы в функцию"""
    with patch("builtins.open", mock_open(read_data='[{"id": 1}]')):
        result = get_financial_transactions("dummy.json")
        assert result == [{"id": 1}]


def test_file_not_found() -> None:
    """тестирует отсутствие файла при передаче в функцию-"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = get_financial_transactions("dummy.json")
        assert result == []
