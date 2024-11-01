import logging

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    """Testing function for function get_mask_card_number from module masks.py"""
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"
    assert get_mask_card_number("") == "This card number is NOT correct. It should have 16 numbers. Try again."
    assert (
        get_mask_card_number("123123123") == "This card number is NOT correct. It should have 16 numbers. Try again."
    )
    assert (
        get_mask_card_number("123456781234567")
        == "This card number is NOT correct. It should have 16 numbers. Try again."
    )
    assert (
        get_mask_card_number("12345678123456789")
        == "This card number is NOT correct. It should have 16 numbers. Try again."
    )


# Decorator that allows to check the function with different input data
@pytest.mark.parametrize(
    "account_number, mask",
    [
        ("12341234123412341234", "**1234"),
        ("54321543215432154321", "**4321"),
        ("1234567891234567", "This account number is NOT correct. It should have 20 numbers. Try again."),
        ("", "This account number is NOT correct. It should have 20 numbers. Try again."),
        ("123456789123456789", "This account number is NOT correct. It should have 20 numbers. Try again."),
        ("123456789123456", "This account number is NOT correct. It should have 20 numbers. Try again."),
    ],
)
def test_get_mask_account(account_number: str, mask: str) -> None:
    """Testing function for function get_mask_account from module masks.py with a help of decorator"""
    assert get_mask_account(account_number) == mask


def test_logging_for_get_mask_card_number(caplog):
    with caplog.at_level(logging.INFO):
        get_mask_card_number("1234567812345678")
    assert "Starting the function get_mask_card_number" in caplog.text
    assert "Mask of the credit card was made: 1234 56** **** 5678" in caplog.text


def test_logging_for_get_mask_account(caplog):
    with caplog.at_level(logging.INFO):
        get_mask_account("12341234123412341234")
    assert "Starting the function get_mask_account" in caplog.text
    assert "Mask of the account was made: **1234" in caplog.text
