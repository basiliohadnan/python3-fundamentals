import requests

url = 'http://api.weatherapi.com/v1/current.json?key=b9f847486cfd4ff3a3c00845232212&q=São Paulo&aqi=no'

response = requests.get(url)
weather_json = response.json()

print(weather_json)
