import json

def get_info(key):
    with open('../json/info.json', 'r') as file:
        return json.load(file)[key]

def info_json_valid():
    with open('../json/info.json', 'r') as file:
        info = json.load(file)
        if info["serverName"]=="N/A" or info["botToken"]=="N/A" or info["steamAPIKey"]=="N/A":
            return False
        return True

def get_game_names():
    with open('../json/gameNames.json', 'r') as file:
        return json.load(file)