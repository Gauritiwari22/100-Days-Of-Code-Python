import smtplib
import datetime as dt
import random
import csv

MY_EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"

# Get today's date
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Read birthday data
with open("Day33/birthday.csv") as file:
    data = csv.DictReader(file)
    birthdays = list(data)

for person in birthdays:
    birthday = (int(person["month"]), int(person["day"]))

    if birthday == today_tuple:

        messages = [
            f"Happy Birthday {person['name']}! 🎉 Have a great year ahead!",
            f"Wishing you a fantastic birthday {person['name']}!",
            f"Many many happy returns of the day {person['name']}!"
        ]

        message = random.choice(messages)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday!\n\n{message}"
            )

print("Done")
