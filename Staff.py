import random
from math import *

import discord
from discord.ext import commands

import google_memer

client = commands.Bot(command_prefix="!")
Id = 720879927108567071
ADMIN_ROLES = ["Admin","NAME BENDER!","Master of channels"]
RANDOM_RESPONSE = ["i need to have a break 😴","WHEN's my shift over at 👿👿👿","🤦‍♂️"]
ERROR_RESPONSE = ["What are you trying to doooo 🤯🤯🤯🤯","🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️","rhetorical : 👏👏👏👏"]
RANDOM_TALK = [
    "Great coffee ☕",
    "ah, awesome tea 🍵",
    "lunch time, 🥪🥪🥪🥪, oh wait !! 🤯",
    "🐟🎣",
    "ψ(｀∇´)ψψ(｀∇´)ψψ(｀∇´)ψψ(｀∇´)ψψ(｀∇´)ψψ(｀∇´)ψψ(｀∇´)ψ"
]

@client.event
async def on_ready():
    print("bot is up!")
    ID = client.get_guild(Id)
    print([i.name for i in ID.roles])
    print([i.name for i in client.get_all_members()])


@client.event
async def on_message(message):

    print(message.content, message.author, message.channel)
    if str(message.channel) == "常规-general":
        if random.randrange(1,101) >= 50:
            await message.channel.send(random.choice(RANDOM_TALK))
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
        await ctx.send(random.choice(ERROR_RESPONSE))


@client.command()
async def google_meme(ctx):
    link = google_memer.fetcher()
    await ctx.send(link)


@client.command()
async def MATH(ctx, math_arg: str):
    try:
        eq = math_arg.replace("^", "**")
        await ctx.send(str(eval(eq)))
    except:
        await ctx.send(random.choice(RANDOM_RESPONSE))


@clear.error
async def clear_err(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(random.choice(ERROR_RESPONSE))

with open("TOKEN.txt","r")as fio:
    TOKEN = fio.read()
client.run(TOKEN)
