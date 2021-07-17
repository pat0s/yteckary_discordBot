import discord
from dotenv import load_dotenv
from discord.ext import commands
import os


# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Bot commands
bot = commands.Bot(command_prefix="$")


@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")


@bot.command()
async def pomoc(ctx):
    await ctx.send("Help yourself. Irony :pinching_hand:")


@bot.command()
async def drga(ctx):
    await ctx.send("Áno, áno, áno, ..., áno")

bot.run(BOT_TOKEN)
