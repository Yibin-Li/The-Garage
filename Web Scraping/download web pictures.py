import urllib.request
img = urllib.request.urlopen('http://www.py4inf.com/cover.jpg').read()
ttt = open('new.jpg', 'wb')
ttt.write(img)
ttt.close()


