from PyInquirer import prompt
from view import View

def create_add_cols_prompt(columns_array):
    add_pr = [

    ]
    for element in columns_array:
        add_pr.append({
            'type': 'input',
            'name': element,
            'message': 'Enter value for {0}'.format(element)
        })
    return add_pr


class concrete_view(View):

    def __init__(self):
        pass

    db_schema = 'none'

    def set_data(self, schema_data):
        self.db_schema = schema_data
        self.fill_table_prompt()

    def fill_table_prompt(self):
        for element in self.db_schema:
            self.tables[0]['choices'].insert(0, element)

    def launch_insert_prompt(self, table_chosen):
        add_prompt = self.create_add_prompt(table_chosen)
        data_dict = prompt(add_prompt)
        return data_dict

    def launch_update_prompt(self, table_chosen):
        upd_selection_prompt = self.create_select_prompt(table_chosen)
        upd_by = prompt(upd_selection_prompt)['sel_pr']
        if upd_by != 'All':
            condition = prompt([{
                'type': 'input',
                'name': 'cond',
                'message': 'enter the condition for selecting by {0}'.format(upd_by)
            }])['cond']
            condition = upd_by + condition
        else:
            condition = 'True'
        upd_cols_prompt = self.create_columns_prompt(table_chosen)
        cols = prompt(upd_cols_prompt)['col_pr']
        new_data_prompt = create_add_cols_prompt(cols)
        columns = prompt(new_data_prompt)
        return {'columns': columns, 'condition': condition}

    def launch_delete_prompt(self, table_chosen):
        delete_prompt = self.create_delete_prompt(table_chosen)
        del_by = prompt(delete_prompt)['del_pr']
        if del_by != 'All':
            condition = prompt([{
                'type': 'input',
                'name': 'cond',
                'message': 'enter the condition for deleting by {0}'.format(del_by)
            }])['cond']
            data = del_by + condition
        else:
            data = 'True'
        return data

    def launch_select_prompt(self, table_chosen):
        select_prompt = self.create_select_prompt(table_chosen)
        sel_by = prompt(select_prompt)['sel_pr']
        if sel_by != 'All':
            condition = prompt([{
                'type': 'input',
                'name': 'cond',
                'message': 'enter the condition for selecting by {0}'.format(sel_by)
            }])['cond']
            data = sel_by + condition
        else:
            data = 'True'
        limit = prompt([{
            'type': 'input',
            'name': 'limit',
            'message': 'limit number of rows read'
        }])['limit']
        data += " LIMIT " + limit
        return data

    def launch_operation_prompt(self):
        return prompt(self.operations)['operation']

    def launch_table_prompt(self):
        return prompt(self.tables)['table']

    def create_delete_prompt(self, table_name):
        schema = self.db_schema[table_name]
        del_pr = [
            {
                'type': 'list',
                'message': 'choose deletion method',
                'name': 'del_pr',
                'choices': [
                    {
                        'name': 'All'
                    },
                    {
                        'name': 'id'
                    }
                ]
            }
        ]
        for col in schema:
            obj = {
                'name': col
            }
            del_pr[0]['choices'].append(obj)
        return del_pr

    def create_add_prompt(self, table_name):
        schema = self.db_schema[table_name]
        add_pr = [

        ]
        for element in schema:
            add_pr.append({
                'type': 'input',
                'name': element,
                'message': 'Enter value for {0}'.format(element)
            })
        return add_pr

    def create_columns_prompt(self, table_name):
        schema = self.db_schema[table_name]
        col_pr = [
            {
                'type': 'checkbox',
                'message': 'select columns to update',
                'name': 'col_pr',
                'choices': [
                ]
            }
        ]
        for elem in schema:
            col_pr[0]['choices'].append({
                'name': elem
            })
        return col_pr

    def create_select_prompt(self, table_name):
        schema = self.db_schema[table_name]
        sel_pr = [
            {
                'type': 'list',
                'message': 'choose selection method',
                'name': 'sel_pr',
                'choices': [
                    {
                        'name': 'All',
                        'data': ''
                    },
                    {
                        'name': 'id'
                    }
                ]
            }
        ]
        for col in schema:
            obj = {
                'name': col
            }
            sel_pr[0]['choices'].append(obj)
        return sel_pr

    tables = [
        {
            'type': 'list',
            'message': 'Select table',
            'name': 'table',
            'choices': [
                {
                    'name': 'Exit'
                }
            ]
        }
    ]

    operations = [
        {
            'type': 'list',
            'message': 'Select operation',
            'name': 'operation',
            'choices': [
                {
                    'name': 'Preview'
                },
                {
                    'name': 'Add'
                },
                {
                    'name': 'Add Random'
                },
                {
                    'name': 'Update'
                },
                {
                    'name': 'Delete'
                },
                {
                    'name': 'Back'
                }
            ]
        }
    ]

    def display_select_data(self, data, table_name):
        print('Data from table: {0}'.format(table_name))
        print('-----------------------------')
        str = 'id    '
        for elem in self.db_schema[table_name]:
            str += elem + '   '
        print (str)
        print('-----------------------------')
        for item in data:
            print item
        print('-----------------------------')

    def display_delete_data(self, data, table_name):
        print('-----------------------------')
        print('Deleted items where {0} from table: {1}'.format(data, table_name))
        print('-----------------------------')

    def display_insert_data(self, data, table_name):
        print('-----------------------------')
        print('Inserted {0} into table: {1}'.format(data, table_name))
        print('-----------------------------')

    def display_update_data(self, columns, condition, table_name):
        print('-----------------------------')
        print('Updated items {0} to {1} where {2} in table: {3}'.format(columns.keys(),
                                                                        columns.values(),
                                                                        condition,
                                                                        table_name))
        print('-----------------------------')
