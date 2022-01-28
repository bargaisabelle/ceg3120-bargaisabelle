import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    movie_quotes = [
        'I dont even have any good skills. You know like nunchuck skills, bow hunting skills, computer hacking skills.',    
        'I am not a computer nerd. I prefer to be called a hacker',
        'Its still magic even if you know how its done',
        'Theres a new virus in the database, its replicating, eating up memory. What do I do? Type cookie you idiot',
    ]

    if message.content == 'hacker':
        response = random.choice(movie_quotes)
        await message.channel.send(response)
        await message.channel.send(file=discord.File('intro-1596024186.jpg'))

client.run(TOKEN)
