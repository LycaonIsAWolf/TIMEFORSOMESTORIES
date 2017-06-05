from mastodon import Mastodon
import json, random, threading, os

min_delay = 600
max_delay = 1800

quotes = []
with open('corpus.txt', 'r') as file:
	quotes = file.read().split('\n')

#get login info from secrets.json
secrets = {}
with open('secrets.json', 'r') as f:
	secrets = json.loads(f.read())

mastodon = Mastodon(client_id=secrets["id"], client_secret=secrets["secret"], access_token=secrets["access_token"], api_base_url="https://botsin.space")

mastodon = Mastodon(client_id=secrets["id"], client_secret=secrets["secret"], access_token=secrets["access_token"], api_base_url="https://botsin.space")


def make_post():
	quote = random.choice(quotes)
	
	while len(quote) > 500:
		quote = random.choice(quotes)
	
	print("posting {}".format(quote))
	mastodon.status_post(quote, visibility="unlisted")

	threading.Timer(random.randint(min_delay, max_delay), make_post).start()

make_post()
