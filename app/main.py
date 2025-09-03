import os
import requests

def get_weather() -> None:
    api_key = os.getenv('API_KEY')
    FILTER = 'Paris'
    print(f"API key: {api_key}")
    if not api_key:
        print('API key not found!')
    else:
        url = 'http://api.weatherapi.com/v1/current.json'
        result = requests.get(url + f"?key={api_key}&" + f"q={FILTER}")

        if result.status_code == 200:
            data = result.json()
            city = data["location"]["name"]
            country = data["location"]["country"]
            day_time = data["location"]["localtime"]
            temperatura = data["current"]["temp_c"]
            type_weather = data["current"]["condition"]["text"]
            print(f"{city}/{country} {day_time} "
                  f"Weather: {temperatura} {type_weather}")
        else:
            print("Error: invalid request")


if __name__ == "__main__":
    get_weather()
