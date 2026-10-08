import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_currency(transaction: dict) -> float:
    """принимает словарь с транзакцией и возвращает флоат рублей, обращается к серверу если транзакция в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        payload: dict = {}
        headers: dict = {
            "apikey": os.getenv("API_KEY"),
        }

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={transaction['operationAmount']['currency']['code']}&amount={transaction['operationAmount']['amount']}"

        response = requests.request("GET", url, headers=headers, data=payload)

        data = response.json()

        return float(data["result"])
