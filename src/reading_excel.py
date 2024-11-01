from typing import Any

import pandas as pd


def reading_xlsx(file_name: str) -> Any:
    """This function allows to read data from Excel files and returns a list of
    dictionaries."""
    transactions = []
    try:
        df = pd.read_excel(file_name)
        for index, row in df.iterrows():
            transactions.append(row.to_dict())
    except FileNotFoundError:
        print(f"File {file_name} was not found.")
    except Exception as e:
        print(f"Error occurred: {e}.")
    return transactions


if __name__ == "__main__":
    result = reading_xlsx("../data/transactions_excel.xlsx")
    print(result[:3])
