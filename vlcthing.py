import requests,math
from bs4 import BeautifulSoup
import sys
try:
  r = requests.get('http://localhost:8080/requests/status.xml', auth=('', 'aaaa'))
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

print "'{0:02d}:{1:02d}:{2:02d}.{3:03d}'".format(h,m,s,mils)
