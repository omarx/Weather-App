import psycopg2

conn= psycopg2.connect(database="weather", user="weather_user", password="weather_pass", host="localhost", port="5432")

cursor = conn.cursor()