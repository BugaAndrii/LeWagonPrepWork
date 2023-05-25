import requests


def city_info(data):
    """
    Extracts relevant information from the response and returns a dictionary with city information.

    Args:
        data (list): A list containing the response data.

    Returns:
        dict: A dictionary containing the city name, latitude, and longitude extracted from the response.
    """

    # Create a dictionary with the extracted information
    return {
        "city": data[0]["name"],
        "lat": data[0]["lat"],
        "lon": data[0]["lon"]
    }


if __name__ == "__main__":
    # Testing for city_info function
    response = requests.get("https://weather.lewagon.com/geo/1.0/direct?q=london").json()
    print(city_info(response))
