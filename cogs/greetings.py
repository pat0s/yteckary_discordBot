import discord
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['hi'])
    async def hello(self, ctx):
        name = ctx.author.name
        await ctx.send(f'Hi {name}!')

    @commands.command()
    async def goodmorning(self, ctx):
        name = ctx.author.name
        await ctx.send(f'Good morning **{name}** :)')


def setup(bot):
    bot.add_cog(Greetings(bot))
