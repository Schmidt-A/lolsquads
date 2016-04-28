import requests
from apikey import APIKEY

SUMMONER_BASE_URL = 'https://na.api.pvp.net/api/lol/{region}/v1.4/summoner/{0}'

def get_summoner_icon_value(summoner_id):
    payload = {'api_key': APIKEY}
    url = SUMMONER_BASE_URL.format(summoner_id)

    r = requests.get(url, params=payload)
    return r.json()[summoner_id]['profileIconID']
