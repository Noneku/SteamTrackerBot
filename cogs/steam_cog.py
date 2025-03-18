import discord
from discord.ext import commands
from steam_api import get_steam_profile

class SteamCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="steam")
    async def steam(self, ctx, steam_id: str):
        """ Affiche les infos d'un utilisateur Steam """
        profile = get_steam_profile(steam_id)

        if profile:
            embed = discord.Embed(title=profile["personaname"], color=discord.Color.blue())
            embed.set_thumbnail(url=profile["avatarfull"])
            embed.add_field(name="Steam ID", value=profile["steamid"], inline=False)
            embed.add_field(name="Profil", value=f"[Lien vers le profil]({profile['profileurl']})", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("❌ Impossible de récupérer le profil Steam.")

async def setup(bot):
    await bot.add_cog(SteamCog(bot))
