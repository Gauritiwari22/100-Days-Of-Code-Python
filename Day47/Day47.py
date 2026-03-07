import requests
from bs4 import BeautifulSoup
import smtplib

URL="AMAZON_PRODUCT_URL"

headers={
    "User-Agent": "YOUR USER AGENT",
    "Accept-Language": "en-US,en;q=0.9"
}
response=requests.get(URL, headers=headers)
soup=BeautifulSoup(response.text, "html.parser")
title=soup.find(id="productTitle").getText().strip()
price=soup.find(class_="a-offscreen").getText()

price_without_currency=price.split("₹")[1]
price_float=float(price_without_currency.replace(",", ""))

target_price=20000

if price_float<target_price:
    MY_EMAIL="your_email@gmail.com"
    PASSWORD="your_password"

    message=f"{title} is now {price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}"
        )