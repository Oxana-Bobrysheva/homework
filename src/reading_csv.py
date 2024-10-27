import pandas as pd


def reading_csv(file_name):
    df = pd.read_csv(file_name)
    return df


if __name__ == "__main__":
    result = reading_csv("../data/transactions.csv")
    print(result.head())
