import urllib.request
ddd= urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
txt=ddd.read()
mys=txt.decode()
print (mys)

