import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("봇 로그인")

access_token = os.environ["BOT TOKEN"]    
    
client.run(access_token)
