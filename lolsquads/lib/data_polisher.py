import ddragon
import riotapi

def get_summoner_icon_url(summoner_id):
    summoner_icon = riotapi.get_summoner_icon_value(summoner_id))
    return ddragon.summoner_icon_url(summoner_icon)
