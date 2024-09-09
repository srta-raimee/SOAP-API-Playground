import requests

key = "cd4e7a7af23d4bffb44222108240909"

city_name = input("Digite o nome da cidade que deseja saber a temperatura: ")

current_weather = requests.get(f"http://api.weatherapi.com/v1/current.json?key={key}&q={city_name}&lang=pt").json()

print(f"Temperatura atual em {city_name}, {current_weather['location']['region']}, {current_weather['location']['country']}: {current_weather['current']['temp_c']}ºC")