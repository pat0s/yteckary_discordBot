import discord
from discord.ext import commands
import os
from os.path import dirname, join
from dotenv import load_dotenv

# Load environment variables
load_dotenv('../')
IMG_PATH = os.getenv("IMG_PATH")


class Schedule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["schedule"])
    async def rozvrh(self, ctx, arg=None):
        if arg == "pato":
            path = join(IMG_PATH, 'pato.png')
            await ctx.send(file=discord.File(path))
        elif arg == "dalibor":
            path = join(IMG_PATH, 'dalibor.png')
            await ctx.send(file=discord.File(path))
        elif arg == "johny" or arg == "honza" or arg == "jan":
            path = join(IMG_PATH, 'johny.png')
            await ctx.send(file=discord.File(path))
        elif arg == "lukas":
            path = join(IMG_PATH, 'lukas.png')
            await ctx.send(file=discord.File(path))
        elif arg == "marcel":
            path = join(IMG_PATH, 'marcel.png')
            await ctx.send(file=discord.File(path))
        elif arg == "erika" or arg == "eri":
            path = join(IMG_PATH, 'erika.png')
            await ctx.send(file=discord.File(path))
        elif arg is None:
            path = join(IMG_PATH, f'{ctx.author.id}.png')
            await ctx.send(file=discord.File(path))


def setup(bot):
    bot.add_cog(Schedule(bot))
