import datetime

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


def text_to_word_search_arr(text_piece):
    word_str = '('
    for word in text_piece:
        word_str += word
        if word != text_piece[-1]:
            word_str += ' & '
        else:
            word_str += ')'
    print word_str
    return word_str


class concrete_view(View):

    def __init__(self):
        pass

    db_schema = 'none'

    def launch_joint_search_prompt(self):
        is_active = prompt([{
            'type': 'input',
            'name': 'is_active',
            'message': 'Is player active'
        }])['is_active']
        team_name = prompt([{
            'type': 'input',
            'name': 'team_name',
            'message': 'Team name'
        }])['team_name']
        print is_active
        print team_name
        return {'player_is_active': is_active, 'team_name': team_name}

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
        upd_cols_prompt = self.create_columns_chk_prompt(table_chosen)
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
        print sel_by
        cond_data = []
        if not sel_by:
            condition_string = 'False'
        elif 'All' not in sel_by:
            for x in range(0, len(sel_by), 1):
                condition = prompt([{
                    'type': 'input',
                    'name': 'cond',
                    'message': 'enter the condition for selecting by {0}'.format(sel_by[x])
                }])['cond']
                cond_data.append({'row': sel_by[x], 'cond': condition})
            condition_string = '('
            for cond in cond_data:
                condition_string += cond['row'] + " " + cond['cond']
                if cond != cond_data[-1]:
                    condition_string += ' AND '
            condition_string += ')'
        else:
            condition_string = 'True'
        limit = prompt([{
            'type': 'input',
            'name': 'limit',
            'message': 'limit number of rows read'
        }])['limit']
        end_data = {
            'cond': condition_string,
            'limit': limit
        }
        return end_data

    def launch_text_search_prompt(self, table_chosen):
        col_pr = self.create_columns_prompt(table_chosen)
        column_to_search = prompt(col_pr)['col_pr']
        type = prompt([{
            'type': 'list',
            'name': 'type',
            'message': 'Choose full text search type',
            'choices': [
                {
                    'name': 'Is not in text '
                },
                {
                    'name': 'Is in'
                }
            ]
        }])['type']
        print type
        text_piece = None
        if type == 'Is not in text':
            text_piece = prompt([{
                'type': 'input',
                'name': 'txt',
                'message': 'Enter text to not include in search'
            }])['txt']
        else:
            text_piece = prompt([{
                'type': 'input',
                'name': 'txt',
                'message': 'Enter text to search'
            }])['txt']
        text_piece = text_piece.split()
        text_piece = text_to_word_search_arr(text_piece)
        data = {'in': type == 'Is in', 'col': column_to_search, 'textp': text_piece}
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

    def create_columns_chk_prompt(self, table_name):
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

    def create_columns_prompt(self, table_name):
        schema = self.db_schema[table_name]
        col_pr = [
            {
                'type': 'list',
                'message': 'select column for fulltext search',
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
                'type': 'checkbox',
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
                    'name': 'Joint search'
                },
                {
                    'name': 'Text search'
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
        columns_str = 'id    '
        for elem in self.db_schema[table_name]:
            columns_str += elem + '   '
        print columns_str
        print('-----------------------------')
        for item in data:
            itemstr = ''
            for col in item:
                if type(col) == datetime.date:
                    textdata = col.strftime("%d-%m-%Y")
                else:
                    textdata = col.__repr__()
                itemstr += textdata + ' | '
            print itemstr
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
