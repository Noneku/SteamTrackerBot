import os
import requests
from dotenv import load_dotenv

load_dotenv()

STEAM_API_KEY = os.getenv("STEAM_API_KEY")
BASE_URL = "https://api.steampowered.com"

def get_steam_profile(steam_id):
    """ Récupère le profil Steam d'un utilisateur """
    url = f"{BASE_URL}/ISteamUser/GetPlayerSummaries/v2/"
    params = {
        "key": STEAM_API_KEY,
        "steamids": steam_id
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if "response" in data and "players" in data["response"]:
            return data["response"]["players"][0]  # Retourne le premier profil trouvé
    return None
