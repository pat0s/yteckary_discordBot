import discord
from discord.ext import commands


class Jokes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def drga(self, ctx):
        await ctx.send(f'Áno, áno, áno, ... áno.')


def setup(bot):
    bot.add_cog(Jokes(bot))
