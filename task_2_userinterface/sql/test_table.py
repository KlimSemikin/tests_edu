from framework.sql.crud_database import CRUDBaseTable
from task_2_userinterface.tests import test_data
import mysql.connector
from framework.utils.random_generator import RanGen
import getpass


class TestTable(CRUDBaseTable):
    def __init__(self):
        super().__init__(connector=mysql.connector, connect_data=test_data.CONNECTION_DATA)
        self._project_name = test_data.PROJECT_NAME
        self._author = getpass.getuser()
        self.columns = ['id', 'name', 'status_id', 'method_name', 'project_id', 'session_id', 'start_time', 'end_time',
                        'env', 'browser', 'author_id']

    def _data_parser(self, data_list):
        answer = [{self.columns[i]: data[i] for i in range(len(data))} for data in data_list]
        return answer

    def get_project_id_and_add_if_needs(self):
        project_id = self.get(table='project', columns=('id',), where=f"name = '{self._project_name}'")
        if not project_id:
            project_id = self.add(table='project', columns=('name',), values=f"'{self._project_name}'")
        else:
            project_id = project_id[0][0]
        return project_id

    def get_author_id_and_add_if_needs(self):
        author_id = self.get(table='author', columns=('id',), where=f"name = '{self._author}'")
        if not author_id:
            author_id = self.add(table='author', columns=('name', 'login', 'email'),
                                 values=f"'{self._author}', '{self._author}', '{test_data.email2}'")
        else:
            author_id = author_id[0][0]
        return author_id

    def get_session_id_and_add_if_needs(self, start_time, build_number):
        session_id = self.get(table='session', columns=('id',),
                              where=f"session_key = '{start_time}'")
        if not session_id:
            session_id = self.add(table='session', columns=('session_key', 'created_time', 'build_number'),
                                  values=f"'{start_time}', '{start_time}', '{build_number}'")
        else:
            session_id = session_id[0][0]
        return session_id

    def get_status_id(self, status):
        return self.get(table='status', columns=('id',), where=f"name = '{status.upper()}'")[0][0]

    def add_test_record(self, data):
        if 'project_id' not in data:
            project_id = self.get_project_id_and_add_if_needs()
        else:
            project_id = data['project_id']
        if 'session_id' not in data:
            session_id = self.get_session_id_and_add_if_needs(data['session_start_time'], 2)
        else:
            session_id = data['session_id']
        if 'status_id' not in data:
            status_id = self.get_status_id(data['status'])
        else:
            status_id = data['status_id']
        if 'author_id' not in data:
            author_id = self.get_author_id_and_add_if_needs()
        else:
            author_id = data['author_id']

        return self.add(table='test', columns=self.columns[1:],
                        values=f"'{data['name']}', {str(status_id)}, '{data['method_name']}', "
                               f"{str(project_id)}, {str(session_id)}, '{data['start_time']}', "
                               f"'{data['end_time']}', '{data['env']}', '{data['browser']}', '{str(author_id)}'")

    def get_items_with_repeatable_ids(self, n):
        list_ids = RanGen.generate_n_random_repeatable_numbers_in_range(n, a=1, b=9)
        return self._data_parser(self.get(table='test', where=f"id in ({', '.join(list_ids)})"))

    def del_items(self, ids):
        self.delete(table='test', where=f"id in ({', '.join(ids)})")

    def update_item(self, id, column, value):
        self.edit(table='test', where=f"id = {id}", column=column, value="'" + str(value) + "'")
