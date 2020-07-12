import random
from math import *

import discord
from discord.ext import commands

import google_memer

client = commands.Bot(command_prefix="!")
Id = 720879927108567071
MEMBERS = []
ADMIN_ROLES = ["Admin","NAME BENDER!","Master of channels"]
RANDOM_RESPONSE = ["i need to have a break 😴","WHEN's my shift over at 👿👿👿","🤦‍♂️","im retirering"]
ERROR_RESPONSE = ["What are you trying to doooo 🤯🤯🤯🤯","🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️","我嘞个毛","rhetorical : 👏👏👏👏"]
RANDOM_TALK = [
    "Great coffee ☕",
    "ah, awesome tea 🍵",
    "lunch time, 🥪🥪🥪🥪, oh wait !! 🤯",
    "🐟🎣",
    "I **HEAR** ***YOUR*** call **MY** PEOPLE",
    "ψ(｀∇´)ψψ(｀∇´)ψψ(｀∇´)ψψ(｀∇´)ψψ(｀∇´)ψψ(｀∇´)ψψ(｀∇´)ψ",
    "pls meme",
    "meow ( •̀ ω •́ )✧",
    "🌞",
    "🌚",
    "❄",
    "🔥\n☃",
    "Silently the aircar coasted through the darkness . . . -\npg 158, Chapter 24, Hitchhikers guide of the galaxy"
]

@client.event
async def on_ready():
    global MEMBERS
    global RANDOM_TALK
    print("bot is up!")
    ID = client.get_guild(Id)
    print([i.name for i in ID.roles])
    MEMBERS = [i.name for i in client.get_all_members()]
    RANDOM_TALK.append(f"@{random.choice(MEMBERS)} hello, would you like to enroll in a pyramid scheme?")


@client.event
async def on_message(message):

    print(message.content, message.author, message.channel)
    if str(message.channel) == "常规-general":
        if random.randrange(1,1001) >= 850 or "<@!721146572456329246>" in str(message.content):
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