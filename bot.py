import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=";")

@bot.event

async def on_ready():
    print(">> bot is online << ")

bot.run('ODA2Mzg1NzAyOTM3OTUyMjU3.YBorNQ.QtgkXugCMLGx1Ix3BGIUjtCP-qM')