from sqlite3 import OperationalError
from database import BaseDatabase
from commands import CREATE_TABLES_COMMANDS


class TablesDAO(BaseDatabase):
    def create_tables(self) -> None:
        session_maker = self.session_maker()
        session, cur = next(session_maker)
        for command in CREATE_TABLES_COMMANDS:
            try:
                cur.execute(command)
            except OperationalError:
                pass
        session.commit()
