from discord.ext import commands

class HarvestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="recolte")
    async def _recolte(self, ctx):
        """Affiche l'UI pour choisir un métier de récolte"""
        await ctx.send("🌿 **Choisissez un métier de récolte :**")

# Charger le cog au démarrage
async def setup(bot):
    await bot.add_cog(HarvestCog(bot))
