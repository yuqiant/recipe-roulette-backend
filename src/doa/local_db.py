import json


class JSONDB:

    def __init__(self, local_filename):
        self.__filename = local_filename

    def create(self, key, value):
        self.update(key, value)

    def read(self, key):
        return self.__read_file()[key]

    def update(self, key, new_value):
        db = self.__read_file()
        db[key] = new_value
        self.__write_file(json.dumps(db))

    def destroy(self, key):
        db = self.__read_file()
        del db[key]
        self.__write_file(json.dumps(db))

    def __read_file(self, ):
        return json.loads(self.__filename)

    def __write_file(self, json_string):
        with open(self.__filename, 'w') as file:
            file.write(json_string)
