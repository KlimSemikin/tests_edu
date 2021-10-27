import mysql.connector

from framework.config import sql_data
from framework.sql.crud_database import CRUDBaseTable
from framework.utils.random_generator import RanGen


class TestTable(CRUDBaseTable):
    def __init__(self):
        super().__init__(connector=mysql.connector, connect_data=sql_data.CONNECTION_DATA)
        self.columns = ['id', 'name', 'status_id', 'method_name', 'project_id', 'session_id', 'start_time', 'end_time',
                        'env', 'browser', 'author_id']
        self.table_name = 'test'

    def _data_parser(self, data_list):
        answer = [{self.columns[i]: data[i] for i in range(len(data))} for data in data_list]
        return answer

    def add_test_record(self, data):
        values = ''
        for column in self.columns[1:]:
            values += f"'{str(data[column])}'" + ', '
        values = values[:-2]

        return self.add(table=self.table_name, columns=self.columns[1:], values=values)

    def get_items_with_repeatable_ids(self, n, a, b):
        list_ids = RanGen.generate_n_random_repeatable_numbers_in_range(n, a, b)
        return self._data_parser(self.get(table=self.table_name, where=f"id in ({', '.join(list_ids)})"))

    def del_items(self, ids):
        self.delete(table=self.table_name, where=f"id in ({', '.join(ids)})")

    def update_item(self, id, column, value):
        self.edit(table=self.table_name, where=f"id = {id}", column=column, value="'" + str(value) + "'")
