import json
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("/home/user/PycharmProjects/homework_new/logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def flatten_dict(d: dict, parent_key: str = "", sep: str = "_") -> dict:
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items


def get_transactions(url: str) -> list[dict]:
    """Gets data information about transactions from operations.json"""
    logger.info("Starting the function get_transactions")
    if not os.path.isfile(url):
        # file is not found
        logging.warning("There is no such file")
        return []
    with open(url, "r", encoding="UTF-8") as file:
        try:
            logger.info("Downloading data from file")
            data = json.load(file)
            if isinstance(data, list):
                # flat the dictionaries
                flat_data: list = []
                for d in data:
                    dd = flatten_dict(d, parent_key="", sep="_")
                    flat_data.append(dd)

                return flat_data
            else:
                # if data is not a list
                logging.warning("Data is not a list")
                return []

        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            # Error in decoding json or reading file
            logger.error(f"An Error has occurred {e}")
            print(f"Error reading file: {e}")
            return []


if __name__ == "__main__":
    url = "../data/operations.json"
    transactions = get_transactions(url)
    if not transactions:
        print("No transactions found or file is empty.")
    else:
        print(transactions)
