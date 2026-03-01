import requests
import os
from datetime import datetime, timedelta
from flight_data import FlightData

TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]

headers = {
    "apikey": TEQUILA_API_KEY
}

class FlightSearch:

    def get_flight(self, destination_code):

        endpoint = "https://api.tequila.kiwi.com/v2/search"

        tomorrow = datetime.now() + timedelta(days=1)
        six_months = datetime.now() + timedelta(days=180)

        params = {
            "fly_from": "DEL",  # change to your origin
            "fly_to": destination_code,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y"),
            "curr": "INR",
            "limit": 1,
            "sort": "price"
        }

        response = requests.get(endpoint, headers=headers, params=params)
        data = response.json()

        try:
            flight = data["data"][0]
        except IndexError:
            return None

        return FlightData(
            price=flight["price"],
            origin_city=flight["route"][0]["cityFrom"],
            origin_airport=flight["route"][0]["flyFrom"],
            destination_city=flight["route"][0]["cityTo"],
            destination_airport=flight["route"][0]["flyTo"],
            out_date=flight["route"][0]["local_departure"].split("T")[0],
            return_date=flight["route"][1]["local_departure"].split("T")[0],
        )