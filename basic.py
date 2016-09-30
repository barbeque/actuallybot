import time, os, sys
from slackclient import SlackClient

# TODO: put in another module
def get_slack_token():
	key = "SLACK_TOKEN"
	if not key in os.environ:
		sys.stderr.write("Could not find " + key + " environment variable.\n")
		sys.exit(1)
	else:
		return os.environ[key]

def get_response_for_message(message_text):
	message_text = message_text.lower()
	if "google apps" in message_text:
		return "I think you mean G Spot."
	return None

token = get_slack_token()
print "Got token"

sc = SlackClient(token)
if sc.rtm_connect():
	print "Slackbot is alive!"
	while True:
		new_events = sc.rtm_read()
		for event in filter(lambda e: "type" in e, new_events):
			if event["type"] == "message" and "text" in event:
				message_text = event["text"]
				response = get_response_for_message(message_text)
				if response is not None:
					# Correct them!
					sc.rtm_send_message(event["channel"], response)
		time.sleep(3)
else:
	print "Connection failed, invalid token?"

		
