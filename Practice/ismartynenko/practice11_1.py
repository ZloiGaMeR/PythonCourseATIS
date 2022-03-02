import sqlite3
import json


class SqlWrapper:
    # При входе в наш менеджер контекста - создаем соединение с БД
    def __enter__(self):
        self._db_name = "films.db"
        self.conn = sqlite3.connect(self._db_name)
        self.conn.row_factory = sqlite3.Row

    # При выходе - завершаем соединение
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    # метод select
    def select(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        return json.dumps(cur.fetchall())

    # метод execute
    def execute(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()


with SqlWrapper():
    SqlWrapper.execute("INSERT INTO films (name, desc) VALUES ('Cool Film', 'SHORT LONG STORY')")
    SqlWrapper.select("SELECT * FROM films")
