import praw
import config
import os
import re
#log in
def bot_login():
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "Image_jpg_bot agent")
	return r
#check for images that can be linked
def run(r, comments_replied_to, add_pattern):
	for comment in r.subreddit('test').comments(limit=25):
		if comment.id not in comments_replied_to and comment.author != r.user.me():
			if comment.body in images:
				comment.reply("[" + comment.body + "](" + images[comment.body] + ")")
				comments_replied_to.append(comment.id)
				with open("comments_replied_to.txt", "a") as f:
					f.write(comment.id + "\n")
			#user may want to add a new link
			elif add_pattern.match(comment.body):
				print comment.body
			

#Retrieve the saved comments from the comments_replied_to.txt file
def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
	return comments_replied_to

comments_replied_to = get_saved_comments()
images = {"feelsbadman.jpg" : "http://imgur.com/buEBNnk", "iseewhatyoudidthere.jpg" : "http://imgur.com/9gBzlFv"}
add_pattern = re.compile("add \[[a-z, A-Z, 0-9]+\.jpg\]\(http:\/\/imgur\.com\/[a-z, A-Z, 0-9]+\)")
r = bot_login()
run(r, comments_replied_to, add_pattern)