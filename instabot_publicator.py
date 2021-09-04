#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

'''
my JSON config struct by default:
{\n
"username":"my_insta_name",\n
"password":"my_insta_pass",\n
"dir":"photo_for_publications"\n
"timeout":"10"\n
}
'''

'''
when bot see that in dir photo_for_publications you put a new photo.jpg,
he publicate it on your insta page
and replase that photo to folder photo_for_publications/publicated/
wait timeout and see in photo_for_publications again
'''

import os
from instabot import Bot
import instabot
from time import sleep
import json

if not os.path.exists("config.json"):
	os.mknode("config.json")


with open("config.json", "r", encoding="utf-8") as f:
	config = json.load(f)

dir = config["dir"]
timeout = config["timeout"] * 60

if not os.path.exists(dir): 
	os.mkdir(dir)
	os.mkdir("{}/publicated".format(dir))
	print("{}/publicated".format(dir))

bot = Bot()
bot.login(username = config["username"], password = config["password"])
photos = os.listdir(dir)

def publication(photo):
	bot.upload_photo(photo, caption = "")

while True:
	for pub_file in os.listdir(dir):
		#if os.path.isfile(pub_file): contunue
		if "jpg" or "JPG" in pub_file and not "REMOVE_ME" in pub_file and os.path.isfile(pub_file):
			publication("{}/{}".format(dir, pub_file))
			print("Publication: {}".format(pub_file))
			sleep(timeout)
			try:
				os.replace("{}/{}.REMOVE_ME".format(dir, pub_file), "{}/{}/{}".format(dir,"publicated", pub_file))
			except: continue
			sleep(timeout)
