import os

import requests
from dotenv import load_dotenv

load_dotenv()


def exchange_currency(to, from1, amount):
    """Function that takes rate from API and returns the exchange amount of RUBLES"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from1}&amount={amount}"

    headers = {"apikey": os.getenv("API_TOKEN")}

    response = requests.get(url, headers=headers)

    status_code = response.status_code
    if status_code:
        result = response.json().get("result")
    return result


if __name__ == "__main__":
    print(exchange_currency("RUB", "EUR", 100))
