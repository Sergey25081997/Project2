SELECT_ALL_ITEMS = """
SELECT title, weight, id
FROM item
"""
SELECT_ITEMS_BY_TITLE = """
SELECT title, weight, id
FROM item
WHERE title LIKE ?
"""
SELECT_ITEMS_BY_ID = """
SELECT title, weight, id
FROM item
WHERE id = ?
"""
