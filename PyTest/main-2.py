import time
import discord
from discord.ext import commands

Client = commands.Bot(command_prefix = 'l', self_bot =True)

@Client.event
async def on_ready():
    print('loading...░░░░░░░░░░░░░░░░')
    print(' ')
    time.sleep(0.6)
    print('loading...▓░░░░░░░░░░░░░░░')
    print(' ')
    time.sleep(0.3)
    print('loading...▓▓░░░░░░░░░░░░░░')
    print(' ')
    time.sleep(1)
    print('loading...▓▓▓░░░░░░░░░░░░░')
    print(' ')
    time.sleep(0.3)
    print('loading...▓▓▓▓▓░░░░░░░░░░░')
    print(' ')
    time.sleep(0.1)
    print('loading...▓▓▓▓▓▓▓░░░░░░░░░')
    print(' ')
    time.sleep(0.1)
    print('loading...▓▓▓▓▓▓▓▓░░░░░░░░')
    print(' ')
    time.sleep(0.4)
    print('loading...▓▓▓▓▓▓▓▓▓▓░░░░░░')
    print(' ')
    time.sleep(0.5)
    print('loading...▓▓▓▓▓▓▓▓▓▓▓░░░░░')
    print(' ')
    time.sleep(0.8)
    print('loading...▓▓▓▓▓▓▓▓▓▓▓▓▓░░░')
    print(' ')
    time.sleep(0.3)
    print('loading...▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
    print(' ')
    time.sleep(0.1)
    print('---------loaded-----------')


@Client.command()
async def l(ctx, *, text):
    await ctx.send((text)+" | by ๖ۜkOFFe")
    time.sleep(0.2)
    await ctx.message.delete()
    # await me.edit_message(message, '  ', embed=actualObj)


Client.run("NzIyNDM0MzkyMTI3MTc2NzE0.X330Fg.pYMxuPmZ-srZ6s0wCS8V5pDMzpI", bot = False)