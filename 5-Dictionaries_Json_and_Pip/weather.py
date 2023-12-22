import requests

city = 'London'

url = 'http://api.weatherapi.com/v1/current.json?key=b9f847486cfd4ff3a3c00845232212&q='+city+'&aqi=no'

response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_c')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, "is", description, "and the temperature is", temp, "degrees.")
