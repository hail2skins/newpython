import requests

url = 'http://api.weatherapi.com/v1/current.json?key=1efcda17022b47cba8b160500242103&q=55126&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather is: " + description + " with a temperature of " + str(temp) + " degrees Fahrenheit.")
print(temp)
print(weather_json)