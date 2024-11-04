# ChattyCat Discord Bot

ChattyCat is a Discord bot designed to enhance user engagement and interaction by providing various utilities such as quotes, reminders, polls, definitions, coin flips, and coding challenges. This bot is easy to use and integrates well into any server for fun and productivity.

## Features

1. **Greetings**: The bot greets users when they send a "hello" message.

2. **Motivational Quotes**: Users can request motivational quotes to stay inspired by using the command `!quote`.

3. **Reminders**: Users can set reminders specifying the number of seconds after which they should be reminded using `!remind <seconds> <reminder>`.

4. **Polls**: Users can create simple polls to gather opinions from server members using `!poll <question> <opt1> <opt2>...`.

5. **Definitions**: Get definitions of words using `!define <word>`.
   
6. **Coin Flip**: Flip a coin to get a random result of "Heads" or "Tails" using `!coinflip`.

7. **Coding Challenges**: Users can interact with coding challenges with various commands:
    - `!challenge`: Get a random coding challenge.
    - `!add <link>`: Add a new coding challenge link.
    - `!list`: List all available coding challenges.

8. **YouTube Song Search**: Search for a song on YouTube and get a link to the first result using `!song <track_name>`.

9. **GIF Search**: Fetch a random GIF related to the search term from Tenor using `!gif <search_term>`.

10. **Weather Information**: Fetch current weather data for a specified location using `!weather <location>`.

11. AI-Generated Images: Generate an AI image based on a text prompt using Hugging Face's Stable Diffusion model with ``!image <prompt>``.
     
## Deployment
The project can be deployed by running the bot script (bot.py) on a server that is always online, such as Heroku or AWS.

## Contributing
Feel free to open a pull request for any improvements or new features. Contributions are always welcome.
