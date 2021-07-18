import discord
from discord.ext import commands
import random


class Jokes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def drga(self, ctx):
        one_liners = ['Áno, áno, áno, ... áno.',
                      'Nie, nie, nie, ... nie.',
                      'Dobre, dobre, dobre...'
                      ]
        one_liner = random.choice(one_liners)
        await ctx.send(f'{one_liner}')

    @commands.command()
    async def little(self, ctx):
        await ctx.send(":pinching_hand:")


def setup(bot):
    bot.add_cog(Jokes(bot))
