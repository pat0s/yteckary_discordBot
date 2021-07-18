import discord
from dotenv import load_dotenv
from discord.ext import commands
import os

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Bot commands
bot = commands.Bot(
    command_prefix=["$", "?"],
    case_insensitive=True
)

# Extent bot functionality with cogs
extensions = ['greetings', 'jokes', 'counter']
for extension in extensions:
    bot.load_extension(f"cogs.{extension}")

bot.run(BOT_TOKEN)
