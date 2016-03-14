#!/usr/bin/python
 # -*- coding: utf-8 -*-

import os
import json
import urllib2
import random
from urllib import urlretrieve
import time
import sys, getopt

album_id = ''
json_data = []
api_link = 'https://api.imgur.com/3/album/'
wallpaper_path = './wallpapers/wallpaper.jpg'

try:
	opts, args = getopt.getopt(sys.argv[1:],"h:a:")
except getopt.GetoptError:

	print 'Pyckground.py -a imgur_albun_id'
	sys.exit(2)

for opt, arg in opts:
	if opt == '-h':
		print 'Pyckground.py -a imgur_albun_id'
		sys.exit()
	elif opt in ("-a"):
		album_id = arg

imgur_album_link = "%s%s" % (api_link, album_id)

try:
	print "Connecting with Imgur api..."
	json_data = json.load(urllib2.urlopen(imgur_album_link))
	print "Album data loaded!"
except:
	print "Can't connect to Imgur¡¡"

if json_data:
	selected_image = random.choice(json_data['data']['images'])

	print "Downloading random image..."
	file = urlretrieve(selected_image['link'], wallpaper_path)
	print "random image successfully downloaded!"


	# Thanks to http://unix.stackexchange.com/questions/59653/change-desktop-wallpaper-from-terminal

	command = 'gsettings set org.cinnamon.desktop.background picture-uri'
	image_url = 'file://%s' % os.path.abspath(file[0])

	print "Applying image as wallpaper..."
	os.system('%s "%s"' % (command, image_url))
	print "Success!"
