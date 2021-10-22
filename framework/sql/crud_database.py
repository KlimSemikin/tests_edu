from framework.utils.sql_utils import Database

from abc import ABC


class CRUDBaseTable(ABC):
    def __init__(self, connector, connect_data):
        self.CONN_DATA = connector, connect_data

    def get(self, table, columns=None, where=None):
        with Database(*self.CONN_DATA) as db:
            where = f'WHERE {where} ' if where else ''

            sql = f"SELECT {'*' if not columns else ', '.join(columns)} FROM {table} {where}"
            return db.query(sql)

    def add(self, table, values, columns=None):
        with Database(*self.CONN_DATA) as db:
            sql = f"INSERT INTO {table} ({'' if not columns else ', '.join(columns)}) VALUES ({values})"
            db.query(sql)
            return db.cursor.lastrowid

    def edit(self, table, column, value, where=None):
        with Database(*self.CONN_DATA) as db:
            where = f'WHERE {where} ' if where else ''

            sql = f"UPDATE {table} SET {column} = {value} {where}"
            return db.query(sql)

    def delete(self, table, where=None):
        with Database(*self.CONN_DATA) as db:
            where = f'WHERE {where} ' if where else ''

            sql = f"DELETE FROM {table} {where}"
            return db.query(sql)
