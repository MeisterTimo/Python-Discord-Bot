import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents, help_command=None,
    debug_guilds=[1234567890000000000] # Trage hier deine Server-ID ein!
)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound): return
    raise error

@bot.event
async def on_ready():
    activity = discord.Activity(
    type=discord.ActivityType.custom,
    state="Hallo Welt!"
)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"🟢{bot.user} ist online")


for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f"cogs.{fn[:-3]}")
        print(f"✅Loading {fn[:-3]}")

load_dotenv()
bot.run(os.getenv("TOKEN"))
