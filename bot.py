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
QUOTES += [
"Man is born free, and everywhere he is in chains.",
"The unexamined life is not worth living.",
"I think, therefore I am.",
"Happiness depends upon ourselves.",
"It is the mark of an educated mind to entertain a thought without accepting it.",
"Knowing yourself is the beginning of all wisdom.",
"The only thing I know is that I know nothing.",
"Do not do to others what angers you if done to you.",
"The greatest wealth is to live content with little.",
"Virtue is its own reward.",
"He who opens a school door closes a prison.",
"Liberty consists in doing what one desires.",
"The aim of the wise is not to secure pleasure, but to avoid pain.",
"It is not enough to have a good mind; the main thing is to use it well.",
"Time is the moving image of eternity.",
"The beginning is the most important part of the work.",
"Justice means giving each what is owed.",
"The wise man does not lay up his own treasures.",
"Excellence is never an accident.",
"Pleasure in the job puts perfection in the work.",
"Silence is the sleep that nourishes wisdom.",
"To do injustice is more shameful than to suffer it.",
"The root of education is bitter, but the fruit is sweet.",
"Without music, life would be a mistake.",
"Man cannot remake himself without suffering.",
"All that is necessary for evil to succeed is that good men do nothing.",
"The highest form of knowledge is empathy.",
"He who is brave is free.",
"A wise man speaks because he has something to say.",
"Education is the best provision for old age.",
"The mind is everything; what you think you become.",
"Those who know do not speak; those who speak do not know.",
"The journey of a thousand miles begins with a single step.",
"The greater the difficulty, the more glory in surmounting it.",
"He who conquers himself is the mightiest warrior.",
"To rule oneself is the ultimate power.",
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
import os
print("TOKEN =", os.getenv("TOKEN"))
# 🔑 token from environment variable
client.run(os.getenv("TOKEN"))
