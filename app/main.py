import discord
from discord.ext import commands # imports commands from Discord module

import jsonInterface as JI
import ipInfo as II
import valveAPI as VAPI


intents = discord.Intents().all()
client = commands.Bot(command_prefix=',', intents=intents)

botToken = JI.get_info("botToken")

if not JI.info_json_valid():
    print("Please run setup/setup.py before running this file.")
    exit(1)
else:
    print("-info.json file is Complete-")

@client.event
async def on_ready(): # code that runs once connected to Discord
    channel = discord.utils.get(client.get_all_channels(), name='asc-status')
    print('-Logged in as {0.user}-'.format(client)) # message to print once a connection has been made

@client.event
async def on_message(message):# code that runs once a message is received
    message.content=message.content.lower()
    if message.author == client.user:# makes sure that the bot ignores it's own messages
        return

    if message.content.startswith('/asc'):

        print(f"{message.author} ({message.author.id}) says \"{message.content}\" in \"{message.channel}\"") # prints the message content and the user who posted it, aswell as their Discord ID

        if message.content==("/asc"): # identifies if they used the '/SG' command
            await message.channel.send(f'Hello! <@{message.author.id}>\nMy Name is Ark Server Companion!\nI am a Discord bot that can get you Ark Server Information.\ntry \"/asc help\" for available commands.')

        elif message.content=="/asc help":
            await message.channel.send(f"IP: {II.get_public_ipv4()}")

        elif message.content=="/asc ip":
            await message.channel.send(f"IP: {II.get_public_ipv4()}")

        elif message.content=="/asc info":
            ip = II.get_public_ipv4()
            server_info_text=VAPI.get_server_info(JI.get_info("steamAPIKey"), ip, JI.get_game_names())
            await message.channel.send(f"Servers @ {ip}:\n{server_info_text[0]}")
            for x in range(len(server_info_text) - 1):
                x += 1
                await message.channel.send(f"{server_info_text[x]}")

        elif message.content[0:10] == "/asc info ":
            if message.content[-1].isnumeric():
                ip = message.content.replace("/asc info ","")
            else:
                ip = II.get_ip_from_domain(message.content.replace("/asc info ", ""))

            print(f"Using IP: {ip}")
            server_info_text = VAPI.get_server_info(JI.get_info("steamAPIKey"), ip, JI.get_game_names())
            if ip=="Incorrect Domain":
                await message.channel.send(f"Servers @ {ip}:\n{server_info_text[0]}\n\nCorrect usage:\n/asc info google.com\n/asc info 69.69.69.69")
            else:
                await message.channel.send(f"Servers @ {ip}:\n{server_info_text[0]}")
                for x in range(len(server_info_text)-1):
                    x+=1
                    await message.channel.send(f"{server_info_text[x]}")

        else:
            print(message.content[0:12])
            await message.channel.send(f"Sorry I don't recognise that command <@{message.author.id}> :(")

client.run(botToken)