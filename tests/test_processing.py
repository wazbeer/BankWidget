from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state,expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 1),
        ("PENDING", 0),
    ],
)
def test_filter_by_state(sample_operations: list[dict[str, Any]], state: str, expected_count: int) -> None:
    result = filter_by_state(sample_operations, state)
    assert len(result) == expected_count


def test_filter_by_state_default(sample_operations: list[dict[str, Any]]) -> None:
    result = filter_by_state(sample_operations)
    assert len(result) == 2


def test_sort_by_date_descending(sample_operations: list[dict[str, Any]]) -> None:
    result = sort_by_date(sample_operations)
    # Самая свежая дата (2019 год) должна быть первой
    assert result[0]["id"] == 41428829
    # Самая старая дата (2018-06-30) должна быть последней
    assert result[-1]["id"] == 939719570


def test_sort_by_date_ascending(sample_operations: list[dict[str, Any]]) -> None:
    result = sort_by_date(sample_operations, reverse=False)
    assert result[0]["id"] == 939719570
