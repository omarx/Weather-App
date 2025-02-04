import json
import os
from datetime import date
import requests
from db_operations import *
from dotenv import load_dotenv

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

def get_weather(city:str) -> dict:
    coords:list=get_coordinates(city)
    try:
        print("getting weather data ...")
        response:any = requests.get(data_url+"lat="+str(coords[0])+"&lon="+str(coords[1])+"&appid="+api_key)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(err)
        return err.response.json()



def add_weather(city: str) -> bool:
    lat = str(get_coordinates(city)[0])
    lon = str(get_coordinates(city)[1])
    temp = str(get_weather(city)['main']['temp'])
    feels = str(get_weather(city)['main']['feels_like'])
    wind = str(get_weather(city)['wind']['speed'])
    humidity = str(get_weather(city)['main']['humidity'])
    today = date.today()
    try:
        cursor.execute(
        "INSERT INTO forecast(latitude, longitude, temperature, feels_like, humidity, city, wind_speed, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
        (lat, lon, temp, feels, humidity, city, wind, today))
        conn.commit()
        print("Successfully added weather data for "+city,", the temperature is now "+ temp +" fahrenheit" +" it feels like "+ feels + " with " + humidity +" humidity")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False
    return True



if __name__ == '__main__':
    city = input("Press enter a center to a city for weather forecast: ")
    if add_weather(city):
        print("Successfully added weather data for "+city)
    else:
        print("Weather forecast for "+city+" is unsuccessful")

