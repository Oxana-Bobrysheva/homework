import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_or_account_info, mask",
    [
        ("Счет 12341234123412341234", "**1234"),
        ("Счет 54321543215432154321", "**4321"),
        ("Visa 1234567891234567", "1234 56** **** 4567"),
        ("Mastercard 1234567891234567", "1234 56** **** 4567"),
        ("", "Wrong input! Try again."),
        ("Счет 123", "Wrong input! Try again."),
        ("Счет 1233123412341234", "Wrong input! Try again."),
        ("1233123412341234", "1233 12** **** 1234"),
        ("12331234123412341234", "**1234"),
    ],
)
def test_mask_account_card(card_or_account_info: str, mask: str) -> None:
    """Testing function for function get_mask_account from module masks.py with a help of decorator"""
    assert mask_account_card(card_or_account_info) == mask


@pytest.mark.parametrize(
    "date_info, mask",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("", "No date information"), ("2024-03-11T", "11.03.2024")],
)
def test_get_date(date_info: str, mask: str) -> None:
    assert get_date(date_info) == mask
