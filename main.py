import re

import pandas as pd

from src.filter import filter_by_search_string
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reading_csv import read_financial_operations
from src.reading_excel import reading_xlsx
from src.utils import get_transactions
from src.widget import get_date, mask_account_card


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ")

    if choice == "1":
        file_path = "data/operations.json"
        transactions = get_transactions(file_path)
        file_type = "JSON"
    elif choice == "2":
        file_path = "data/transactions.csv"
        transactions = read_financial_operations(file_path)
        file_type = "CSV"
    elif choice == "3":
        file_path = "data/transactions_excel.xlsx"
        transactions = reading_xlsx(file_path)
        file_type = "XLSX"
    else:
        print("Неверный выбор. Завершение программы.")
        return

    print(f"Для обработки выбран {file_type}-файл.")

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            "Введите выбранный статус: "
        ).upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    filtered_transactions = filter_by_state(transactions, status)
    print(f'Операции отфильтрованы по статусу "{status}".')

    sort_choice = input("Отсортировать операции по дате? Yes / No\nВаш выбор: ").strip().lower()

    if sort_choice == "yes":
        order_choice = input("Отсортировать по возрастанию? Yes / No\nВаш выбор: ").strip().lower()
        ascending = order_choice == "yes"
        filtered_transactions = sort_by_date(filtered_transactions, ascending)

    currency_choice = input("Выводить только рублевые транзакции? Yes / No\nВаш выбор: ").strip().lower()

    if currency_choice == "yes":
        filtered_transactions = list(filter_by_currency(filtered_transactions, "RUB"))

    keyword_choice = (
        input("Распечатывать список транзакций по определенному слову в описании? Yes / No\nВаш выбор: ")
        .strip()
        .lower()
    )

    if keyword_choice == "yes":
        keyword = input("Введите слово для фильтрации по описанию: ")
        filtered_transactions = filter_by_search_string(filtered_transactions, keyword)

    print("Распечатываю итоговый список транзакций...")

    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(list(filtered_transactions))}")
        for tx in filtered_transactions:
            print(f"{get_date(tx['date'])} {tx['description']}")
            if pd.isna(tx["from"]):
                line_from = ""
            elif tx.get("from"):
                words1 = re.match(r"\D*", tx["from"])
                if words1 is not None:
                    line_from = f'{words1.group(0)} {mask_account_card(tx["from"])} -> '
            else:
                line_from = ""
            if tx["to"]:
                words2 = re.match(r"\D*", tx["to"])
                if words2 is not None:
                    line_to = f'{words2.group(0)} {mask_account_card(tx["to"])}'
            else:
                line_to = ""
            print(f"{line_from}{line_to}")
            value = tx.get("operationAmount_amount")
            if value is not None:
                print(f"Сумма: {tx['operationAmount_amount']} {tx["operationAmount_currency_name"]}\n")
            else:
                print(f"Сумма: {tx['amount']} {tx["currency_name"]}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

    return


if __name__ == "__main__":
    main()
