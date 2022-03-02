import sqlite3


class SqlWrapper:
    def __init__(self):
        self.conn = conn

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def select(self):
        pass

    def execute(self):
        cur = self.cursor()


db_name = "films.db"
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row

req = SqlWrapper
# req.execute("INSERT INTO films VALUES ")
