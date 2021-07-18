import discord
from discord.ext import commands


class Counter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def counter(self, ctx, channel: discord.TextChannel=None):
        channel = channel or ctx.channel

        count = 0
        async for _ in channel.history(limit=None):
            count += 1

        await ctx.send(f'Number of messages: **{count}** in **{channel.name}** channel')


def setup(bot):
    bot.add_cog(Counter(bot))
