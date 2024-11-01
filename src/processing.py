from src.reading_csv import read_financial_operations


def filter_by_state(cards_information: list, status: str = "EXECUTED") -> list:
    """Function that takes the list of dictionaries and returns a new list
    of only those dictionaries in which the key "state" matches the indicated value.
    """
    filtered_list = []
    for card_information in cards_information:
        if card_information.get("state") == status:
            filtered_list.append(card_information)
        else:
            continue
    return filtered_list


def sort_by_date(cards_information: list, reverse: bool = True) -> list:
    """Function that takes the list of dictionaries and returns the sorted list
    of  dictionaries by date."""
    sorted_list_of_dictionaries = sorted(cards_information, key=lambda x: x["date"], reverse=reverse)
    return sorted_list_of_dictionaries


if __name__ == "__main__":
    file_path = "../data/transactions.csv"
    transactions = read_financial_operations(file_path)
    print(filter_by_state(transactions, "PENDING"))
    print(transactions)
