import discord
from discord.ext import commands
import os
from os.path import dirname, join
from dotenv import load_dotenv

# Load environment variables
load_dotenv('../')
CHOSEN = os.getenv('CHOSEN')
CHOSEN2 = os.getenv('CHOSEN2')
CHOSEN3 = os.getenv('CHOSEN3')
CHOSEN4 = os.getenv('CHOSEN4')
CHOSEN5 = os.getenv('CHOSEN5')


class Schedule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["schedule"])
    async def rozvrh(self, ctx):
        if ctx.author.id == int(CHOSEN):
            path = join(dirname(__file__), 'pato.png')
            await ctx.send(file=discord.File(path))
        elif ctx.author.id == int(CHOSEN2):
            path = join(dirname(__file__), 'dalibor.png')
            await ctx.send(file=discord.File(path))
        elif ctx.author.id == int(CHOSEN3):
            path = join(dirname(__file__), 'pato.png')
            await ctx.send(file=discord.File(path))
        elif ctx.author.id == int(CHOSEN4):
            path = join(dirname(__file__), 'marcel.png')
            await ctx.send(file=discord.File(path))
        elif ctx.author.id == int(CHOSEN5):
            path = join(dirname(__file__), 'johny.png')
            await ctx.send(file=discord.File(path))


def setup(bot):
    bot.add_cog(Schedule(bot))
