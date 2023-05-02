import json
import os


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
        if not os.path.exists(self.__filename):
            raise FileNotFoundError(f"File '{self.__filename}' not found.")
        with open(self.__filename, 'r') as f:
            return json.load(f)

    def __write_file(self, json_string):
        with open(self.__filename, 'w') as f:
            f.write(json_string)


if __name__ == '__main__':
    # Test block written by chatGPT
    # Create test JSON file
    with open('test_db.json', 'w') as file:
        file.write('{}')

    # Test cases
    test_db = JSONDB('test_db.json')

    # Create
    test_db.create('key1', {'nested_key1': 'value1'})
    test_db.create('key2', {'nested_key2': 'value2'})
    test_db.create('key3', {'nested_key3': 'value3'})

    # Read
    assert test_db.read('key1') == {'nested_key1': 'value1'}
    assert test_db.read('key2') == {'nested_key2': 'value2'}
    assert test_db.read('key3') == {'nested_key3': 'value3'}

    # Update
    test_db.update('key1', {'nested_key1': 'new_value1'})
    test_db.update('key2', {'nested_key2': 'new_value2'})
    test_db.update('key3', {'nested_key3': 'new_value3'})

    assert test_db.read('key1') == {'nested_key1': 'new_value1'}
    assert test_db.read('key2') == {'nested_key2': 'new_value2'}
    assert test_db.read('key3') == {'nested_key3': 'new_value3'}

    # Destroy
    test_db.destroy('key1')
    test_db.destroy('key2')
    test_db.destroy('key3')

    # Clean up
    os.remove('test_db.json')
