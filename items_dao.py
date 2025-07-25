from data_types import BaseItem, Item, NullableBaseItem
from database import BaseDatabase
from commands import (
    SELECT_ALL_ITEMS,
    SELECT_ITEMS_BY_TITLE,
    SELECT_ITEMS_BY_ID,
    INSERT_ITEM,
    UPDATE_ITEM_BY_ID,
    DELETE_ITEM_BY_ID
)


class ItemsDAO(BaseDatabase):
    def get_all_items(self) -> list[Item]:
        session_maker = self.session_maker()
        _, cursor = next(session_maker)
        cursor.execute(SELECT_ALL_ITEMS)
        result = cursor.fetchall()
        return [Item(*args) for args in result]

    def get_items_by_title(self, title: str) -> list[Item]:
        session_maker = self.session_maker()
        _, cursor = next(session_maker)
        cursor.execute(SELECT_ITEMS_BY_TITLE, (f"%{title}%",))
        result = cursor.fetchall()
        return [Item(*args) for args in result]

    def get_item_by_id(self, id_: int) -> Item:
        session_maker = self.session_maker()
        _, cursor = next(session_maker)
        cursor.execute(SELECT_ITEMS_BY_ID, (id_,))
        return Item(*cursor.fetchone())

    def create_item(self, item: BaseItem) -> Item:
        session_maker = self.session_maker()
        session, cursor = next(session_maker)
        cursor.execute(INSERT_ITEM, (item.title, item.weight))
        session.commit()
        cursor.execute(SELECT_ITEMS_BY_TITLE, (item.title,))
        return Item(*cursor.fetchone())

    def update_item(self, item_to_update: NullableBaseItem):
        session_maker = self.session_maker()
        session, cursor = next(session_maker)
        values = []
        parametrs = []
        if not item_to_update.title and not item_to_update.weight:
            raise ValueError("Вы ничего не изменили")
        if item_to_update.title:
            values.append("title = ?")
            parametrs.append(item_to_update.title)
        if item_to_update.weight:
            values.append("weight = ?")
            parametrs.append(item_to_update.weight)
        parametrs.append(item_to_update.id)
        cursor.execute(UPDATE_ITEM_BY_ID.format(",".join(values)), parametrs)
        session.commit()
        cursor.execute(SELECT_ITEMS_BY_ID, (item_to_update.id,))
        return Item(*cursor.fetchone())
    
    def delete_item(self, item_id: int) -> None:
        session_maker = self.session_maker()
        session, cursor = next(session_maker)
        cursor.execute(DELETE_ITEM_BY_ID, (item_id,))
        session.commit()
