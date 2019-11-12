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

    def read(self, table, data):
        return self.concrete_model.read(table, data)

    def update(self, table, columns, condition):
        return self.concrete_model.update(table, columns, condition)

    def delete(self, table, data):
        return self.concrete_model.delete(table, data)

    def disconnect(self):
        self.concrete_model.disconnect()
