import requests
# x = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
# print(x.text)
# 2hpGGeFAgu98IGucPXoLX4dAA0VMZuMm

api_key="2hpGGeFAgu98IGucPXoLX4dAA0VMZuMm"
City = input("Enter your City name:")
url = f"http://dataservice.accuweather.com/locations/v1/cities/search?q={City}&apikey={api_key}"

def fetchLocaltionkey():
    location_url = url
    response = requests.get(location_url)
    data = response.json()
    if response.status_code == 200 and data:
        location_key = data[0]['Key']
        return location_key
    else:
        print("Error fetching the location key")

location_key = fetchLocaltionkey()

weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}"

response = requests.get(weather_url)


if response.status_code == 200:
    weather_data = response.json()
    if weather_data:
        temperature = weather_data[0]['Temperature']['Metric']['Value']
        unit = weather_data[0]['Temperature']['Metric']['Value']
        description = weather_data[0]['WeatherText']

        print(f"The current weather in {City}: {description}, {temperature} degree {unit} ")
    else:
        print("No weather data formed")
else:
    print(f"Failed to fetch weather data. {response.status_code}")