import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(list_of_transactions: list) -> None:
    expected_result = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    result = filter_by_currency(list_of_transactions, "USD")
    assert next(result) == expected_result


def test_transaction_descriptions(list_of_transactions: list) -> None:
    expected_result = "Перевод организации"
    result = transaction_descriptions(list_of_transactions)
    assert next(result) == expected_result


@pytest.mark.parametrize(
    "start, end, mask",
    [
        (1, 2, "0000 0000 0000 0001"),
        (2, 3, "0000 0000 0000 0002"),
    ],
)
def test_card_number_generator(start: int, end: int, mask: str) -> None:
    assert next(card_number_generator(start, end)) == mask
