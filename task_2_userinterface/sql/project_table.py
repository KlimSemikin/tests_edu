import mysql.connector

from framework.config import sql_data
from framework.sql.crud_database import CRUDBaseTable


class ProjectTable(CRUDBaseTable):
    def __init__(self):
        super().__init__(connector=mysql.connector, connect_data=sql_data.CONNECTION_DATA)
        self.columns = ['id', 'name']
        self.table_name = 'project'

    def get_project_id_and_add_if_needs(self):
        project_id = self.get(table=self.table_name, columns=('id',), where=f"name = '{sql_data.PROJECT_NAME}'")
        if not project_id:
            project_id = self.add(table=self.table_name, columns=('name',), values=f"'{sql_data.PROJECT_NAME}'")
        else:
            project_id = project_id[0][0]
        return project_id
