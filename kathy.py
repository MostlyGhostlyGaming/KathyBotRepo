import discord
from discord import message
from discord.ext import commands
client = discord.Client()
intents = discord.Intents.all()
client = commands.Bot(command_prefix= '.', intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'eightball', '8b'])
async def _8ball(ctx, *, question):
    ctx.send('pong')

@client.command(aliases=['h'])
async def _help(ctx):
    embed=discord.Embed(title="Help", description="Hello! I am a meme bot called Kathy. I was made simply for memes and I serve no other purpose then to be FUNNY!!! You can recommend features for me in <#877480907215343647> using the suggestions template stated below. Thank you for using me!")
    embed.set_author(name="From the developers of PrestigeMod", url="https://discord.gg/vE4PhX8NR4", icon_url="https://cdn.discordapp.com/attachments/757221765712969780/872795105256415232/unknown.png")
    embed.add_field(name="Suggestions Template", value="```\nBot Name:\nSuggestion:\nYour Username:\n```", inline=False)
    await ctx.send(embed=embed)
    print('Help command activated')

@client.event
async def on_member_join(member):
    channel = client.get_channel(877480902081515581)
    joinEmbed=discord.Embed(description=f'{member} has joined the **Official Prestige Programming Center!**\nEveryone Welcome Them!')
    await channel.send(embed=joinEmbed)
    print(f'{member} has join a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left or been removed from a server')

client.run(TOKEN)
