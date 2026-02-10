import os
import requests
from twilio.rest import Client

# Keys from environment
OWM_API_KEY = "e37ddf831957534369a6e11965bda7b2"
ACCOUNT_SID=os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN=os.environ.get("TWILIO_AUTH_TOKEN")

# Weather request
weather_params ={
    "lat":28.6,
    "lon":77.2,
    "appid":OWM_API_KEY,
    "cnt":4,
}

response=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=weather_params)
response.raise_for_status()
data=response.json()

# Check rain condition
will_rain=False
for hour_data in data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True

# Send SMS
if will_rain:
    client=Client(ACCOUNT_SID, AUTH_TOKEN)
    message=client.messages.create(
        body="Bring an umbrella ",
        from_="+123456789",
        to="+987654321"
    )
    print(message.status)
