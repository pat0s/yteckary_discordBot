import discord
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        name = ctx.author.name
        await ctx.send(f'Hi {name}!')

    # TODO: say hello to new member
    #       just in the concrete room

    # from https://discordpy.readthedocs.io/en/master/ext/commands/cogs.html
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Welcome {member.mention}.')


def setup(bot):
    bot.add_cog(Greetings(bot))
