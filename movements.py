from dao.movements_dao import MovementsDAO
from data_types import BaseMovement, Movement, MovementType
from utils import get_user_choice
from datetime import datetime

MOVEMENTS_MENU = """1. Перемещения товара
2. Создать перемещение товара
3. Перемещения по ID товара
0. Выход"""
MOVEMENTS_CHOICES = {0, 1, 2, 3}


def print_movement(m: Movement) -> None:
    # Преобразуем дату в понятный формат
    date_str = m.created_at.strftime("%d.%m.%Y %H:%M")
    # Определяем тип операции
    operation_type = "Приход" if m.type == MovementType.income else "Расход"
    # Выводим информацию
    print(f"[{m.id}] {operation_type} {m.count} шт. (Товар ID: {m.item_id}, {date_str})")
    # Теперь информация о перемещении будет выводиться в понятном формате.


def print_list_movements(movements: list[Movement]) -> None:
    for m in movements:
        print_movement(m)


def get_movement_data() -> BaseMovement:
    item_id = int(input("ID товара: "))
    created_at = datetime.now()
    count = int(input("Количество: "))
    if (type_number := int(input("Тип: 1 - приход, 2 - уход\n: "))) not in {1, 2}:
        raise ValueError
    type_ = MovementType.income if type_number == 1 else MovementType.outcome
    return BaseMovement(item_id, created_at, count, type_)


def movements_menu(movements_dao: MovementsDAO) -> None:
    while True:
        print(MOVEMENTS_MENU)
        user_input = get_user_choice(MOVEMENTS_CHOICES)
        match user_input:
            case 0:
                break
            case 1:
                movements = movements_dao.get_all_movements()
                print_list_movements(movements)
            case 2:
                base_movement = get_movement_data()
                movement = movements_dao.create_movement(base_movement)
                print_movement(movement)
            case 3:  
                try:
                    item_id = int(input("Введите ID товара: "))
                    movements = movements_dao.get_movements_by_item_id(item_id)
                    
                    if movements:  # Если есть перемещения
                        print(f"\nПеремещения для товара ID {item_id}:")
                        print_list_movements(movements)
                    else:
                        print("\nДля этого товара перемещений не найдено")
                        
                except ValueError:  # Если ввели не число
                    print("Ошибка! ID должен быть числом")
