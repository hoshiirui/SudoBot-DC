import discord
import os
import random
import asyncio
from discord.ext import commands, tasks
import sudokutools as sdk
import datetime

description = '''An example bot to showcase the discord.ext.commands extension
module.'''

#setup
activity = discord.Game(name="Generate Random Sudoku and Solve It!")
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?',
                   description=description,
                   intents=intents,
                   activity=activity,
                   status=discord.Status.idle)
client = discord.Client(intents=intents)
#normalmsg = commands.Bot(command_prefix='!',intents=discord.Intents.all())

# ------------------------------ Mulai Command Bot ------------------------------


#pas diidupin
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


#tambah 2 angka
@bot.command()
async def add(ctx, *num):
    x = 0
    for i in num:
        x = x + int(i)
    """Adds two numbers together."""
    await ctx.send("Your result: " + str(x))


#kapan sebuah member join
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined in {member.joined_at}')


@bot.command()
async def tes(ctx):
    """Testing for embed commands"""
    embed = discord.Embed(title="hai",
                          description="inia ku ini ak ainsidfsj",
                          color=0xff0ff)
    await ctx.send(embed=embed)


# @bot.command()
# async def sudoku(ctx):
#   sdk.solve()
#   await ctx.send(sdk.cetak(sudogrid))


@bot.command()
async def generate(ctx, difficulty: str):
    """Generate a random sudoku based on inputted difficulty."""
    if (difficulty == "Random") or (difficulty == "random") or (difficulty
                                                                == "r"):
        sudogrid = sdk.buat()
        sudocomp = sdk.deepcopy(sudogrid)
        sdk.solve(sudogrid)
        while (sudogrid == sudocomp):
            sudogrid = sdk.buat()
            sudocomp = sdk.deepcopy(sudogrid)
            sdk.solve(sudogrid)
    elif(difficulty == "Easy") or (difficulty == "e") or (difficulty
                                                           == "easy"):
        sudocomp = [[0, 0, 0, 2, 6, 0, 7, 0, 1], 
                    [6, 8, 0, 0, 7, 0, 0, 9, 0],
                    [1, 9, 0, 0, 0, 4, 5, 0, 0], 
                    [8, 2, 0, 1, 0, 0, 0, 4, 0],
                    [0, 0, 4, 6, 0, 2, 9, 0, 0], 
                    [0, 5, 0, 0, 0, 3, 0, 2, 8],
                    [0, 0, 9, 3, 0, 0, 0, 7, 4], 
                    [0, 4, 0, 0, 5, 0, 0, 3, 6],
                    [7, 0, 3, 0, 1, 8, 0, 0, 0]]
        sudogrid = sdk.deepcopy(sudocomp)
        sdk.solve(sudogrid)
    elif(difficulty == "Normal") or (difficulty == "n") or (difficulty == "normal"):
        sudocomp = [[0, 2, 0, 6, 0, 8, 0, 0, 0], 
                    [5, 8, 0, 0, 0, 9, 7, 0, 0],
                    [0, 0, 0, 0, 4, 0, 0, 0, 0], 
                    [3, 7, 0, 0, 0, 0, 5, 0, 0],
                    [6, 0, 0, 0, 0, 0, 0, 0, 4], 
                    [0, 0, 8, 0, 0, 0, 0, 1, 3],
                    [0, 0, 0, 0, 2, 0, 0, 0, 0], 
                    [0, 0, 9, 8, 0, 0, 0, 3, 6],
                    [0, 0, 0, 3, 0, 6, 0, 9, 0]]
        sudogrid = sdk.deepcopy(sudocomp)
        sdk.solve(sudogrid)
    elif(difficulty == "Hard") or (difficulty == "h") or (difficulty == "hard"):
        sudocomp = [[0, 0, 0, 6, 0, 0, 4, 0, 0], 
                    [7, 0, 0, 0, 0, 3, 6, 0, 0],
                    [0, 0, 0, 0, 9, 1, 0, 8, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 5, 0, 1, 8, 0, 0, 0, 3], 
                    [0, 0, 0, 3, 0, 6, 0, 4, 5],
                    [0, 4, 0, 2, 0, 0, 0, 6, 0], 
                    [9, 0, 3, 0, 0, 0, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0, 1, 0, 0]]
        sudogrid = sdk.deepcopy(sudocomp)
        sdk.solve(sudogrid)
    hasil = discord.Embed(title="Sudoku Generated!",
                          description=sdk.cetak(sudocomp),
                          color=0xff0ff,
                          timestamp=datetime.datetime.utcnow())
    hasil.set_footer(text="Sudobot", icon_url="https://drive.google.com/file/d/1nBG8pTLfVvCatNBUS_rsvcy1RMfiV_U6/view?usp=share_link")
    await ctx.send(embed=hasil)
    await ctx.send("Solve it magically? (y/n)")
    try:
        msg = await bot.wait_for(
            "message",
            timeout=60,
            check=lambda message: message.author == ctx.author)
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond")
        return
    if msg.content == "y":
        hasil = discord.Embed(title="Solution",
                              description=sdk.cetak(sudogrid),
                              color=0xff0ff,
                              timestamp=datetime.datetime.utcnow())
        hasil.set_footer(text="Sudobot", icon_url="https://drive.google.com/file/d/1nBG8pTLfVvCatNBUS_rsvcy1RMfiV_U6/view?usp=share_link")
        await ctx.send(embed=hasil)


bot.run(os.environ['bot-token'])
