ChattyCat Discord Bot

ChattyCat is a Discord bot designed to enhance user engagement and interaction by providing various utilities such as quotes, reminders, polls, definitions, coin flips, and coding challenges. This bot is easy to use and integrates well into any server for fun and productivity.

Features

Greetings: The bot greets users when they send a "hello" message.

Example:

User: hello
ChattyCat: Hello, smoky07830!

Motivational Quotes: Users can request motivational quotes to stay inspired by using the command !quote.

Example:

User: !quote
ChattyCat: Those Who Dare To Fail Miserably Can Achieve Greatly.

Reminders: Users can set reminders for themselves, specifying the number of seconds after which they should be reminded.

Example:

User: !remind 10 run
ChattyCat: Reminder set! I'll remind you in 10 seconds.
ChattyCat: Reminder: run

Polls: Users can create simple polls to collect opinions from server members. The command format allows specifying the poll question and the options.

Example:

User: !poll BGT? India Australia
ChattyCat: — 
BGT?
1. India
2. Australia

Definitions: Users can get definitions of words using the !define command.

Example:

User: !define placements
ChattyCat: 📜 Definition of placements: The act of placing or putting in place; the act of locating or positioning; the state of being placed.

Coin Flip: Users can flip a coin to get a random result of "Heads" or "Tails" using the !coinflip command.

Example:

User: !coinflip
ChattyCat: 🎖 The coin landed on: Tails!

Coding Challenges: Users can interact with coding challenges using various commands:

!challenge: Get a random coding challenge.

!add <link>: Add a new coding challenge link.

!list: List all available coding challenges.

Example:

User: !challenge
ChattyCat: https://codingchallenges.fyi/challenges/3

User: !add https://leetcode.com/problems/middle-of-the-linked-list/
ChattyCat: Challenge added successfully.

User: !list
ChattyCat: Available Challenges:
https://codingchallenges.fyi/challenges/1
https://codingchallenges.fyi/challenges/2
https://codingchallenges.fyi/challenges/3
https://leetcode.com/problems/middle-of-the-linked-list/

How to Install

Clone the repository:

git clone <repository-url>

Install dependencies using pip:

pip install -r requirements.txt

Create a .env file with your Discord bot token:

DISCORD_TOKEN=<your-bot-token>

Run the bot:

python bot.py

Usage

Once the bot is added to your Discord server, use the commands listed above to interact with it.

All commands start with a !.

Commands

Command

Description

hello

Greet the bot

!quote

Get a motivational quote

!remind <time> <task>

Set a reminder for <time> seconds and receive a prompt to <task>

!poll <question> <option1> <option2>

Create a poll with options

!define <word>

Get the definition of a word

!coinflip

Flip a coin to get "Heads" or "Tails"

!challenge

Get a random coding challenge

!add <link>

Add a new coding challenge link

!list

List all available coding challenges

Contributing

Contributions are welcome! Feel free to fork this project and submit a pull request.

License

This project is licensed under the MIT License.
