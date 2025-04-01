# bot/bot_singleton.py
import discord
from discord.ext import commands

class BotSingleton:
    _instance = None

    @classmethod
    def get_bot(cls):
        if cls._instance is None:
            intents = discord.Intents.default()
            intents.messages = True
            intents.guilds = True
            cls._instance = commands.Bot(command_prefix="!", intents=intents)
        return cls._instance
