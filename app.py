import requests
import os
from fastapi import FastAPI
from dotenv import load_dotenv 
load_dotenv() 
app = FastAPI()

JF_URL = os.getenv("JF")
JF_API = os.getenv("JF_KEY")
headers = {
    "Authorization": f'MediaBrowser Token="{JF_API}",'
}
response = requests.get(JF_URL, headers=headers)


API_Data = response.json()

for key in API_Data:
    print(key,":", API_Data[key])

@app.get("/api/jellyfin")
def jellyfin():
    response = requests.get(JF_URL, headers=headers)
    jf_data = response.json()
    return {
        "MovieCount": jf_data["MovieCount"],
        "SeriesCount": jf_data["SeriesCount"],
        "SongCount": jf_data["SongCount"]
    }