from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Функция принимает счёт либо карту и возвращает комбинрованное значение имени и счёта"""
    parts = data.split()
    num = parts[-1]
    name = " ".join(parts[:-1])
    if name == "Счет":
        return f"{name} {get_mask_account(num)}"
    else:
        return f"{name} {get_mask_card_number(num)}"


def get_date(date_string: str) -> str:
    """Функция принимает ISO формат времени и возвращет форматированную дату"""
    date_obj = datetime.fromisoformat(date_string)
    parsed_date = datetime.strftime(date_obj, "%d.%m.%Y")
    return parsed_date
