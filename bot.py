import time, os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv

load_dotenv()		# load the credentials
 
# Twillo has issues when it's behind a proxy, this addresses the issue.
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

# Get credentials
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
client = Client(account_sid, auth_token, http_client=proxy_client)

today = time.strftime("%m-%d")

def check_bday():
	"""
	A function to check if today is someone's birthday.
	It reads in data from a txt file of the format 04-21 John Doe
	It sends a message to the user.
	"""
	filename = open("file1.txt", "r")
	count = 0

	for line in filename:
		if today in line:		# There is a birthday
			count = 1 	
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