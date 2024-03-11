import mysql.connector

from framework.config import sql_data
from framework.sql.crud_database import CRUDBaseTable


class StatusTable(CRUDBaseTable):
    def __init__(self):
        super().__init__(connector=mysql.connector, connect_data=sql_data.CONNECTION_DATA)
        self.columns = ['id', 'name']
        self.table_name = 'status'

    def get_status_id(self, status):
        return self.get(table=self.table_name, columns=(self.columns[0],), where=f"name = '{status.upper()}'")[0][0]
