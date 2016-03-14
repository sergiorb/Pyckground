# Pyckground
A simple python script to set your linux background from Imgur galleries.

### Usage
```
usage: Pyckground.py [-h] [-a GALLERYID] [-nD] [-c COPYCURRENTIMAGE]

optional arguments:
  -h, --help            show this help message and exit
  -a GALLERYID, --galleryId GALLERYID
                        Allows you to download and set an image from an Imgur
                        gallery as your background.
  -nD, --noDelete       Avoids last image deletion when downloading a new
                        wallpaper.
  -c COPYCURRENTIMAGE, --copyCurrentImage COPYCURRENTIMAGE
                        Copy last used image to given path..

```
Example:
```
Pyckground.py --galleryId dbVN1

Pyckground.py --galleryId dbVN1 --noDelete

Pyckground.py -c /home/user/Pictures/

```
