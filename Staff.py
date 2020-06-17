import discord
from discord.ext import commands
import json
import timer
import google_memer
from math import *

client = commands.Bot(command_prefix="!")
Id = "SERVER ID"
SPAM_COUNT = 0
text_stream_buffer = {}


@client.event
async def on_ready():
    print("bot is up!")
    ID = client.get_guild(Id)
    print([i.name for i in ID.roles])
    print([i.name for i in client.get_all_members()])
    for i in [str(i.name) for i in client.get_all_members()]:
        print(i)
        text_stream_buffer[i] = 0


def spam_tracker(author):
    text_stream_buffer[author] += 1


def spam():
    global SPAM_COUNT
    SPAM_COUNT += 1


timer.start()
tstamp_log = [0, 0]


@client.event
async def on_message(message):
    global tstamp_log
    global SPAM_COUNT

    tstamp_log[0] = tstamp_log[1]
    tstamp_log[1] = 0

    ope = list(str(message.author))
    ap_r = []
    for i in ope:
        if i == "#":
            break
        ap_r.extend(i)

    ap_r = "".join(ap_r)
    spam_tracker(ap_r)
    await client.process_commands(message)

    tstamp_log[1] = timer.end(display=False)
    tp = tstamp_log[1]-tstamp_log[0]
    if tp <= 0.566:
        spam()

    if SPAM_COUNT == 6:
        await message.channel.purge(limit=2*SPAM_COUNT)
        await message.channel.send("BOI U STOP SPAMMING")
        SPAM_COUNT = 0

    elif len(str(message.content)) >= 1010:
        await message.channel.purge(limit=1)
        await message.channel.send("BOI U STOP SPAMMING")
    #print(message.content, message.author, message.channel, SPAM_COUNT)


@client.command()
async def show_text_stream_buffer(ctx):
    buffer_as = str(text_stream_buffer).replace(
        ",", ",\n").replace("{", "{\n").replace("}", "\n}")
    await ctx.send(buffer_as)


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
client.run("TOKEN <enter your own>")
