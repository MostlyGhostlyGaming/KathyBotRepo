# KathyBot

KathyBot is a discord bot made in Python using discord.py. 

## Why

This discord bot was made because I wanted to learn a new coding language. All my discord bots (including [PrestigeMod](https://discord.com/oauth2/authorize?client_id=835723743107088402&permissions=8&scope=bot)) are coded in JavaScript using [Node.js](https://nodejs.org/en/). This bot is mainly just me learning a new coding language because I wanted to. 

## Some Tutorial

So if u wanna learn how to code a bot in python, well I'll teach you how to set it up.

First, Install your programs

* [Python3](https://www.python.org/downloads/)
* [IDE](https://www.eclipse.org/ide/) or [Code Editor](https://code.visualstudio.com)

### Installing discord.py

Open console by typing `cmd` In your search bar and clicking **Run as Administrator**. If you don't run as administrator it might not work correctly.

Type this in console

* `py -3.6 -m pip install -U discord.py[voice]` For voice support
* `py -3.6 -m pip install -U discord.py` for without voice support

Now make your bot.py file. 

Your half way there, Congrats.

## Coding

Start by putting down some basic code
```python
import discord
from discord.ext import commands
client = discord.Client()
intents = discord.Intents.all()
client = commands.Bot(command_prefix= '<your prefix of choice>', intents=intents)

client.run('<your token>')
```
Now make your ready function
```python
@client.event
async def on_ready():
    print('Bot Ready!')
```
Your file should look like this
```python
import discord
from discord.ext import commands
client = discord.Client()
intents = discord.Intents.all()
client = commands.Bot(command_prerfix= '<your prefix of choice>', intents=intents)

@client.event
async def on_ready():
     print('Bot Ready!')

client.run('<your token>')
```
Run that and boom, discord bot running.


Im to lazy to write more so just check out the [documentation](https://discordpy.readthedocs.io/en/stable/). 

Ok bye
