import json

with open('../json/infoDefault.json', 'r') as file:
    json_data = json.load(file)

print(json_data)
json_data['serverName']=input("Enter server name: ")
json_data['botToken']=input("Enter Bot Token: ")

with open('../json/info.json', 'w') as file:
    json.dump(json_data, file)