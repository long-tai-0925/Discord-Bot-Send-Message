if input("輸入要選擇哪個Bot\n1.NK4 NK4#0753\n2.Next#7616\n") == "1":
    Token = "OTc2ODQ2MTc5MjU2MTIzMzky.Gg1tyt.aQ8K-aNJer8QXBt0GjPpwAZODtTpnxbtDsmMG8"
else:
    Token = "ODQ0OTU0ODg5OTIyNjc0NzM4.Gzc5DJ.U06ToI4OMYni2e_9jK2vafEgoOm1ZhTGmzQwDU"
    
import discord
from discord.ext import commands

client = discord.Client()
number = 0

@client.event
async def on_ready():
    number = 0
    print(f'---------------------------------------------------\n機器人名稱：{client.user}')
    guild_names = []
    guild_ids = []
    for guild in client.guilds:
        guild_names.append(guild.name)
        guild_ids.append(guild.id)
        number += 1
        print(f'{number}.Server Name: {guild.name}, ID: {guild.id}')
    guild_list = int(input("---------------------------------------------------\n輸入第幾個Server：\n-----------------------------------\n"))-1
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
    channel_list = int(input("---------------------------------------------------\n 輸入第幾個channel：\n"))-1
    print(f"---------------------------------------------------\nchannel Name：{channel_names[channel_list]}")
    print(f"---------------------------------------------------\nchannel ID：{channel_ids[channel_list]}")
    while True:
        guild_send = client.get_guild(guild_ids[guild_list])
        channel = guild_send.get_channel(channel_ids[channel_list])
        await channel.send(input("---------------------------------------------------\n輸入要發送的訊息：\n"))


client.run(Token)