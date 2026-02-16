import requests
from twilio.rest import Client
import os

# ---------------------- CONFIG ---------------------- #
STOCK="TSLA"
COMPANY_NAME="Tesla Inc"

STOCK_API_KEY=os.environ.get("STOCK_API_KEY")
NEWS_API_KEY=os.environ.get("NEWS_API_KEY")

TWILIO_SID=os.environ.get("TWILIO_SID")
TWILIO_AUTH=os.environ.get("TWILIO_AUTH")

FROM_NUMBER=os.environ.get("FROM_NUMBER")
TO_NUMBER=os.environ.get("TO_NUMBER")

# ---------------------- STOCK DATA ---------------------- #
stock_url="https://www.alphavantage.co/query"

stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY,
}

response=requests.get(stock_url, params=stock_params)
response.raise_for_status()
data=response.json()["Time Series (Daily)"]

data_list=list(data.items())

yesterday_close=float(data_list[0][1]["4. close"])
day_before_close=float(data_list[1][1]["4. close"])

difference=yesterday_close - day_before_close
up_down = "🔺" if difference > 0 else "🔻"

percent_change = round(abs(difference) / day_before_close * 100)

# ---------------------- NEWS ---------------------- #
if percent_change>=5:
    news_url="https://newsapi.org/v2/everything"

    news_params={
        "q":COMPANY_NAME,
        "apiKey":NEWS_API_KEY,
    }

    news_response=requests.get(news_url, params=news_params)
    news_response.raise_for_status()

    articles=news_response.json()["articles"][:3]

    formatted_articles=[
        f"{STOCK}: {up_down}{percent_change}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in articles
    ]

    # ---------------------- SMS ---------------------- #
    client=Client(TWILIO_SID, TWILIO_AUTH)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=FROM_NUMBER,
            to=TO_NUMBER,
        )
