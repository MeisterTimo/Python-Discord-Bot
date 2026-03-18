import discord
from discord.ext import commands

class CogClassTemplate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Hier der Code

def setup(bot):
    bot.add_cog(CogClassTemplate(bot))
