import json

def get_info(key):
    with open('../json/info.json', 'r') as file:
        return json.load(file)[key]