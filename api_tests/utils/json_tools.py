import json
import os

from config import get_project_root


class JSONFileHandler:
    """
    A class for handling operations on JSON files.
    """

    def __init__(self, file_path):
        """
        Initialize the JSONFileHandler with a file path.
        :param file_path: Path to the JSON file.
        """
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            self._write_to_file({})  # Create an empty JSON file if it doesn't exist

    def _read_from_file(self):
        """Read data from the JSON file."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}

    def _write_to_file(self, data):
        """Write data to the JSON file."""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def read(self, key=None):
        """
        Read the value associated with a key or return the entire content.
        :param key: Key to look up in the JSON data.
        :return: Value of the key or entire JSON data.
        """
        data = self._read_from_file()
        if key:
            return data.get(key)
        return data

    def write(self, key, value):
        """
        Write a key-value pair to the JSON file.
        :param key: Key to write.
        :param value: Value to associate with the key.
        """
        data = self._read_from_file()
        data[key] = value
        self._write_to_file(data)

    def delete(self, key):
        """
        Delete a key-value pair from the JSON file.
        :param key: Key to delete.
        """
        data = self._read_from_file()
        if key in data:
            del data[key]
            self._write_to_file(data)

    def clear(self):
        """Clear all data in the JSON file."""
        self._write_to_file({})


if __name__ == '__main__':
    json_handler = JSONFileHandler(os.path.join(get_project_root(), "api_tests", "data", "data.json"))
    print(json_handler.read('cases'))
