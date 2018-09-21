import urllib.request
import re
total1 = []
total2 = []
count = 0
def graburl(url):
	e = urllib.request.urlopen(url).read()
	txt = e.decode()
	t = re.findall('href="(http://.+?)"', txt)
	for x in t:
		if len(x) >= 0:
			total1.append(x)
			
graburl('http://tieba.baidu.com/p/2693305981') #level 0 url 

total2 = total1 + [] #level 1 url
print (len(total2))

for w in range(2):   #run scraping for how many times 
	for w in total2:
		try:
			graburl(w) 
		except:
			continue
		count += 1
		print (count)

	count = 0
	total2 = total1 + [] #level 2 url
	print (len(total2))

