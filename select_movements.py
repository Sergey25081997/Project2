SELECT_MOVEMENT_BY_DATETIME = """
SELECT item_id, created_at, count, type, id
FROM movement
WHERE created_at = ?
"""
SELECT_MOVEMENTS = """
SELECT item_id, created_at, count, type, id
FROM movement
"""
# Этот запрос будет искать все перемещения для конкретного товара по его ID.
SELECT_MOVEMENTS_BY_ITEM_ID = """
SELECT item_id, created_at, count, type, id
FROM movement
WHERE item_id = ?
"""
