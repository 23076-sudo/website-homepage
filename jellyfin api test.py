import requests
import os
from dotenv import load_dotenv 
load_dotenv() 

JF_URL = os.getenv("JF")
JF_API = os.getenv("JF_KEY")
headers = {
    "Authorization": f'MediaBrowser Token="{JF_API}",'
}
response = requests.get(JF_URL, headers=headers)


API_Data = response.json()

for key in API_Data:{
    print(key,":", API_Data[key])
}
