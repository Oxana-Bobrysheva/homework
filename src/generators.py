from typing import Generator, Iterator


def filter_by_currency(list_of_transactions: list, currency: str) -> list[dict]:
    """This function takes the list of transactions and returns iterator
    that shows transactions with certain currency"""
    new_list_of_transacions = []
    for transaction in list_of_transactions:
        if transaction.get("operationAmount_currency_code"):
            if transaction["operationAmount_currency_code"] == currency:
                new_list_of_transacions.append(transaction)
        else:
            if transaction["currency_code"] == currency:
                new_list_of_transacions.append(transaction)

    return new_list_of_transacions


def transaction_descriptions(list_of_transactions: list) -> Iterator[str]:
    """This function takes the list of transactions and returns iterator
    that shows description of transaction"""
    for transaction in list_of_transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """This function generates credit card numbers in the format XXXX XXXX XXXX XXXX
    within the specified range."""
    for card_num in range(start, end):
        # Convert card number to string
        card_str = str(card_num)

        # Pad with leading zeros to ensure 16 digits
        padded_card = card_str.zfill(16)

        # Format the card number
        formatted_card = f"{padded_card[:4]} {padded_card[4:8]} {padded_card[8:12]} {padded_card[12:]}"

        yield formatted_card
