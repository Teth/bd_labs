from controller import Controller
from conView import concrete_view
from db_crud import DBOperations
import randomTableFiller
dbo = DBOperations()

controller = Controller()
controller.set_model(dbo)

view = concrete_view()

view.set_data(controller.get_schemas())

def get_table_class(table_chosen):
    if table_chosen == 'teams':
        return randomTableFiller.RandomTeam
    if table_chosen == 'game':
        return randomTableFiller.RandomGame
    if table_chosen == 'player':
        return randomTableFiller.RandomPlayer
    if table_chosen == 'stadium':
        return randomTableFiller.RandomStadium

def tuple_from_table_dictionary(table_name, table_dictionary):
    schema = controller.get_schemas()[table_name]
    data_tuple = "("
    for x in range(0, len(schema) - 1):
        data_tuple += table_dictionary[schema[x]] + ", "
    data_tuple += table_dictionary[schema[len(schema) - 1]]
    data_tuple += ")"
    return data_tuple


def key_value_string_from_dictionary(dictionary):
    kv_string = ""
    for elem in dictionary:
        kv_string += elem + '=' + dictionary[elem]
        if elem != dictionary.keys()[-1]:
            kv_string += ', '
    return kv_string


def run():
    while True:
        table_chosen = view.launch_table_prompt()
        if table_chosen == 'Exit':
            break
        operation_chosen = view.launch_operation_prompt()
        try:
            if operation_chosen != 'Back':
                if operation_chosen == 'Preview':
                    data = view.launch_select_prompt(table_chosen)
                    res = controller.read(table_chosen, data['cond'], data['limit'])
                    view.display_select_data(res, table_chosen)
                if operation_chosen == 'Add':
                    data_dict = view.launch_insert_prompt(table_chosen)
                    data = tuple_from_table_dictionary(table_chosen, data_dict)
                    controller.insert(table_chosen, data)
                    view.display_insert_data(data, table_chosen)
                if operation_chosen == 'Add Random':
                    data_dict = get_table_class(table_chosen).get_random()
                    data = tuple_from_table_dictionary(table_chosen, data_dict)
                    controller.insert(table_chosen, data)
                    view.display_insert_data(data, table_chosen)
                if operation_chosen == 'Delete':
                    data = view.launch_delete_prompt(table_chosen)
                    res = controller.delete(table_chosen, data)
                    view.display_delete_data(data, table_chosen)
                if operation_chosen == 'Update':
                    data = view.launch_update_prompt(table_chosen)
                    columns = key_value_string_from_dictionary(data['columns'])
                    controller.update(table_chosen, columns, data['condition'])
                    view.display_update_data(data['columns'], data['condition'], table_chosen)
                if operation_chosen == 'Text search':
                    data = view.launch_text_search_prompt(table_chosen)
                    if data['in'] == True:
                        res = controller.fulltext_search(table_chosen, data['col'], data['textp'])
                    else:
                        res = controller.no_fulltext_search(table_chosen, data['col'], data['textp'])

                    view.display_select_data(res, table_chosen)
                if operation_chosen == 'Joint search':
                    data = view.launch_joint_search_prompt()
                    res = controller.joint_search(data['player_is_active'], data['team_name'])
                    view.display_select_data(res, table_chosen)
        except Exception as error:
            print('Error in model: ' + error.message)
            controller.force_commit()
    controller.disconnect()
