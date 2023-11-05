import json

with open('../json/infoDefault.json', 'r') as file:
    json_data = json.load(file)


json_data['serverName']=input("Enter server name: ")
json_data['botToken']=input("Enter Bot Token: ")
json_data["SteamAPIKey"]=input("Enter Steam Web API Key: ")

with open('../json/info.json', 'w') as file:
    json.dump(json_data, file)