import asyncio
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands  # Importer `commands` de discord.ext
from bot_singleton import BotSingleton

# Récupérer l'instance du bot
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)  # Utiliser `commands.Bot` au lieu de `discord.Client`

# Event on_ready - Lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f"✅ {bot.user} est connecté et prêt !")
    print(f"📜 Commandes disponibles : {[command.name for command in bot.commands]}")  # Liste des commandes

    # Envoi d'un message dans un canal spécifique après le démarrage
    channel_id = int(os.getenv("DISCORD_CHANNEL_ID")) # Récupère l'ID du canal depuis le fichier .env
    channel = bot.get_channel(channel_id)  # Récupère le canal
    if channel:
        await channel.send("Le bot est prêt et fonctionne ! 🎉")  # Envoie un message dans le canal
    else:
        print("❌ Le canal n'a pas été trouvé.")

# Event on_message - Lorsque le bot reçoit un message
@bot.event 
async def on_message(message: discord.Message):
    if message.content.lower() == "!recolte":  # Vérifier si la commande est envoyée
        await message.channel.send('🌾 En route pour la récolte !')  # Envoie un message de réponse

# Fonction pour charger toutes les extensions (cogs)
async def load_extensions():
    cogs_directory = os.path.join(os.path.dirname(__file__), 'cogs')
    for filename in os.listdir(cogs_directory):
        if filename.endswith(".py") and filename != "__init__.py":
            try:
                # Utilisation de 'load_extension' au lieu de 'add_cog'
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"✅ Cog {filename} chargé avec succès.")
            except Exception as e:
                print(f"❌ Erreur lors du chargement de {filename}: {e}")

# Fonction principale pour démarrer le bot
async def main():
    load_dotenv()  # Charger les variables d'environnement depuis le fichier .env
    await load_extensions()  # Charger toutes les extensions
    await bot.start(os.getenv("DISCORD_TOKEN"))  # Lancer le bot avec le token

if __name__ == "__main__":
    asyncio.run(main())  # Lancer la fonction main
