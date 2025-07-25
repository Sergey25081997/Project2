INSERT_MOVEMENT = """
INSERT INTO movement (
        item_id,
        created_at,
        count,
        type )
VALUES (?, ?, ?, ?)
"""
