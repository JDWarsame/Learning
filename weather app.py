import requests

api_key = '8391eb2be63d8121004e6a490dc38769'

user_input = input('Enter City: ')

weather_data = requests.get(
     f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
   
    weather = weather_data.json()['weather'][0]['main']
    weathertype = weather_data.json()['weather'][0]['description']
    temp = round(weather_data.json()['main']['temp'])

    print(user_input)
    print(f"The weather in {user_input} is: {weather}, type: {weathertype}")
    print(f"The temperature in {user_input} is: {temp}°C")



