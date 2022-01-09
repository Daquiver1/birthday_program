# Download the helper library from https://www.twilio.com/docs/python/install
#time library to check day and month of today
import time
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv
load_dotenv()

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
client = Client(account_sid, auth_token, http_client=proxy_client)
today = time.strftime("%m-%d")

def check_bday():
	filename = open("file1.txt", "r")
	count = 0

	for line in filename:
		if today in line:
			count = 1 	# There is a birthday
			message = client.messages.create(
			                     body=f"Today is the birthday of {line[5:]}",
			                     from_=os.getenv("twilio_num"),
			                     to=os.getenv("my_num"))
			print(message.sid)
	if count == 0:
		no_birthday = client.messages.create(
			body="There is no birthday today!",
			from_=os.getenv("twilio_num"),
			to=os.getenv("my_num"))
		print(no_birthday.sid)

if __name__ == "__main__":
	check_bday()
