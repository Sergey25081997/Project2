CREATE_TABLES_COMMANDS = (
    """
    CREATE TABLE item (
        id INTEGER PRIMARY KEY,
        title TEXT,
        weight INTEGER,
        CONSTRAINT item_title UNIQUE (title)
    )""",
    """
    CREATE TABLE movement (
        id INTEGER PRIMARY KEY,
        item_id INTEGER,
        created_at TEXT,
        count INTEGER,
        type TEXT,
        FOREIGN KEY (item_id) REFERENCES item(id)
    )""",
)
