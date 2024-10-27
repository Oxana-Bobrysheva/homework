import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> str:
    """Testing function for function get_mask_card_number from module masks.py"""
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"
    assert get_mask_card_number("") == "This card number is NOT correct. It should have 16 numbers. Try again."
    assert (
        get_mask_card_number("123123123") == "This card number is NOT correct. It should have 16 numbers. Try again."
    )
    assert (
        get_mask_card_number("Visa 1231231231231234")
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
    ],
)
def test_get_mask_account(account_number: str, mask: str) -> str:
    """Testing function for function get_mask_account from module masks.py with a help of decorator"""
    assert get_mask_account(account_number) == mask
