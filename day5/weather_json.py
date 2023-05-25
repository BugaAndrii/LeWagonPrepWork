import requests
import datetime


def weather_forecast(data):
    """
    Extracts the weather forecast for tomorrow from the provided data.

    Args:
        data (dict): A dictionary containing the weather forecast data.

    Returns:
        str: The weather forecast for tomorrow in the format "The weather in <city> tomorrow is <forecast>".
    """
    # Get tomorrow's date and time in the required format
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d 06:00:00")

    # Extract the city name from the data
    city = data["city"]["name"]

    # Initialize an empty forecast string
    forecast = ""

    # Iterate over the forecast data to find tomorrow's weather
    for item in data["list"]:
        if item.get("dt_txt") == tomorrow:
            forecast += item["weather"][0]["description"]

    # Return the weather forecast string
    return f"The weather in {city} tomorrow is {forecast}"


if __name__ == "__main__":
    # Testing for weather_forecast function

    # Get the weather forecast data for a specific location
    response = requests.get("https://weather.lewagon.com/data/2.5/forecast?lat=51.5073219&lon=-0.1276474&units=metric").json()

    # Define a sample weather forecast data for San Francisco
    san_francisco = {
        "city": {
            "name": "San Francisco"
        },
        "list": [
            {},
            {
                "weather": [
                    {
                        "id": 802,
                        "main": "Heavy Rain",
                        "description": "heavy rains",
                    }
                ],
                "dt_txt": (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d 06:00:00")
            }
        ]
    }

    # Print the weather forecast for the given data
    print(weather_forecast(response))
    print(weather_forecast(san_francisco))
