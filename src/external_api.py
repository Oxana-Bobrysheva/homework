import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def exchange_currency(transaction: dict) -> float:
    """Function that takes rate from API and returns the exchange amount of RUBLES"""

    amount = transaction['operationAmount']['amount']
    from_currency = transaction['operationAmount']['currency']['code']
    if from_currency == 'RUB':
        return float(amount)
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={from_currency}&amount={amount}"

        headers = {"apikey": os.getenv("API_TOKEN")}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            result = response.json().get("result")
            return result
        else:
            return None


if __name__ == "__main__":
    print(os.getenv("API_TOKEN"))
    with open('../data/operations.json', 'r', encoding='UTF-8') as file:
        operations = json.load(file)
        for o in operations[:5]:
            print(exchange_currency(o))
