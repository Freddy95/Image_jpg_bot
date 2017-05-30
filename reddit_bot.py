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
		if "skip" in comment.body:
			print comment.body
r = bot_login()
run(r)