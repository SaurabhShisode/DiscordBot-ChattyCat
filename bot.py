import discord
from discord.ext import commands
import requests
import json
import random
import re

TOKEN = 'YOUR TOKEN'


intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == 'hello':
        await message.channel.send(f'Hello, {message.author.name}!')
    
    await bot.process_commands(message)


@bot.command(name='challenge')
async def challenge(ctx):
    with open('challenges.json', 'r') as f:
        challenges = json.load(f)
        challenge = random.choice(challenges)
        await ctx.send(challenge)

@bot.command(name='quote')
async def quote(ctx):
    response = requests.get('https://dummyjson.com/quotes/random')
    if response.status_code == 200:
        quote = response.json().get('quote')
        await ctx.send(quote)
    else:
        await ctx.send("Couldn't fetch a quote right now.")

@bot.command(name='add')
async def add_challenge(ctx, url):
    if not re.match(r'^https?://', url):
        await ctx.send("Invalid URL. Please provide a valid URL starting with http:// or https://.")
        return
    with open('challenges.json', 'r+') as f:
 
        challenges = json.load(f)
        challenges.append(url)
        f.seek(0)
        json.dump(challenges, f, indent=4)
        f.truncate() 
    await ctx.send("Challenge added successfully.")

@bot.command(name='list')
async def list_challenges(ctx):
    with open('challenges.json', 'r') as f:
        challenges = json.load(f)
        challenge_list = '\n'.join(challenges)
        await ctx.send(f"Available Challenges:\n{challenge_list}")

@bot.command(name='poll')
async def poll(ctx, question: str, *options: str):
    """Create a poll with up to 10 options."""
    if len(options) < 2:
        await ctx.send("You need at least two options to create a poll.")
        return
    if len(options) > 10:
        await ctx.send("You can only provide up to 10 options.")
        return

    # Creating the poll message
    description = ""
    emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
    for i, option in enumerate(options):
        description += f"{emojis[i]} {option}\n"

    embed = discord.Embed(title=question, description=description)
    poll_message = await ctx.send(embed=embed)

    # Adding reactions for each option
    for i in range(len(options)):
        await poll_message.add_reaction(emojis[i])

@bot.command(name='coinflip')
async def coinflip(ctx):
    """Flip a coin."""
    result = random.choice(['Heads', 'Tails'])
    await ctx.send(f'🪙 The coin landed on: {result}!')

@bot.command(name='define')
async def define(ctx, *, word: str):
    """Get the definition of a word."""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
        await ctx.send(f"📖 Definition of {word}: {definition}")
    else:
        await ctx.send("Word not found. Please try a different word.")

import asyncio

@bot.command(name='remind')
async def remind(ctx, time: int, *, reminder: str):
    """Set a reminder."""
    await ctx.send(f"⏰ Reminder set! I'll remind you in {time} seconds.")
    await asyncio.sleep(time)
    await ctx.send(f"🔔 Reminder: {reminder}")

bot.run(TOKEN)
