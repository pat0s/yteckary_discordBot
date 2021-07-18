import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import cogs.greetings as cg
import cogs.jokes as jk


# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Bot commands
bot = commands.Bot(
    command_prefix="$",
    case_insensitive=True
)

cg.setup(bot)
jk.setup(bot)


"""
cog = bot.get_cog('Greetings')
commands = cog.get_commands()
print([c.name for c in commands])
"""


@bot.command()
async def pomoc(ctx):
    await ctx.send("Help yourself. Irony :pinching_hand:")


bot.run(BOT_TOKEN)
