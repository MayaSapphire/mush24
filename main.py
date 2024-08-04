import discord
import mush

BOT_NAME = "Mush '24"

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count += 1

    print(f"{BOT_NAME} is in {str(guild_count)} guilds.")


@bot.event
async def on_message(message):
    to_send = mush.send_message(message)
    await message.channel.send(to_send)


def push_to_main(message:str):
    for guild in bot.guilds:
        guild.get_channel(1269444451684843563).send(message)


bot.run(open('handle.txt', 'r').read())
