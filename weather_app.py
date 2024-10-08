import streamlit as st
import requests
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('API_KEY')


def weather_extractor(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] != "404":
        today_sky = data['weather'][0]['main']
        temp_rn = data['main']['temp']
        temp_feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        location = data['name']
        return f"Today the sky will be {today_sky}.\nThe temperature right now is {temp_rn}℃ but it feels like {temp_feels_like}℃.\nThe humidity today is {humidity}%, and the wind speed right now {wind_speed} m/s, in {location}."
    else:
        return "City not found."


st.title('Weather App')
st.write('Enter the city name to get the current weather details.')

city_location = st.text_input('City Name')

if city_location:
    weather_info = weather_extractor(city_location)
    st.write(weather_info)
