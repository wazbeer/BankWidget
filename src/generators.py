def filter_by_currency(transactions: list, currency: str):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction

def transaction_descriptions(transactions: list):
    for transaction in transactions:
        yield transaction["description"]

def card_number_generator(start: int, stop: int) -> str:
    for number in range(start, stop + 1):
        number = str(number).zfill(16)
        number = f"{number[0:4]} {number[4:8]} {number[8:12]} {number[12:16]}"
        yield number

if __name__ == "__main__":
    usd = filter_by_currency(transactions, "USD")
    print(next(usd))  # первая USD-транзакция
    print(next(usd))  # вторая
    descriptions = transaction_descriptions(transactions)
    for i in range(5):
        print(next(descriptions))
    for card_number in card_number_generator(1, 5):
        print(card_number)
