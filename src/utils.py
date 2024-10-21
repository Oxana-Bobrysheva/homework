import json
import os

def get_transactions(url: str) -> list[dict]:
    """ Gets data information about transactions from operations.json"""
    if not os.path.isfile(url):
        # file is not found
        return []
    with open(url, 'r', encoding='UTF-8') as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                # if data is not a list
                return []
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            # Error in decoding json or reading file
            print(f"Error reading file: {e}")
            return []


if __name__ == "__main__":
    url = "../data/operations.json"
    transactions = get_transactions(url)
    if not transactions:
        print("No transactions found or file is empty.")
    else:
        print(transactions)
