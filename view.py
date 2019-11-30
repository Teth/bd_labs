class View(object):

    def __init__(self):
        pass

    def set_data(self, schema_data):
        pass

    def fill_table_prompt(self):
        pass

    def launch_joint_search_prompt(self):
        pass

    def launch_text_search_prompt(self, table_chosen):
        pass

    def launch_insert_prompt(self, table_chosen):
        pass

    def launch_update_prompt(self, table_chosen):
        pass

    def launch_delete_prompt(self, table_chosen):
        pass

    def launch_select_prompt(self, table_chosen):
        pass

    def launch_operation_prompt(self):
        pass

    def launch_table_prompt(self):
        pass

    def create_delete_prompt(self, table_name):
        pass

    def create_add_prompt(self, table_name):
        pass

    def create_columns_chk_prompt(self, table_name):
        pass

    def create_columns_prompt(self, table_name):
        pass

    def create_select_prompt(self, table_name):
        pass

    def display_select_data(self, data, table_name):
        pass

    def display_delete_data(self, data, table_name):
        pass

    def display_insert_data(self, data, table_name):
        pass

    def display_update_data(self, columns, condition, table_name):
        pass