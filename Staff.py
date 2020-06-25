from math import *

import discord
from discord.ext import commands

import google_memer

client = commands.Bot(command_prefix="!")
Id = 720879927108567071
ADMIN_ROLES = ["Admin","NAME BENDER!","Master of channels"]

@client.event
async def on_ready():
    print("bot is up!")
    ID = client.get_guild(Id)
    print([i.name for i in ID.roles])
    print([i.name for i in client.get_all_members()])


@client.event
async def on_message(message):

    print(message.content, message.author, message.channel)

    await client.process_commands(message)


@client.command()
async def clear(ctx, lmt_arg:int):
    role = str(ctx.author.roles)

    h_count = 0
    for i in ADMIN_ROLES:
        if i in role:
            h_count+=1

    if h_count != 0:
        await ctx.channel.purge(limit=int(lmt_arg)+1)
    else:
        await ctx.send("You do not have permission to run this command")


@client.command()
async def google_meme(ctx):
    link = google_memer.fetcher()
    await ctx.send(link)


@client.command()
async def MATH(ctx, math_arg: str):
    eq = math_arg.replace("^", "**")
    await ctx.send(str(eval(eq)))


@clear.error
async def clear_err(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("ERROR: not enough arguments")
client.run("NzIxMTQ2NTcyNDU2MzI5MjQ2.XuyZsQ.yqNw-vOuo1rye_nwI1Qj9RWLc8U")
