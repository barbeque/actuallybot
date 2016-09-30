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

token = get_slack_token()

sc = SlackClient(token)
if sc.rtm_connect():
	while True:
		print sc.rtm_read()
		time.sleep(1)
else:
	print "Connection failed, invalid token?"

		
