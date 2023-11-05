import json

with open('../json/infoDefault.json', 'r') as file:
    json_data = json.load(file)


#json_data['serverName']=input("Enter server name: ")
#json_data['botToken']=input("Enter Bot Token: ")
#json_data["steamAPIKey"]=input("Enter Steam Web API Key: ")
while True:
    restart_option = input("Enable restart function? (y/n): ")
    if restart_option=="y":
        json_data["restartFunc"] = "True"
        while True:
            restart_time=input("Enter restart time e.g '00:00', '07:00': ")
            if len(restart_time)==5 and restart_time[0].isnumeric() and restart_time[1].isnumeric() and restart_time[3].isnumeric() and restart_time[4].isnumeric() and restart_time[2]==":":
                json_data["restartTime"]==restart_time
                break
            else:
                print("Please enter a valid time E.G '00:00', '07:00', '06:09'")
        break
    elif restart_option=="n":
        json_data["restartFunc"] = "False"
        break
    else:
        print("Incorrect input, please input 'y' for yes or 'n' for no.")


with open('../json/info.json', 'w') as file:
    json.dump(json_data, file)