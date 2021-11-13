import requests
from win10toast import ToastNotifier
import datetime

x = datetime.datetime.now()
TN = ToastNotifier()

params = {
    'lat': 48.5333,
    'lon': 2.6667,
    'lang': 'fr',
    'units': 'metric',
    'appid': "c9d7638ee8c390a01043b02838d8056b"
}

r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params).json()

temp = r["main"]["temp"]
temp_min = r["main"]["temp_min"]
temp_max = r["main"]["temp_max"]

TN.show_toast("Meteo", f"temp: {temp} °C\ntemp_min: {temp_min} °C\ntemp_max: {temp_max} °C", threaded=True, icon_path="./assets/meteo_icon.ico", duration=30)