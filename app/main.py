import discord
from discord.ext import commands # imports commands from Discord module

import jsonInterface as JI
import ipInfo as II
import valveAPI as VAPI


intents = discord.Intents().all()
client = commands.Bot(command_prefix=',', intents=intents)

botToken = JI.get_info("botToken")

commands = ["/SG - brings up welcome text."]
@client.event
async def on_ready(): # code that runs once connected to Discord
    channel = discord.utils.get(client.get_all_channels(), name='asc-status')
    #await channel.send("Ark Server Companion started")
    print('We have logged in as {0.user}'.format(client)) # message to print once a connection has been made

@client.event
async def on_message(message):# code that runs once a message is received

    if message.author == client.user:# makes sure that the bot ignores it's own messages
        return

    if message.content.startswith('/ASC'): #identifies the messages that start with '/SG' (Stock Genie)

        print(f"{message.author} ({message.author.id}) says \"{message.content}\" in \"{message.channel}\"") # prints the message content and the user who posted it, aswell as their Discord ID

        if message.content==("/ASC"): # identifies if they used the '/SG' command
            await message.channel.send(f'Hello! <@{message.author.id}>\nMy Name is Ark Server Companion!\nI am a Discord bot that can get you Ark Server Information.\ntry \"/ASC help\" for available commands.')

        elif message.content=="/ASC ip":
            await message.channel.send(f"IP: {II.get_public_ipv4()}")

        elif message.content=="/ASC info":
            ip = II.get_public_ipv4()
            server_info_text=VAPI.get_server_info(JI.get_info("steamAPIKey"), ip)
            await message.channel.send(f"Servers @ {ip}:\n{server_info_text}")

        elif message.content[0:14] == "/ASC info -ip ":
            ip = message.content.replace("/ASC info -ip ","")
            print(ip)
            server_info_text = VAPI.get_server_info(JI.get_info("steamAPIKey"), ip)
            await message.channel.send(f"Servers @ {ip}:\n{server_info_text}")

        elif message.content[0:15] == "/ASC info -dom ":
            ip = II.get_ip_from_domain(message.content.replace("/ASC info -dom ",""))
            print(ip)
            server_info_text = VAPI.get_server_info(JI.get_info("steamAPIKey"), ip)
            await message.channel.send(f"Servers @ {ip}:\n{server_info_text}")

        else:
            print(message.content[0:12])
            await message.channel.send(f"Sorry I don't recognise that command <@{message.author.id}> :(")

client.run(botToken)