import json
from collections import Counter


def get_categories(list_of_transactions: list) -> list:
    """Function that makes list of categories in description of transactions"""
    list_of_categories = set()
    for transaction in list_of_transactions:
        category = transaction.get("description")
        if category:
            list_of_categories.add(category)
    return list(list_of_categories)


def count_transactions_by_category(list_of_transactions: list, list_of_categories: list) -> dict:
    """Function that takes list of transactions and list of categories and returns quantity of each category in the
    list of transactions"""

    # Создаем счетчик для подсчета операций
    category_counter: Counter = Counter()

    # Итерируемся по всем операциям
    for transaction in list_of_transactions:
        # Получаем описание операции
        description = transaction.get("description", "")

        # Проверяем, если описание содержит категорию
        for category in list_of_categories:
            if category in description:
                category_counter[category] += 1

    # Преобразуем счетчик в словарь и возвращаем
    return dict(category_counter)


# Пример использования
if __name__ == "__main__":
    with open("../data/operations.json", "r", encoding="UTF-8") as file:
        data = json.load(file)

    categories = get_categories(data)
    print(categories)

    result = count_transactions_by_category(data, categories)
    print(result)
