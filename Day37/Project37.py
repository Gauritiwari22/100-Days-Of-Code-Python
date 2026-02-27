import requests
from datetime import datetime

USERNAME = "your_username"
TOKEN = "your_token"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# ----------------- CREATE USER -----------------
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ----------------- CREATE GRAPH -----------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ----------------- ADD PIXEL -----------------
today = datetime.now()
date = today.strftime("%Y%m%d")

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": date,
    "quantity": "2.5"
}

response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)