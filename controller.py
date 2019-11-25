class Controller(object):
    concrete_model = 'none'

    def get_schemas(self):
        return self.concrete_model.get_schemas()

    def set_model(self, model):
        self.concrete_model = model

    def force_commit(self):
        self.concrete_model.force_commit()

    def insert(self, table, data):
        return self.concrete_model.insert(table, data)

    def fulltext_search(self,table, column, text_piece):
        return self.concrete_model.fulltext_search(table, column, text_piece)

    def read(self, table, conditions, limit):
        return self.concrete_model.read(table, conditions, limit)

    def update(self, table, columns, condition):
        return self.concrete_model.update(table, columns, condition)

    def delete(self, table, data):
        return self.concrete_model.delete(table, data)

    def disconnect(self):
        self.concrete_model.disconnect()
