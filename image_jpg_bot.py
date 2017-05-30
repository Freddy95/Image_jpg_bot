import praw
import config

def bot_login():
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "Image_jpg_bot agent")
	return r

def run(r):
	for comment in r.subreddit('test').comments(limit=25):
		if "feelsbadman.jpg" in comment.body:
			print comment.body
			comment.reply("[feelsbadman.jpg](http://imgur.com/buEBNnk)")
r = bot_login()
run(r)