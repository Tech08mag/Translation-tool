import json


def read_json(file: str, key: str):
    with open(file, mode="r", encoding="utf-8") as read_file:
        settings_data = json.load(read_file)
        return settings_data[key]


def write_json(file: str, key: str, value: any):
    with open(file, mode="r", encoding="utf-8") as read_file:
        settings_data = json.load(read_file)
        if key in settings_data:
            settings_data[key] = value
        else:
            print(f"{key} does not exists")