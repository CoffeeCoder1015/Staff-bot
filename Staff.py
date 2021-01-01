import io
import random
import time
from math import *

import aiohttp
import discord
import requests
from discord.ext import commands
from termcolor import colored

import f_opt
import google_memer
from TextResponse import *

client = commands.Bot(command_prefix="!")
MEMBERS = []
ADMIN_ROLES = ["admin"]
dcmd = ["power", "myside", "noschool",
        "oof", "breaksnowbot", "boom", "arson", "slap", "reverse"]


@client.event
async def on_ready():
    global MEMBERS
    global RANDOM_TALK
    print("bot is up!")
    print([i.name for i in client.get_all_members()])


@client.event
async def on_message_edit(before, after):
    if before.content != after.content:
        att = []
        for obj in [before, after]:
            if len(obj.attachments) != 0:
                attach = obj.attachments[0].url
                att.append(attach)
            else:
                att.append(None)
        printstr = f"{before.content}  |  {att[0]}\n{after.content}  |  {att[1]}\n{before.author}  |  {before.channel} | {before.guild}"
        print(colored(f"EDIT:\n{printstr}", "green"))


@client.event
async def on_message_delete(msg):
    attach = None
    if len(msg.attachments) != 0:
        attach = msg.attachments[0].url
    printstr = f"{msg.content}  |  {attach}  |  {msg.author}  |  {msg.channel} | {msg.guild}"
    print(colored(f"DELETE: {printstr}", "red"))


@client.event
async def on_message(message):
    global Norm_txt_Log
    dcs = False
    cc = False
    attach = None

    if Norm_txt_Log == True:
        if len(message.attachments) != 0:
            attach = message.attachments[0].url
        printstr = f"{message.content}  |  {attach}  |  {message.author}  |  {message.channel} | {message.guild}"
        print(printstr)

    # -------------check establishing if statement-----------------------
    if "staffbot" in str(message.content).lower() or "<@!721146572456329246>" in str(message.content):
        dcs = True
        for i in str(message.content).split(" "):
            if i in dcmd:
                cc = i
    # --------------------- END of C.E.I.S ---------------------------------

    # random responce controller
    if str(message.channel) == "常规-general" and dcs == False:
        if random.randrange(1, 1001) >= 955:
            await message.channel.send(random.choice(RANDOM_TALK))

    # direct command controller
    if dcs == True:
        # ------ if no D.C is selected -------
        if cc == False:
            if random.randrange(0, 2) == 1:
                await message.channel.send(random.choice(RANDOM_TALK))
            else:
                m = random.choice(DIRECT_RESPONSE)
                if m[0] == "img":
                    async with aiohttp.ClientSession() as session:
                        async with session.get(m[1]) as resp:
                            data = io.BytesIO(await resp.read())
                            await message.channel.send(file=discord.File(data, 'image.jpg'))
                else:
                    await message.channel.send(m)
        # ------- when a D.C is selected -------------
        else:
            # ---------- "myside" direct command -----------------
            if cc == "myside":
                async with aiohttp.ClientSession() as session:
                    async with session.get("https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSTTzOG8xtq--BBFjcHE13DyU0EvXmKWohDnw&usqp=CAU") as resp:
                        data = io.BytesIO(await resp.read())
                        await message.channel.send(file=discord.File(data, 'image.jpg'))

            # --------- "power" direct command --------------------
            if cc == "power":
                async with aiohttp.ClientSession() as session:
                    async with session.get(random.choice(POWER_urls)) as resp:
                        data = io.BytesIO(await resp.read())
                        await message.channel.send(file=discord.File(data, 'image.gif'))

            # ----- "kermit meme" ------
            if cc == "noschool":
                await message.channel.send("https://i.imgflip.com/27mcwr.gif")
            # oof
            if cc == "oof":
                async with aiohttp.ClientSession() as session:
                    async with session.get("https://images-na.ssl-images-amazon.com/images/I/61IwNTw0fCL._AC_UL600_SR600,600_.png") as resp:
                        data = io.BytesIO(await resp.read())
                        await message.channel.send(file=discord.File(data, 'image.png'))
            # boom
            if cc == "boom":
                await message.channel.send("https://gfycat.com/querulousspecificfossa")
            # arson
            if cc == "arson":
                await message.channel.send("https://filmdaily.co/wp-content/uploads/2020/06/meme-03.gif")
            # slap
            if cc == "slap":
                await message.channel.send("https://tenor.com/view/fight-push-penguin-slap-gif-5543928")
            # uno reverse
            if cc == "reverse":
                await message.channel.send("https://tenor.com/view/reverse-uno-card-game-colorful-gif-16633402")
            if cc == "breaksnowbot":
                for _ in range(0, 10):
                    await message.channel.send("hello")
                    await message.channel.send("snowbot")

    await client.process_commands(message)


@client.command()
async def clear(ctx, lmt_arg: int):
    role = str(ctx.author.roles)

    # check if user has x role (so that they won't clear anything only authorized can)
    h_count = 0
    for i in ADMIN_ROLES:
        if i in role:
            h_count += 1

    # has x role
    if h_count != 0:
        await ctx.channel.purge(limit=int(lmt_arg)+1)
    # doesn't have x role
    else:
        m = random.choice(ERROR_RESPONSE_1)
        if m[0] == "img":
            async with aiohttp.ClientSession() as session:
                async with session.get(m[1]) as resp:
                    data = io.BytesIO(await resp.read())
                    await ctx.send(file=discord.File(data, 'image.jpg'))
        else:
            await ctx.send(m)


@client.command()
async def google_meme(ctx):
    link = google_memer.fetcher()
    await ctx.send(link)


@client.command()
async def MATH(ctx, math_arg: str):
    role = str(ctx.author.roles)

    # check if x user has role (so that they won't list giant numbers,only authorized can)
    h_count = 0
    for i in ADMIN_ROLES:
        if i in role:
            h_count += 1

    try:
        eq = math_arg.replace("^", "**")
        v = str(eval(eq))
        # ---content not bigger than 2000---
        if len(v) <= 2000:
            await ctx.send(v)
        # ---has x role to use the jank char limit overide-er to see the answer---
        # the limit is there so that it wont bomb the channel with text
        elif h_count != 0 and len(v) <= 30000:
            ts = len(v)//2000
            v = list(v)
            nlst = []
            for _ in range(ts):
                apo = "".join(v[0:2000])
                del v[0:2000]
                nlst.append(apo)
            if len(v) != 0:
                apo = "".join(v[0:len(v)])
                del v[0:len(v)]
                nlst.append(apo)
            for i in nlst:
                await ctx.send(i)
        # ---too big---
        else:
            await ctx.send("TO BIG TO SEND")
    # ---error handler---
    except:
        m = random.choice(ERROR_RESPONSE_0)
        if m[0] == "img":
            async with aiohttp.ClientSession() as session:
                async with session.get(m[1]) as resp:
                    data = io.BytesIO(await resp.read())
                    await ctx.send(file=discord.File(data, 'image.jpg'))
        else:
            await ctx.send(m)


@clear.error
async def clear_err(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        m = random.choice(ERROR_RESPONSE_1)
        if m[0] == "img":
            async with aiohttp.ClientSession() as session:
                async with session.get(m[1]) as resp:
                    data = io.BytesIO(await resp.read())
                    await ctx.send(file=discord.File(data, 'image.jpg'))
        else:
            await ctx.send(m)

Norm_txt_Log = True


def run(ID, mode):
    client.run(ID, bot=mode)


f_opt.f_opt({
    "-rm": ([str, bool], run)
})
