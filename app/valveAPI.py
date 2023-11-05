import requests

def get_server_info(steamApiKey,ip,gameNames):


    response = requests.get(f'https://api.steampowered.com/IGameServersService/GetServerList/v1/?key={steamApiKey}&filter=addr\\{ip}')
    server_info = response.json()
    server_info_text = [""]
    try:

        for x in server_info["response"]["servers"]:
            if x['product'] in gameNames:
                gameName = gameNames[x["product"]]
            else:
                gameName=x["product"]


            server_string=f'Game name: {gameName}\nServer name: {x["name"]}\nMap: {x["map"]}\nPlayers: {x["players"]}/{x["max_players"]}\nAddress: {x["addr"]}\nJoin: steam://connect/{x["addr"]}\n------------------------\n'
            if len(server_info_text[-1])+len(server_string)>1900:
                server_info_text.append(server_string)
            else:
                server_info_text[-1]+=server_string

    except Exception as e:
        print(e)
        server_info_text = ["Sorry I can't find any servers at this address."]
    return server_info_text