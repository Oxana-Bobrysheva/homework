import csv


def read_financial_operations(file_path: str) -> list:
    transactions = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    return transactions


if __name__ == "__main__":
    result = read_financial_operations("../data/transactions.csv")
    print(result)
