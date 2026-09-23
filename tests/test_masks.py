import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number,expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1596837868705199", "1596 83** **** 5199"),
        ("6831982476737658", "6831 98** **** 7658"),
    ],
)
def test_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number,expected",
    [("73654108430135874305", "**4305"), ("64686473678894779589", "**9589"), ("35383033474447895560", "**5560")],
)
def test_account_number(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected
