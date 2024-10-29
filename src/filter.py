import re


def filter_by_search_string(list_of_transactions: list, search_string: str) -> list:
    """This function takes list of dictionaries with bank transactions and a string for search.
    As the result it returns the filtered list of transactions."""
    filtered_transactions = []
    pattern = re.compile(search_string, re.IGNORECASE)

    for transaction in list_of_transactions:
        if "description" in transaction and pattern.search(transaction["description"]):
            filtered_transactions.append(transaction)

    return filtered_transactions


if __name__ == "__main__":
    # Пример данных о банковских операциях
    transactions = [
        {"id": 1, "amount": 100, "description": "Оплата за услуги"},
        {"id": 2, "amount": 200, "description": "Перевод на счет"},
        {"id": 3, "amount": 150, "description": "Оплата за интернет"},
        {"id": 4, "amount": 250, "description": "Оплата за услуги связи"},
    ]

    # Пример использования функции
    search_str = "услуги"
    result = filter_by_search_string(transactions, search_str)
    print(result)
