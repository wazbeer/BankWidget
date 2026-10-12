from src.processing import filter_by_state, sort_by_date
from src.readers import csv_reader, excel_reader
from src.services import desc_search
from src.utils import get_financial_transactions
from src.widget import get_date, mask_account_card


def main() -> None:
    n = int(
        input(
            "Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )
    )

    if n == 1:
        transactions = get_financial_transactions("../data/operations.json")
    elif n == 2:
        transactions = csv_reader("../data/transactions.csv")
    elif n == 3:
        transactions = excel_reader("../data/transactions_excel.xlsx")
    else:
        print("Неверный ввод!")
        exit(0)

    while True:
        filtration_status = input("Введите статус... ").upper().strip()
        if filtration_status in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Операции отфильтрованы по статусу '{filtration_status}'")
            transactions = filter_by_state(transactions, filtration_status)
            break
        else:
            print(f"Статус операции '{filtration_status}' недоступен")

    is_sort = input("Отсортировать операции по дате? Да/Нет\n").lower()
    if is_sort == "да":
        order = input("Отсортировать по возрастанию или по убыванию?\n").lower()
        is_reverse = False if order == "по возрастанию" else True
        transactions = sort_by_date(transactions, reverse=is_reverse)

    is_rub = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
    if is_rub == "да":

        transactions = [
            t
            for t in transactions
            if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB" or t.get("currency_code") == "RUB"
        ]

    is_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
    if is_word == "да":
        word = input("Введите слово для поиска:\n")
        transactions = desc_search(transactions, word)

    print("Распечатываю итоговый список транзакций...\n")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}\n")
        for t in transactions:
            date_str = get_date(t.get("date", ""))
            description = t.get("description", "")

            sender = mask_account_card(t["from"]) if t.get("from") else ""
            recipient = mask_account_card(t["to"]) if t.get("to") else ""
            from_to = f"{sender} -> {recipient}" if sender else recipient

            if "operationAmount" in t:
                amount = t["operationAmount"]["amount"]
                currency = t["operationAmount"]["currency"]["name"]
            else:
                amount = t.get("amount")
                currency = t.get("currency_name", "руб.")

            print(f"{date_str} {description}")
            print(f"{from_to}")
            print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
