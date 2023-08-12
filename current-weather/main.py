import requests
import json

API_KEY = ":)"


def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273.15
    return celcius


city_name = input("Enter city name: ").title()

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}").json()

with open("weather-data.json", "w") as data:
    data.write(json.dumps(response, indent=4))


temp_kelvin = response["main"]["temp"]
feels_like = response["main"]["feels_like"]
weather = response["weather"][0]["description"].title()
temp_celcius = round(kelvin_to_celcius(temp_kelvin))
celcius_feels_like = round(feels_like - 273.15)
print(weather)
print(f"Temperature today is: {temp_celcius}")
print(f"What temperature you are feeling: {celcius_feels_like}")
