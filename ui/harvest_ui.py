# ui/harvest_ui.py
import discord

class HarvestUI(discord.ui.View):
    def __init__(self):
        super().__init__()
        # Ajoute ici les boutons ou autres éléments interactifs pour l'UI

    @discord.ui.button(label="Récolter", style=discord.ButtonStyle.green)
    async def recolter_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("Vous avez choisi de récolter !")
