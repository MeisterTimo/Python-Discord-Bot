import discord
from discord.ext import commands
import platform
import sys

class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="info_bot", description="Zeigt Informationen über den Bot an.")
    async def info_bot(self, ctx: discord.ApplicationContext):
        bot = self.bot

        bot_name = bot.user.name
        bot_id = bot.user.id
        erstellt_am = bot.user.created_at.strftime("%d.%m.%Y")
        ping = int(bot.latency * 1000)

        betriebssystem = platform.system()
        python_version = sys.version.split()[0]
        pycord_version = discord.__version__

        embed = discord.Embed(
            title="Bot-Infos",
            color=discord.Color.blue()
        )

        embed.add_field(name="🤖 Bot Name", value=f"```{bot_name}```", inline=False)
        embed.add_field(name="🆔 Bot ID", value=f"```{bot_id}```", inline=False)
        embed.add_field(name="📅 Erstellt am", value=f"```{erstellt_am}```", inline=False)
        embed.add_field(name="📶 Ping", value=f"```{ping}ms```", inline=False)
        embed.add_field(name="💻 Betriebssystem", value=f"```{betriebssystem}```", inline=False)
        embed.add_field(name="🐍 Python Version", value=f"```{python_version}```", inline=True)
        embed.add_field(name="😎 Pycord Version", value=f"```{pycord_version}```", inline=True)

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(BotInfo(bot))
