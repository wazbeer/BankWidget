from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime

def mask_account_card(data: str) -> str:
    parts = data.split()
    num = parts[-1]
    name = " ".join(parts[:-1])
    if name == "Счет":
        return f"{name} {get_mask_account(num)}"
    else:
        return f"{name} {get_mask_card_number(num)}"

def get_date(date_string: str) -> str:
    date_obj = datetime.fromisoformat(date_string)
    parsed_date = datetime.strftime(date_obj, "%Y.%m.%d")
    return parsed_date

if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(get_date("2024-03-11T02:26:18.671407"))