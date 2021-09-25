import os
import random

import discord
from discord.errors import Forbidden
from discord.ext import commands

TOKEN = os.getenv('TOKEN') # Fetch token from .env
intents = discord.Intents.all() # all discord intents, requires manual setup at discord.com/developers
client = commands.Bot(command_prefix='.', intents=intents) # Initialize 'client' with all intents and the prefix '.'

@client.event # new client event
async def on_ready(): # on_ready means the bot connected to discords api successfully
    print(f'Logged in with {client.user}') # client.user is your bot

@client.command() # New Bot command
async def hello(ctx): # Define command 'hello'
    await ctx.reply('Hello ;)', mention_author=False) # reply with hello without mentioning the author

@client.command(aliases=['pm']) # new command with an alias
async def pingme(ctx): # Define command pingme
    mention = ctx.author # get message author
    await ctx.send(f'{mention.mention} triggered!') # send triggered with the author mentioned

@client.command(aliases=['rng'])
async def randomnumbergen(ctx, a, b): # Define command randomnumbergen
    a = int(a) # Define a as integer
    b = int(b) # Define b as integer
    await ctx.reply(random.randint(a, b), mention_author=False) # reply with a random number between a and b

@client.command(aliases=['txt'])
async def text(ctx, user : discord.Member ,chn : discord.TextChannel): # Define command text
    await ctx.message.delete() # delete original message
    await ctx.send(f'{user.mention} Refer to {chn.mention}!') # send message with the user and textchannel mentioned

client.run(TOKEN) # run client with token
