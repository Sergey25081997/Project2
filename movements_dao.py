from datetime import datetime
from commands import INSERT_MOVEMENT
from commands.select_movements import SELECT_MOVEMENT_BY_DATETIME, SELECT_MOVEMENTS, SELECT_MOVEMENTS_BY_ITEM_ID
from data_types import BaseMovement, Movement
from database import BaseDatabase


class MovementsDAO(BaseDatabase):
    def get_all_movements(self) -> list[Movement]:
        session_maker = self.session_maker()
        _, cursor = next(session_maker)
        cursor.execute(SELECT_MOVEMENTS)
        return [Movement.from_tuple(row) for row in cursor.fetchall()]

    def get_movement_by_datetime(self, date: datetime) -> Movement:
        session_maker = self.session_maker()
        _, cursor = next(session_maker)
        cursor.execute(SELECT_MOVEMENT_BY_DATETIME, (date.isoformat(),))
        return Movement.from_tuple(cursor.fetchone())

    def create_movement(self, movement: BaseMovement) -> Movement:
        session_maker = self.session_maker()
        session, cursor = next(session_maker)
        cursor.execute(
            INSERT_MOVEMENT,
            (
                movement.item_id,
                movement.created_at.isoformat(),
                movement.count,
                movement.type.value,
            ),
        )
        session.commit()
        return self.get_movement_by_datetime(movement.created_at)
    
    # Этот метод позволяет получить все перемещения для указанного ID товара.
    def get_movements_by_item_id(self, item_id: int) -> list[Movement]:
        session_maker = self.session_maker()
        _, cursor = next(session_maker)
        cursor.execute(SELECT_MOVEMENTS_BY_ITEM_ID, (item_id,))
        return [Movement.from_tuple(row) for row in cursor.fetchall()]
