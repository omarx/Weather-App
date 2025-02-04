import os
import json
from dotenv import load_dotenv
from db_operations import *
import requests

load_dotenv()
api_key: str= os.getenv("API_KEY")
data_url:str =os.getenv("DATA_URL")
coord_url:str = os.getenv("COORD_URL")


def get_coordinates(city:str) -> list:
    try:
        response:any =requests.get(coord_url+city+"&appid="+api_key)
        response.raise_for_status()
        return [response.json()[0]['lat'],response.json()[0]['lon']]
    except requests.exceptions.HTTPError as err:
        print(err)
        return err.response.json()

print(json.dumps(get_coordinates('Kingston'),indent=2))

def get_weather(city:str) -> dict:
    coords:list=get_coordinates(city)
    try:
        response:any = requests.get(data_url+"lat="+str(coords[0])+"&lon="+str(coords[1])+"&appid="+api_key)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(err)
        return err.response.json()

print(json.dumps(get_weather('Kingston')['list'],indent=2))



