# Thanks to http://unix.stackexchange.com/questions/59653/change-desktop-wallpaper-from-terminal

import os
import json
import urllib2
import random
from urllib import urlretrieve
import time

imgur_album_link = "https://api.imgur.com/3/album/dbVN1"

json_data = json.load(urllib2.urlopen(imgur_album_link))

#print json_data['data']['images']

images = json_data['data']['images']

selected_image = random.choice(images)

file = urlretrieve(selected_image['link'], './wallpapers/wallpaper.jpg')

command = 'gsettings set org.cinnamon.desktop.background picture-uri'
image_url = 'file://%s' % os.path.abspath(file[0])

os.system('%s "%s"' % (command, image_url))