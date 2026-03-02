from twilio.rest import Client
import os

class NotificationManager:

    def send_sms(self, message_body):

        account_sid = os.environ["TWILIO_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=message_body,
            from_=os.environ["TWILIO_NUMBER"],
            to=os.environ["MY_NUMBER"]
        )

        print(message.status)