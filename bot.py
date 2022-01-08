# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Yo Christian, this is a test2.",
                     from_=os.getenv("twilio_num"),
                     to=os.getenv("my_num")
                 )

print(message.sid)
