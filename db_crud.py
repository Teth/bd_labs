import psycopg2
from controller import Controller


def array_to_tuple(schema_array):
    str_schema = '('
    for x in range(0, len(schema_array) - 1):
        str_schema = str_schema + schema_array[x] + ', '
    str_schema = str_schema + schema_array[len(schema_array) - 1]
    str_schema = str_schema + ')'
    return str_schema


class DBOperations(Controller):
    schemas = {'teams': ['name', 'city', 'cr_date'],
               'game': ['score_a', 'score_b', 'match_date'],
               'player': ['age', 'first_name', 'surname', 'phone_number', 'is_active'],
               'stadium': ['capacity', 'address', 'phone_number']
               }

    def __init__(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="111",
                                               host="127.0.0.1",
                                               port="5432",
                                               database="Sports")
            self.cursor = self.connection.cursor()

        except (Exception, psycopg2.Error) as error:
            print ("Error while connecting to PostgreSQL", error)

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")

    def get_schemas(self):
        return self.schemas

    def read(self, table, data):
        query = "select * from {0}" \
                " WHERE {1} " \
            .format(table, data)
        self.cursor.execute(query)
        rec = self.cursor.fetchall()
        return rec

    def insert(self, table, data):
        if table in self.schemas:
            query = "insert into {0}" \
                    " values {1}" \
                .format(table + array_to_tuple(self.schemas[table]), data)
            res = self.cursor.execute(query)
            self.connection.commit()
            return True
        else:
            raise Exception('SQL error during insert operation')

    def update(self, table, columns, condition):
        if table in self.schemas:
            query = "update {0}" \
                    " set {1}" \
                    " where {2}" \
                .format(table, columns, condition)
            self.cursor.execute(query)
            self.connection.commit()
            return True
        else:
            raise Exception('SQL error during delete operation')

    '''
    pass table name and condition as in 'id>1' or 'name=John'
    '''
    def delete(self, table, data_condition):
        if table in self.schemas:
            query = "delete from {0}" \
                    " where {1}" \
                .format(table, data_condition)
            res = self.cursor.execute(query)
            self.connection.commit()
            return True
        else:
            raise Exception('SQL error during delete operation')

    def force_commit(self):
        self.connection.commit()