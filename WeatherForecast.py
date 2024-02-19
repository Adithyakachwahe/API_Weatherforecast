import requests

# Replace 'YOUR_API_KEY' with the actual API key you obtained from OpenWeatherMap
api_key = '80fce6db787db1de202821fc6772e2cd'
city = 'Bangalore'  # Replace with the desired city

# API endpoint URL for current weather
current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# http://api.openweathermap.org/data/2.5/weather?q={Bangalore}&appid={80fce6db787db1de202821fc6772e2cd}

# Make a GET request to the current weather API endpoint
response = requests.get(current_weather_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data from the response
    current_weather_data = response.json()
    # print(current_weather_data)
    # Print current weather information
    print("Current Weather in", city)
    print("Temperature:", current_weather_data['main']['temp'], "K")
    print("Description:", current_weather_data['weather'][0]['description'])
    print("Humidity:", current_weather_data['main']['humidity'])
else:
    print(f"Error: {response.status_code}")


