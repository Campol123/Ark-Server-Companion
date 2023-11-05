import requests

def get_server_info(steamApiKey,ip):
    response = requests.get(f'https://api.steampowered.com/IGameServersService/GetServerList/v1/?key={steamApiKey}&filter=addr\\{ip}')
    server_info = response.json()
    server_info_text = ""
    try:
        for x in server_info["response"]["servers"]:
            server_info_text += f'Server name: {x["name"]}\nMap: {x["map"]}\nPlayers: {x["players"]}/{x["max_players"]}\nAddress: {x["addr"]}\nJoin: steam://connect/{x["addr"]}\n------------------------\n'
    except:
        server_info_text = "Sorry I can't find any servers at this address."
    return server_info_text