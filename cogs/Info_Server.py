import discord
from discord.ext import commands

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="info_server", description="Zeigt Informationen über den Server an.")
    async def info_server(self, ctx: discord.ApplicationContext):
        server = ctx.guild
        besitzer = await server.fetch_member(server.owner_id)

        mitglieder_anzahl = server.member_count
        bot_anzahl = 0
        for mitglied in server.members:
            if mitglied.bot:
                bot_anzahl += 1

        textkanal_anzahl = len(server.text_channels)
        sprachkanal_anzahl = len(server.voice_channels)
        rollen_anzahl = len(server.roles)
        erstellt_am = server.created_at.strftime("%d.%m.%Y")

        embed = discord.Embed(
            title=server.name,
            color=discord.Color.blue()
        )

        embed.add_field(name="👑 Besitzer", value=f"```{besitzer.name}```", inline=False)
        embed.add_field(name="🧑 Mitglieder", value=f"```{mitglieder_anzahl}```", inline=True)
        embed.add_field(name="🤖 Bots", value=f"```{bot_anzahl}```", inline=True)
        embed.add_field(name="🆔 Server ID", value=f"```{server.id}```", inline=False)
        embed.add_field(name="📅 Erstellt am", value=f"```{erstellt_am}```", inline=False)
        embed.add_field(name="💬 Textkanäle", value=f"```{textkanal_anzahl}```", inline=True)
        embed.add_field(name="🔊 Sprachkanäle", value=f"```{sprachkanal_anzahl}```", inline=True)
        embed.add_field(name="🎭 Rollen", value=f"```{rollen_anzahl}```", inline=True)

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(ServerInfo(bot))
