import pandas as pd


def reading_xlsx(file_name):
    df = pd.read_excel(file_name)
    return df


if __name__ == "__main__":
    result = reading_xlsx("../data/transactions_excel.xlsx")
    print(result.head())
