import discord
from discord.ext import commands
import io

class AvatarCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="avatar", description="Zeigt das Profilbild eines Nutzers an.")
    async def avatar(self, ctx, user: discord.User = None):
        user = user or ctx.author
        await ctx.defer()

        dateiformat = "gif" if user.display_avatar.is_animated() else "png"
        dateiname = f"Avatar_{user.id}.{dateiformat}"

        avatar = await user.display_avatar.read()
        bild_datei = discord.File(io.BytesIO(avatar), filename=dateiname)

        embed = discord.Embed(
            title=f"Avatar von {user.name}",
            color=discord.Color.blue()
        )
        embed.set_image(url=f"attachment://{dateiname}")
        await ctx.respond(embed=embed, file=bild_datei)

def setup(bot):
    bot.add_cog(AvatarCommand(bot))
