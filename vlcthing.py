#!/usr/bin/python
import subprocess
import requests,math
from bs4 import BeautifulSoup
import sys,re,time

border = 5
top_menu = 19
bottom_menu = 48

try:
  r = requests.get('http://localhost:9999/requests/status.xml', auth=('', 'aaaa'))
  soup = BeautifulSoup(r.text)
  length = float(soup.length.string)
  percent = float(soup.position.string)
  position = length*percent
except:
  sys.exit(1)

m, s = divmod(position, 60)
h, m = divmod(m, 60)

mils = s
(h,m,s) = (int(math.floor(h)), int(math.floor(m)), int(math.floor(s)))
mils = int(math.floor((mils - s) * 1000))

timecode = "'{0:02d}:{1:02d}:{2:02d}.{3:03d}'".format(h,m,s,mils)

child = subprocess.Popen("xdotool getmouselocation --shell", shell=True, stdout=subprocess.PIPE)
exec(child.stdout.read())
mousex = X
mousey = Y


child = subprocess.Popen("xdotool search --class vlc getwindowgeometry --shell", shell=True, stdout=subprocess.PIPE)
exec(child.stdout.read())
vlcx = X
vlcy = Y
vlcw = WIDTH
vlch = HEIGHT

child = subprocess.Popen("zenity --entry --text 'Zoom' --entry-text='100'", shell=True, stdout=subprocess.PIPE)
zoom = float(child.stdout.read()) * 0.01


left = vlcx + border
top = vlcy + border + top_menu

right = left + vlcw - 1
bottom = top + vlch - border - bottom_menu - top_menu

#subprocess.Popen("xdotool mousemove {0} {1}".format(left,top), shell=True, stdout=subprocess.PIPE)
#time.sleep(1)
#subprocess.Popen("xdotool mousemove {0} {1}".format(right,bottom), shell=True, stdout=subprocess.PIPE)
xp = round(float(mousex - left)/float(right-left),2)
yp = round(float(mousey - top)/float(bottom-top),2)
print "{0} {1} {2} {3}".format(zoom,xp,yp,timecode)

