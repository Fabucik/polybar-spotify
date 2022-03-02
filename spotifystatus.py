import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()


current_track_url = "https://api.spotify.com/v1/me/player/currently-playing"

SPT_TOKEN = os.environ["spt_token"]

def get_current_track(token):
    response = requests.get(current_track_url, headers={"Authorization": "Bearer {0}".format(token)})
    resp_json = json.loads(response.content)
    track_name = resp_json["item"]["name"]
    track_artists = resp_json["item"]["artists"]
    artist_name = ", ".join([artist["name"] for artist in track_artists])
    
    finalString = artist_name + " - " + track_name

    return finalString

try:
    current_track_info = get_current_track(SPT_TOKEN)
    print(current_track_info)
except:
    print("")
