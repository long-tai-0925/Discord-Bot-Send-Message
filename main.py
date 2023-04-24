#import something
import discord
from discord.ext import commands

# set variable
client = discord.Client()
number = 0

# Print bot name when link to DisocrdAPI
@client.event
async def on_ready():
    print(f'---------------------------------------------------\nBot Name：{client.user}')

# Main Code
@client.event
async def on_ready():
    number = 0
    guild_names = []
    guild_ids = []
    for guild in client.guilds:
        guild_names.append(guild.name)
        guild_ids.append(guild.id)
        number += 1
        print(f'{number}.Server Name: {guild.name}, ID: {guild.id}')
    guild_list = int(input("---------------------------------------------------\nSelect the first few Servers：\n-----------------------------------\n"))-1
    print(f"Server Name：{guild_names[guild_list]}\n")
    print(f"Server ID：{guild_ids[guild_list]}")
    number = 0
    guild = client.get_guild(guild_ids[guild_list])
    channel_names = []
    channel_ids = []
    for channel in guild.channels:
        channel_names.append(channel.name)
        channel_ids.append(channel.id)
        number += 1
        print(f'{number}.Server Name: {channel.name}, ID: {channel.id}')
    channel_list = int(input("---------------------------------------------------\n Select the first few channel：\n"))-1
    print(f"---------------------------------------------------\nchannel Name：{channel_names[channel_list]}")
    print(f"---------------------------------------------------\nchannel ID：{channel_ids[channel_list]}")
    while True:
        guild_send = client.get_guild(guild_ids[guild_list])
        channel = guild_send.get_channel(channel_ids[channel_list])
        await channel.send(input("---------------------------------------------------\nEnter a message to send：\n"))

# Replace "Your_Token" with your Token
client.run("UE_TOKEN")
