import discord

client = discord.Client()

@client.event
async def on_ready():
    print("봇 로그인")

client.run("ODU3MzQ0OTY5Mjk5NzIyMjQw.YNOOuQ.x1wC8vuR5D3TP14bGtVah0yzGJQ")