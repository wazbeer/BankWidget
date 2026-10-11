from typing import Any
from unittest.mock import MagicMock, Mock, mock_open, patch

from src.readers import csv_reader, excel_reader


def test_happy_csv() -> None:
    with patch("builtins.open", mock_open(read_data="id;amount\n1;100")):
        result = csv_reader("dummy.csv")
        assert result == [{"id": "1", "amount": "100"}]


def test_no_file_csv() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = csv_reader("bad_path.csv")
        assert result == []


@patch("pandas.read_excel")
def test_happy_xls(mock_read_excel: Any) -> None:
    mock_df = Mock()
    mock_df.fillna.return_value.to_dict.return_value = [{"id": "1", "amount": "100"}]
    mock_read_excel.return_value = mock_df
    result = excel_reader("dummy.xlsx")
    assert result == [{"id": "1", "amount": "100"}]


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_no_file_xls(read_data: MagicMock) -> None:
    result = excel_reader("bad_path.xlsx")
    assert result == []
