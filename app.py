import requests
import os
import json
from dotenv import load_dotenv 
load_dotenv() 

# jellyfin api urls/keys
JF_URL = os.getenv("JF")
JF_API = os.getenv("JF_KEY")
JF_HEADERS = {
    "Authorization": f'MediaBrowser Token="{JF_API}"'
}

#seerr api urls/keys
SEERR_URL = os.getenv("SEERR_URL")
SEERR_KEY = os.getenv("SEERR_KEY")
SEERR_HEADERS = {
    "X-API-Key": SEERR_KEY
}

#seerr api urls/keys
PROWLARR_URL = os.getenv("PROWLARR_URL")
PROWLARR_KEY = os.getenv("PROWLARR_KEY")
PROWLARR_HEADERS = {
    "X-API-Key": PROWLARR_KEY
}

def jellyfin():
    response = requests.get(f"{JF_URL}/Items/Counts", headers=JF_HEADERS)
    data = response.json()
    return {
        "MovieCount": data["MovieCount"],
        "EpisodeCount": data["EpisodeCount"],
        "SongCount": data["SongCount"]
    }

def seerr():
    response = requests.get(f"{SEERR_URL}/api/v1/request/count", headers=SEERR_HEADERS)
    data = response.json()
    return {
        "RequestsTotal": data["total"],
        "RequestsPending": data["pending"],
        "RequestsApproved": data["approved"],
    }

def prowlarr():
    response = requests.get(f"{PROWLARR_URL}/api/v1/system/status", headers=PROWLARR_HEADERS)
    data = response.json()
    return {
        "ProwlarrVersion": data["version"],
    }

def results():
    stats = {}
    stats.update(jellyfin())
    stats.update(seerr())
    stats.update(prowlarr())

    with open("./homepage/stats.json", "w") as f:
        json.dump(stats, f)
        print(stats)
jellyfin()
seerr()
prowlarr()
results()