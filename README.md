# Weather App

This is a simple Streamlit app that provides current weather details for any city using the OpenWeatherMap API.

## Features

- Get current weather conditions for any city
- Displays:
  - Sky condition
  - Temperature
  - Feels like temperature
  - Humidity
  - Wind speed
  - Location

## Installation

To run this app locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```
2. **Create a virtual environment:**
```bash
python -m venv env
```
3. **Activate the virtual environment:**
- On Windows:
```bash 
.\env\Scripts\activate
```
- On macOS and Linux:
```bash
source env/bin/activate
```
4. **Install the dependencies:**
```bash
pip install -r requirements.txt
```
## Usage
1. **Run the Streamlit app:**
```bash
streamlit run app.py
```
2. **Open your browser and go to:**
```bash
http://localhost:8501
```
3. **Enter the city name to get the current weather details.**

## Code Overview
The app consists of a simple Python script `(app.py)` that uses Streamlit for the web interface and requests to fetch weather data from the OpenWeatherMap API.

```python
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

```
## License
This project is licensed under the MIT License.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [OpenWeatherMap](https://openweathermap.org/)