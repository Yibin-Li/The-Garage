import urllib.request
import re
import bs4
 
total1 = []
total2 = []
count = 0
		
content = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm').read().decode()
parsing_content = bs4.BeautifulSoup(content, "html.parser")
a = parsing_content.a
b1 = parsing_content.p
b2 = parsing_content.p.text # To extract 'p' tag text
c = parsing_content.html
d = parsing_content.head
tags = w('a')
print (a)
print ()
print (b1)
print ()
print (b2)
print ()
print (c)
print ()
print (d)
print('')
print ('the page is',w)
print ()
print (tags)
print ()
for tag in tags:
	x = tag.get('href')
	print (x)





