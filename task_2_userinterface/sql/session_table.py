import mysql.connector

from framework.config import sql_data
from framework.sql.crud_database import CRUDBaseTable


class SessionTable(CRUDBaseTable):
    def __init__(self):
        super().__init__(connector=mysql.connector, connect_data=sql_data.CONNECTION_DATA)
        self.columns = ['id', 'session_key', 'created_time', 'build_number']
        self.table_name = 'session'

    def get_session_id_and_add_if_needs(self, start_time):
        session_id = self.get(table=self.table_name, columns=('id',), where=f"session_key = '{start_time}'")
        if not session_id:
            session_id = self.add(table=self.table_name, columns=self.columns[1:],
                                  values=f"'{start_time}', '{start_time}', {sql_data.BUILD_NUMBER}")
        else:
            session_id = session_id[0][0]
        return session_id
