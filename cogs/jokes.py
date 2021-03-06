import discord
from discord.ext import commands
import random
import os
from os.path import join
from dotenv import load_dotenv

# Load environment variables
load_dotenv('../')
CHOSEN = os.getenv('CHOSEN')
IMG_PATH = os.getenv('IMG_PATH')


class Jokes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def drga(self, ctx):
        one_liners = ['Áno, áno, áno, ... áno.',
                      'Nie, nie, nie, ... nie.',
                      'Dobre, dobre, dobre...',
                      'Sorry, sorry, sorry, sorry',
                      'Čaute chalani...a dievčence, ak tu máme nejaké',
                      'Astronóm drga',
                      'Hviezdny prostitút.'
                      ]
        one_liner = random.choice(one_liners)
        await ctx.send(f'{one_liner}')

    @commands.command()
    async def meduna(self, ctx):
        await ctx.send("To je BOREC!")

    @commands.command(aliases=['honza'])
    async def cernocky(self, ctx):
        one_liners = ['Drbu na to',
                      'Vojel sem to padesát krát.'
                      ]
        one_liner = random.choice(one_liners)
        await ctx.send(f'{one_liner}')

    @commands.command()
    async def little(self, ctx):
        await ctx.send(":pinching_hand:")

    @commands.Cog.listener()
    async def on_message(self, message):
        mentioned = message.mentions

        for user in mentioned:
            if user.id == int(CHOSEN):
                await message.channel.send(f'**{user.name}** má rád **VEĽKÉ kravy**.')
                path = join(IMG_PATH, 'krava.gif')
                await message.channel.send(file=discord.File(path))

    @commands.command()
    async def noice(self, ctx):
        path = join(IMG_PATH, 'noice.gif')
        await ctx.send(file=discord.File(path))

    @commands.command()
    async def play(self, ctx):
        path = join(IMG_PATH, 'zvucka.wav')
        await ctx.send(file=discord.File(path))

    @commands.command(aliases=['vítomer'])
    async def vitomer(self, ctx):
        one_liners = ['Máš deň pod Víta.',
                      'Na tvoju mentálnu úroveň sa len tak niekto nedostane.',
                      'Máš IQ húpacieho koníka.',
                      'Basic.',
                      'Nemachruj aj ja som prešiel IQ testom.',
                      'Za tvoju genialitu môže jedine výberová škola, na ktorú si chodil.'

                      ]

        iq = random.randrange(-100, 200, 1)
        if iq < 0:
            pos = 0
        elif iq < 50:
            pos = 1
        elif iq < 100:
            pos = 2
        elif iq < 130:
            pos = 3
        elif iq < 150:
            pos = 4
        else:
            pos = 5

        await ctx.send(f'Tvoje IQ je {iq}. {one_liners[pos]}')

    @commands.command(aliases=['prestíž'])
    async def prestiz(self, ctx):
        path = join(IMG_PATH, 'prestiz.gif')
        await ctx.send(file=discord.File(path))

    @commands.command(aliases=['zivot', 'vut', 'vutfit'])
    async def fit(self, ctx):
        path = join(IMG_PATH, 'fit.gif')
        await ctx.send(file=discord.File(path))


def setup(bot):
    bot.add_cog(Jokes(bot))
