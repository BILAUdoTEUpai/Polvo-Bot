import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'🤖 Polvo-Bot conectado como {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

import os
bot.run(os.environ['DISCORD_TOKEN'])
