#!/usr/bin/python
 # -*- coding: utf-8 -*-

import os, json, urllib2, random, sys, getopt, shutil, argparse
from urllib import urlretrieve

class Pyckground():
	"""
		Pyckground allows you to download and set an image from internet as
		your background.
	"""

	default_image_folder_path = './wallpapers'
	config_file_path = './config.json'

	def get_json_from_url(self, url):
		"""
			Get json response from given url and returns it.
		"""

		try:
			print "Connecting to url..."
			json_data = json.load(urllib2.urlopen(url))
			print "data loaded!"
			return json_data
		except:
			print "Can't connect to %s" % url
			return False


	def clean_image_type(self, string):
		"""
			Returns image type from mimetype string.
		"""

		try:
			image_type = string[string.index('/')+1:]
			return image_type
		except:
			return 'unknown'
		

	def get_image_from_url(self, image, 
		destination_path=default_image_folder_path):
		"""
			Get image from given url and writes it to given destination_path.
		"""

		try:
			print "Downloading image from %s ..." % image['link']

			destination_path = '%s/%s.%s' % (
				destination_path, 
				image['id'], 
				self.clean_image_type(image['type']))

			file = urlretrieve(image['link'], destination_path)
			self.save_last_image_path(destination_path)

			print "image successfully downloaded to %s!" % destination_path

			return {'path':file[0]}
		except Exception, e:
			print "Error!: %s" % e
			return False


	def apply_background(self, image_path=default_image_folder_path):
		"""
			Executes host command to apply background.
		"""

		# Thanks to http://unix.stackexchange.com/questions/59653/ \
		# change-desktop-wallpaper-from-terminal
		command = 'gsettings set org.cinnamon.desktop.background picture-uri'
		image_path = 'file://%s' % os.path.abspath(image_path)

		try:
			print "Applying image as wallpaper..."
			os.system('%s "%s"' % (command, image_path))
			print "Success!"
			return True
		except Exception, e:
			print "Error!: %s" % e
			return False


	def save_last_image_path(self, last_image_path):
		"""
			Saves last image path
		"""

		try:
			file = open(self.config_file_path, "w")
			data = {'last_image_path': last_image_path}
			file.write(json.dumps(data))
			file.close()
			return True
		except:
			print "Can't save config file: %s" % self.config_file_path
			return False


	def get_last_image_path(self):
		"""
			Returns last image path.
		"""

		try:
			file = open(self.config_file_path, "r")
			data = file.read()
			file.close()
			json_data = json.loads(data)
			return  json_data['last_image_path']
		except Exception, e:
			print "Can't load config file: %s" % self.config_file_path
			print "Error: %s" % e
			return None


	def copy_current_image(self, destination_path):

		"""
			Copy last used image to given path.
		"""

		if destination_path:

			shutil.copy2(self.get_last_image_path(), destination_path)
		else:
			print "No destination_path given."


	def imgur(self, gallery_id):

		"""
			Connects to imgur gallery api and sets a random image as your 
			wallpaper.
		"""

		api_link = 'https://api.imgur.com/3/gallery/'
		wallpaper_path = './wallpapers/wallpaper.jpg'

		gallery_link = "%s%s" % (api_link, gallery_id)

		json = self.get_json_from_url(gallery_link)

		if json:
			selected_image = random.choice(json['data']['images'])

			image_file = self.get_image_from_url(selected_image)

			self.apply_background(image_file['path'])


def main():

	parser = argparse.ArgumentParser()

	parser.add_argument("-a", "--galleryId", help="allows you to download and \
		set an image from an Imgur  gallery as your background.")

	parser.add_argument("-c", "--copyCurrentImage", help="Copy last used \
		image to given path.")

	args = parser.parse_args()

	pyckground = Pyckground()

	gallery_id = ''
	destination_path = ''

	if args.galleryId:
		gallery_id = args.galleryId
	elif args.copyCurrentImage:
		destination_path = args.copyCurrentImage
		

	if gallery_id:
		pyckground.imgur(gallery_id)
	elif destination_path:
		pyckground.copy_current_image(destination_path)
	else:
		print "Nothing done... don't bother me please."

	sys.exit()


if  __name__ =='__main__':
	main()