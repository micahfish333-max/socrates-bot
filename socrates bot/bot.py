import discord
import random
import time
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# ⏱️ cooldown (seconds)
cooldowns = {}
COOLDOWN_SECONDS = 3

QUOTES = [
"The only true wisdom is in knowing you know nothing.",
"An unexamined life is not worth living.",
"I cannot teach anybody anything. I can only make them think.",
"To find yourself, think for yourself.",
"Be as you wish to seem.",
"Wonder is the beginning of wisdom.",
"He who is not contented with what he has would not be contented with what he would like to have.",
"Education is the kindling of a flame, not the filling of a vessel.",
"True knowledge exists in knowing that you know nothing.",
"Beware the barrenness of a busy life.",
"The greatest way to live with honor in this world is to be what we pretend to be.",
"From the deepest desires often come the deadliest hate.",
"Contentment is natural wealth, luxury is artificial poverty.",
"Prefer knowledge to wealth, for the one is transitory, the other perpetual.",
"He is richest who is content with the least.",
"The secret of happiness is not found in seeking more, but in developing the capacity to enjoy less.",
"Every action has its pleasures and its price.",
"If a man is proud of his wealth, he should not be praised until it is known how he employs it.",
"Not life, but good life, is to be chiefly valued.",
"Death may be the greatest of all human blessings.",
"Let him who would move the world first move himself.",
"Envy is the ulcer of the soul.",
"The easiest and noblest way is not to be crushing others, but to be improving yourselves.",
"Think not those faithful who praise all thy words and actions; but those who kindly reprove thy faults.",
"Strong minds discuss ideas, average minds discuss events, weak minds discuss people.",
"There is only one good, knowledge, and one evil, ignorance.",
"To know, is to know that you know nothing.",
"No evil can happen to a good man, either in life or after death.",
"Be slow to fall into friendship, but when you are in, continue firm and constant.",
"Employ your time in improving yourself by other men’s writings.",
"Once made equal to man, woman becomes his superior.",
"Our prayers should be for blessings in general, for God knows best what is good for us.",
"The beginning of wisdom is a definition of terms.",
"He is a man of courage who does not run away, but remains at his post and fights against the enemy.",
"Where there is reverence there is fear, but there is not reverence everywhere that there is fear.",
"If all misfortunes were laid in one common heap, most would be content to take their own and depart.",
"The hottest love has the coldest end.",
"Understanding a question is half an answer.",
"He who would be a good servant must be a good master.",
"Not those who have much are rich, but those who need little.",
"We cannot live better than in seeking to become better.",
"All men’s souls are immortal, but the souls of the righteous are immortal and divine.",
"Be nicer than necessary to everyone you meet.",
"The only good is knowledge and the only evil is ignorance."
]

def check_cooldown(user_id):
    now = time.time()
    if user_id in cooldowns:
        if now - cooldowns[user_id] < COOLDOWN_SECONDS:
            return False
    cooldowns[user_id] = now
    return True

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    is_mentioned = client.user in message.mentions
    is_reply_to_bot = False

    if message.reference:
        try:
            replied_msg = await message.channel.fetch_message(message.reference.message_id)
            if replied_msg.author == client.user:
                is_reply_to_bot = True
        except:
            pass

    is_command = message.content.lower().startswith("!quote")

    if is_mentioned or is_reply_to_bot or is_command:
        if not check_cooldown(message.author.id):
            await message.reply("⏱️ chill bro, wait a sec 😭")
            return

        quote = random.choice(QUOTES)
        await message.reply(f"💭 {quote}")

# 🔑 token from environment variable
client.run(os.getenv("TOKEN"))