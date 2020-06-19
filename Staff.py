import discord
from discord.ext import commands
import json
import timer
import google_memer
from math import *

client = commands.Bot(command_prefix="!")
Id = 720879927108567071


@client.event
async def on_ready():
    print("bot is up!")
    ID = client.get_guild(Id)
    print([i.name for i in ID.roles])
    print([i.name for i in client.get_all_members()])


@client.event
async def on_message(message):
    print(message.content, message.author, message.channel)

@client.command()
async def clear(ctx, lmt_arg):
    await ctx.channel.purge(limit=int(lmt_arg)+1)


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
