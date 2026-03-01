from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

for destination in sheet_data:

    flight = flight_search.get_flight(destination["iataCode"])

    if flight and flight.price < destination["lowestPrice"]:

        message = f"""
Low price alert!
Only ₹{flight.price} to fly from {flight.origin_city}-{flight.origin_airport}
to {flight.destination_city}-{flight.destination_airport}
from {flight.out_date} to {flight.return_date}.
"""

        notification_manager.send_sms(message)