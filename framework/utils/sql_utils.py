from framework.utils.logger import Logger
from mysql.connector import Error


class Database:
    def __init__(self, controller, kwargs):
        self._conn = controller.connect(**kwargs)
        self._cursor = self._conn.cursor()
        Logger.info(f"Выполнено подлючение к базе данных с помощью {controller.__name__}: {self._log_info()}.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def _log_info(self):
        self.execute("select database();")
        return self.fetchone()

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        Logger.info(f"Закрытие подключения к бд.")
        if commit:
            self.commit()
        self.cursor.close()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        Logger.info(f"Запрос к базе данных: '{sql}'.")
        self.execute(sql, params or ())
        result = self.fetchall()
        Logger.info(f"Результат запроса от базы данных: {result[:20]}")
        return result
