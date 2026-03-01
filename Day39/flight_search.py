import requests
import os

TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]

headers = {
    "apikey": TEQUILA_API_KEY
}

class FlightSearch:

    def get_destination_code(self, city_name):
        endpoint = "https://api.tequila.kiwi.com/locations/query"
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(endpoint, headers=headers, params=params)
        data = response.json()
        return data["locations"][0]["code"]