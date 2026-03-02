import requests
import os

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

class DataManager:

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT, headers=headers)
        data = response.json()
        return data["prices"]

    def update_destination_codes(self, city_data):
        for city in city_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(
                f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )