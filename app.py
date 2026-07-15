import requests
import os
import json
from dotenv import load_dotenv 
load_dotenv() 

JF_URL = os.getenv("JF")
JF_API = os.getenv("JF_KEY")
headers = {
    "Authorization": f'MediaBrowser Token="{JF_API}",'
}
response = requests.get(JF_URL, headers=headers)


API_Data = response.json()

for key in API_Data:
    print(key,":", API_Data[key])

def jellyfin():
    response = requests.get(JF_URL, headers=headers)
    jf_data = response.json()
    jf_stats = {
        "MovieCount": jf_data["MovieCount"],
        "EpisodeCount": jf_data["EpisodeCount"],
        "SongCount": jf_data["SongCount"]
    }
    with open("stats.json", "w") as jf_stat:
        json.dump(jf_stats, jf_stat)
jellyfin()