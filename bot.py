import discord
from discord.ext import commands
import requests
import json
import random
import re
import asyncio
import os
from dotenv import load_dotenv
from craiyon import Craiyon
from flask import Flask
from threading import Thread

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
TENOR_API_KEY = os.getenv('TENOR_API_KEY')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
HUGGING_FACE_API_KEY = os.getenv('HUGGING_FACE_API_KEY')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Flask server to keep the bot alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Bot commands (trimmed for brevity)
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == 'hello':
        await message.channel.send(f'Hello, {message.author.name}!')
    
    await bot.process_commands(message)

@bot.command(name='challenge')
async def challenge(ctx):
    """Send a random coding challenge from the JSON file."""
    try:
        with open('challenges.json', 'r') as f:
            challenges = json.load(f)
        if challenges:
            challenge = random.choice(challenges)
            await ctx.send(challenge)
        else:
            await ctx.send("No challenges found.")
    except FileNotFoundError:
        await ctx.send("Challenges file not found.")
    except json.JSONDecodeError:
        await ctx.send("Error reading challenges file.")

@bot.command(name='quote')
async def quote(ctx):
    """Fetch a random motivational quote."""
    try:
        response = requests.get('https://dummyjson.com/quotes/random')
        response.raise_for_status()
        quote = response.json().get('quote')
        await ctx.send(quote if quote else "No quote found.")
    except requests.RequestException:
        await ctx.send("Couldn't fetch a quote right now.")

@bot.command(name='add')
async def add_challenge(ctx, url):
    """Add a new coding challenge URL to the JSON file."""
    if not re.match(r'^https?://', url):
        await ctx.send("Invalid URL. Please provide a valid URL starting with http:// or https://.")
        return

    try:
        with open('challenges.json', 'r+') as f:
            challenges = json.load(f)
            challenges.append(url)
            f.seek(0)
            json.dump(challenges, f, indent=4)
            f.truncate()
        await ctx.send("Challenge added successfully.")
    except (FileNotFoundError, json.JSONDecodeError):
        await ctx.send("Error reading or writing to challenges file.")

@bot.command(name='list')
async def list_challenges(ctx):
    """List all coding challenges from the JSON file."""
    try:
        with open('challenges.json', 'r') as f:
            challenges = json.load(f)
        if challenges:
            challenge_list = '\n'.join(challenges)
            await ctx.send(f"Available Challenges:\n{challenge_list}")
        else:
            await ctx.send("No challenges available.")
    except (FileNotFoundError, json.JSONDecodeError):
        await ctx.send("Error reading challenges file.")

@bot.command(name='poll')
async def poll(ctx, question: str, *options: str):
    """Create a poll with up to 10 options."""
    if len(options) < 2:
        await ctx.send("You need at least two options to create a poll.")
        return
    if len(options) > 10:
        await ctx.send("You can only provide up to 10 options.")
        return

    description = ""
    emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
    for i, option in enumerate(options):
        description += f"{emojis[i]} {option}\n"

    embed = discord.Embed(title=question, description=description)
    poll_message = await ctx.send(embed=embed)

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
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
        await ctx.send(f"📖 Definition of {word}: {definition}")
    except (requests.RequestException, KeyError, IndexError):
        await ctx.send("Word not found. Please try a different word.")

@bot.command(name='remind')
async def remind(ctx, time: int, *, reminder: str):
    """Set a reminder."""
    await ctx.send(f"⏰ Reminder set! I'll remind you in {time} seconds.")
    await asyncio.sleep(time)
    await ctx.send(f"🔔 Reminder: {reminder}")

@bot.command(name='song')
async def song(ctx, *, track_name: str):
    """Search for a song on YouTube and return the first result link."""
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={track_name}&key={YOUTUBE_API_KEY}&type=video"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data['items']:
            video_id = data['items'][0]['id']['videoId']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            await ctx.send(f"Here's what I found for **{track_name}**: {video_url}")
        else:
            await ctx.send("No results found.")
    except requests.RequestException:
        await ctx.send("There was an error fetching the song. Please try again later.")

@bot.command(name='gif')
async def gif(ctx, *, search_term: str):
    """Fetches a random GIF related to the search term from Tenor."""
    url = f"https://tenor.googleapis.com/v2/search?q={search_term}&key={TENOR_API_KEY}&limit=10"
    try:
        response = requests.get(url)
        response.raise_for_status()
        gifs = response.json().get('results')
        
        if gifs:
            gif_url = random.choice(gifs).get('media_formats', {}).get('gif', {}).get('url')
            if gif_url:
                await ctx.send(gif_url)
            else:
                await ctx.send("No GIF found for this search term.")
        else:
            await ctx.send("No results found.")
    except requests.RequestException as e:
        await ctx.send("There was an error fetching the GIF. Please try again later.")
        print(e)

@bot.command(name='weather')
async def weather(ctx, *, location: str = None):
    """Fetches current weather data for a specified location."""
    if location is None:
        await ctx.send("Please specify a location. Usage: `!weather <location>`")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={location}&aqi=no"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        location_name = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        feelslike_c = data['current']['feelslike_c']
        humidity = data['current']['humidity']
        wind_kph = data['current']['wind_kph']

        weather_report = (
            f"**Weather in {location_name}, {region}, {country}**\n"
            f"🌡️ Temperature: {temp_c}°C (Feels like {feelslike_c}°C)\n"
            f"🌥️ Condition: {condition}\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌬️ Wind Speed: {wind_kph} kph\n"
        )
        await ctx.send(weather_report)

    except requests.RequestException:
        await ctx.send("There was an error fetching the weather data. Please try again later.")
    except KeyError:
        await ctx.send("Could not find weather information for that location. Please check the location and try again.")

@bot.command(name='image')
async def generate_image(ctx, *, prompt: str):
    """Generates an AI image based on a text prompt using Hugging Face's Stable Diffusion."""
    await ctx.send("Generating your image, please wait...")

    url = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
    payload = {"inputs": prompt}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status() 

        image_data = response.content
        image_filename = "generated_image.png"
        with open(image_filename, "wb") as f:
            f.write(image_data)

        await ctx.send(file=discord.File(image_filename))

    except requests.RequestException as e:
        print(f"Error generating image: {e}")
        await ctx.send("There was an error generating the image. Please try again later.")

# Start the Discord bot
bot.run(TOKEN)
