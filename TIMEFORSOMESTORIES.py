from mastodon import Mastodon
import json, random, threading, os

min_delay = 600
max_delay = 1800

quotes = []
index = 0
with open('corpus.txt', 'r') as file:
	quotes = file.read().split('\n')

random.shuffle(quotes)

#get login info from secrets.json
secrets = {}
with open('secrets.json', 'r') as f:
	secrets = json.loads(f.read())

mastodon = Mastodon(client_id=secrets["id"], client_secret=secrets["secret"], access_token=secrets["access_token"], api_base_url="https://botsin.space")

def make_post():
	global index
	if index >= len(quotes):
		index = 0
		random.shuffle(quotes)

	quote = quotes[index]
	index += 1
	
	while len(quote) > 500:
		print("skipping {} because it is too long".format(quote))
		if index >= len(quotes):
			index = 0
			random.shuffle(quotes)
		quote = quotes[index]
		index += 1
	
	print("posting {}".format(quote))
	mastodon.status_post(quote, visibility="unlisted")

	threading.Timer(random.randint(min_delay, max_delay), make_post).start()

make_post()
