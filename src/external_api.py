import os

import requests
from dotenv import load_dotenv

load_dotenv()


def exchange_currency(to, from1, amount):
    """Function that takes rate from API and returns the exchange amount of RUBLES"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from1}&amount={amount}"

    headers = {"apikey": os.getenv("API_TOKEN")}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json().get("result")
        return result
    else:
        return None

if __name__ == "__main__":
    print(exchange_currency("RUB", "EUR", 100))
