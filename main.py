from dao import TablesDAO
from dao import ItemsDAO
from dao.movements_dao import MovementsDAO
from services import item_menu, movements_menu
from utils import get_user_choice

from settings import DB_PATH

MENU = """1. Работа с товарами
2. Работа с перемещениями
0. Выход"""
MENU_CHOICES = {0, 1, 2}


def main():
    print("Привет! Это программа для помощи учета товара на складе")
    tables_dao = TablesDAO(DB_PATH)
    items_dao = ItemsDAO(DB_PATH)
    movements_dao = MovementsDAO(DB_PATH)
    tables_dao.create_tables()
    while True:
        print(MENU)
        user_input = get_user_choice(MENU_CHOICES)
        if user_input == 0:
            break
        if user_input == 1:
            item_menu(items_dao)
        if user_input == 2:
            movements_menu(movements_dao)

    print("Завершение работы программы...")


if __name__ == "__main__":
    main()
