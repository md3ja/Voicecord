import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import keep_alive
import os

Verse1 = commands.Bot("v!")
Verse2 = commands.Bot("v!")
Verse3 = commands.Bot("v!")
Verse4 = commands.Bot("v!")
Verse5 = commands.Bot("v!")


class color:
	BOLD = '\033[1m'
	END = '\033[0m'
	UNDERLINE = '\033[4m'

vcid = int(input("Voice Channel Id : "))
VerseEncrypt1 = os.getenv("Token1")
VerseEncrypt2 = os.getenv("Token2")
VerseEncrypt3 = os.getenv("Token3")
VerseEncrypt4 = os.getenv("Token4")
VerseEncrypt5 = os.getenv("Token5")

os.system('clear')
print(f"""██╗░░░██╗███████╗██████╗░░██████╗███████╗
██║░░░██║██╔════╝██╔══██╗██╔════╝██╔════╝
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░█████╗░░
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██╔══╝░░
░░╚██╔╝░░███████╗██║░░██║██████╔╝███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝

────────────────────────────────────────────────────""")

print(color.BOLD + color.UNDERLINE + "VOICECORD" + color.END)

print("""
Attempting to kill discord
Logging in...
Created by DraKen""")


@Verse1.event
async def on_ready():
	channel = Verse1.get_channel(id=vcid)
	await channel.connect()
	print(f"""
[+] {Verse1.user} connected to vc!""")


@Verse2.event
async def on_ready():
	channel = Verse2.get_channel(id=vcid)
	await channel.connect()
	print(f"""
[+] {Verse2.user} connected to vc!""")


@Verse3.event
async def on_ready():
	channel = Verse3.get_channel(id=vcid)
	await channel.connect()
	print(f"""
[+] {Verse3.user} connected to vc!""")


@Verse4.event
async def on_ready():
	channel = Verse4.get_channel(id=vcid)
	await channel.connect()
	print(f"""
[+] {Verse4.user} connected to vc!""")


@Verse5.event
async def on_ready():
	channel = Verse5.get_channel(id=vcid)
	await channel.connect()
	print(f"""
[+] {Verse5.user} connected to vc!""")

keep_alive.keep_alive()

loop = asyncio.get_event_loop()
loop.create_task(Verse1.start(VerseEncrypt1, bot=False))
loop.create_task(Verse2.start(VerseEncrypt2, bot=False))
loop.create_task(Verse3.start(VerseEncrypt3, bot=False))
loop.create_task(Verse4.start(VerseEncrypt4, bot=False))
loop.create_task(Verse5.start(VerseEncrypt5, bot=False))
loop.run_forever()
