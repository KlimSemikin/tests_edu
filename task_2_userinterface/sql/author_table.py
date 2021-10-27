import mysql.connector

from framework.config import sql_data
from framework.sql.crud_database import CRUDBaseTable


class AuthorTable(CRUDBaseTable):
    def __init__(self):
        super().__init__(connector=mysql.connector, connect_data=sql_data.CONNECTION_DATA)
        self.columns = ['id', 'name', 'login', 'email']
        self.table_name = 'author'

    def get_author_id_and_add_if_needs(self):
        author_id = self.get(table=self.table_name, columns=('id',), where=f"name = '{sql_data.AUTHOR_NAME}'")
        if not author_id:
            author_id = self.add(table=self.table_name, columns=self.columns[1:],
                                 values=f"'{sql_data.AUTHOR_NAME}', '{sql_data.LOGIN}', '{sql_data.EMAIL}'")
        else:
            author_id = author_id[0][0]
        return author_id
