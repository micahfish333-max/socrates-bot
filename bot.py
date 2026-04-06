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

# 🔹 10 short quotes
"I know that I know nothing. — Socrates",
"I think, therefore I am. — René Descartes",
"Man is condemned to be free. — Jean-Paul Sartre",
"God is dead. — Friedrich Nietzsche",
"Happiness is the highest good. — Aristotle",
"Virtue is knowledge. — Socrates",
"Know thyself. — Socrates",
"The only thing necessary for evil to triumph is for good men to do nothing. — Edmund Burke",
"Man is the measure of all things. — Protagoras",
"Freedom is the will to be responsible to ourselves. — Friedrich Nietzsche",

# 🔹 20 medium quotes (1–2 sentences)
"An unexamined life is not worth living, for without reflection we cannot truly understand ourselves. — Socrates",
"You have power over your mind, not outside events. Realize this and you will find strength. — Marcus Aurelius",
"The impediment to action advances action. What stands in the way becomes the way. — Marcus Aurelius",
"Do not act as if you were going to live ten thousand years. Death hangs over you while you live. — Marcus Aurelius",
"All men by nature desire to know, and this desire leads them toward understanding. — Aristotle",
"Happiness depends upon ourselves, not external circumstances. — Aristotle",
"Man is born free, and everywhere he is in chains. — Jean-Jacques Rousseau",
"Freedom is not doing what we want, but having the ability to choose what is right. — Immanuel Kant",
"I cannot teach anybody anything. I can only make them think. — Socrates",
"Waste no more time arguing what a good man should be. Be one. — Marcus Aurelius",
"He who has a why to live can bear almost any how. — Friedrich Nietzsche",
"To do injustice is more shameful than to suffer it. — Plato",
"The beginning is the most important part of the work. — Plato",
"Justice means giving each what is owed, creating balance in society. — Plato",
"One cannot step into the same river twice. — Heraclitus",
"The soul becomes dyed with the color of its thoughts. — Marcus Aurelius",
"Pleasure in the job puts perfection in the work. — Aristotle",
"Liberty consists in doing what one desires. — John Stuart Mill",
"The mind is everything; what you think, you become. — Buddha",
"He who opens a school door closes a prison. — Victor Hugo",

# 🔹 30 longer quotes (4–5 sentences)
"The unexamined life is not worth living because without reflection we live without purpose or direction. Socrates believed that true wisdom comes from questioning our beliefs and actions. By examining ourselves, we can improve and grow. Without this, life becomes empty and automatic. — Socrates",

"You have power over your mind, not outside events. When you accept this, you gain control over how you respond to the world. External events cannot disturb your inner peace unless you allow them to. This understanding is the foundation of true strength. — Marcus Aurelius",

"The impediment to action advances action. Difficulties are not obstacles but opportunities to grow stronger. When we face challenges, we develop resilience and wisdom. What stands in the way becomes part of the path forward. — Marcus Aurelius",

"Do not waste time arguing about what a good person should be. Instead, focus on becoming one through your actions. Living well requires discipline, consistency, and self-awareness. Your character is built through what you do, not what you say. — Marcus Aurelius",

"Man is condemned to be free, meaning we are responsible for all our choices. There is no escaping this responsibility, even when we try to avoid it. Our actions define who we are. Freedom carries both power and burden. — Jean-Paul Sartre",

"Existence precedes essence, meaning we are not born with a fixed purpose. Instead, we create our identity through our choices. This gives us complete freedom but also full responsibility. We shape ourselves through action. — Jean-Paul Sartre",

"I think, therefore I am. This statement proves that the act of thinking confirms existence. Even if everything else is doubted, the thinker cannot be denied. Awareness itself is proof of being. — René Descartes",

"Know thyself, for understanding your own nature is the beginning of wisdom. Without self-knowledge, you cannot truly improve. Reflection allows you to see your strengths and weaknesses. This awareness leads to growth. — Socrates",

"Happiness is the highest good, because all human actions aim toward it. Aristotle believed that a good life is one lived with virtue and reason. External success alone is not enough. True happiness comes from within. — Aristotle",

"Man is born free, yet society often places chains upon him. These chains can limit freedom and individuality. True freedom requires awareness and independence of thought. Only then can a person act according to their will. — Jean-Jacques Rousseau",

"The only thing necessary for evil to triumph is for good men to do nothing. When people stay silent, injustice spreads. Action is required to maintain justice and order. Silence in the face of wrong is a form of permission. — Edmund Burke",

"The mind is everything; what you think, you become. Your thoughts shape your actions, and your actions shape your life. Positive thinking leads to positive outcomes. Master your mind, and you master your life. — Buddha",

"He who has a why to live can bear almost any how. A strong purpose allows a person to endure suffering. Meaning gives strength in difficult times. Without purpose, life becomes harder to sustain. — Friedrich Nietzsche",

"One cannot step into the same river twice, because both the river and the person are constantly changing. This reflects the nature of reality. Everything is in constant motion and transformation. Nothing remains the same. — Heraclitus",

"The beginning is the most important part of the work because it sets the foundation for everything that follows. A strong start leads to better outcomes. Careful planning is essential. Success often depends on how things begin. — Plato",

"Justice means giving each what is owed, ensuring fairness in society. It requires balance between individuals and the community. Without justice, society becomes unstable. Fairness creates harmony. — Plato",

"Pleasure in the job puts perfection in the work. When you enjoy what you do, your work improves. Motivation leads to higher quality. Passion drives excellence. — Aristotle",

"Freedom is not doing whatever we want, but acting according to reason. True freedom involves self-control and responsibility. Without reason, freedom becomes chaos. Discipline defines true liberty. — Immanuel Kant",

"The soul becomes dyed with the color of its thoughts. Our thoughts shape our character and outlook on life. Positive thoughts lead to positive living. What we focus on defines us. — Marcus Aurelius",

"He who opens a school door closes a prison, because education removes ignorance. Knowledge creates opportunity and freedom. Learning transforms individuals and society. Education is a path to liberation. — Victor Hugo",

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
