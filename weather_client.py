import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"
jokeURL ="https://official-joke-api.appspot.com/random_joke"
# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "338a603e6ab1cb30d3e8f749bc0102a1"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)
def get_joke() -> Dict:
    res = requests.get(jokeURL)
    return res.json()
def main():
    temp = get_weather("London")
    print(temp)
    
    tempJoke = get_joke()
    print(tempJoke)

if __name__ == "__main__":
    main()
