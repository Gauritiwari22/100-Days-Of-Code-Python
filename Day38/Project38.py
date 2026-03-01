# Habit Tracker using Google sheets

# API used - Nutritionix
#          - Sheety


# replacements to be made:
# YOUR_APP_ID
# YOUR_API_KEY
# YOUR_SHEETY_ENDPOINT
# YOUR_SHEETY_TOKEN

import requests
import os
from datetime import datetime

# ------------------ ENVIRONMENT VARIABLES ------------------

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

# ------------------ USER INPUT ------------------

exercise_text = input("Tell me which exercises you did: ")

# ------------------ NUTRITIONIX API ------------------

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutrition_params = {
    "query": exercise_text,
}

response = requests.post(
    url=nutrition_endpoint,
    json=nutrition_params,
    headers=nutrition_headers
)

result = response.json()

# ------------------ DATE & TIME ------------------

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

# ------------------ SHEETY API ------------------

sheet_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for exercise in result["exercises"]:

    sheet_input = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_input,
        headers=sheet_headers
    )

    print(sheet_response.text)