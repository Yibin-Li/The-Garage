import urllib.request
import time
import re
u = urllib.request.urlopen('http://www.bing.com/?FORM=HPCNEN&setmkt=en-us&setlang=en-us#').read().decode('gbk', 'ignore')
print (u)
