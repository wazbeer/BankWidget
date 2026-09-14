from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime

def mask_account_card(data: str) -> str:
    num = data.split(" ")[-1]
    name = data.split(" ")[0]
    if name == "Счет":
        return f"{name} {get_mask_account(num)}"
    else:
        return f"{name} {get_mask_card_number(num)}"



if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
