import urllib.request
import bs4
import re


ini_url=input('url:')
if len(ini_url) < 1:
	ini_url = 'http://python-data.dr-chuck.net/known_by_Rhuaridh.html'

urllist=[]
urllist_new=[]
count=0
html=urllib.request.urlopen(ini_url).read()
soup=bs4.BeautifulSoup(html,'html.parser')

tags = soup('a')

print ('First person knows:')

for tag in tags:
    x=tag.get('href', None)
    
    urllist.append(x)
    print (tag.contents[0])

for x in range(3,len(urllist)):
    urllist.pop(1)

count+=1
for x in range(1,10):
    
    for y in urllist:
        html=urllib.request.urlopen(y).read()
        soup=bs4.BeautifulSoup(html,'html.parser')

        tags = soup('a')

        print ('')
        count+=1
        for tag in tags:
            x=tag.get('href', None)
            urllist_new.append(x)
            print (tag.contents[0])
            
    urllist=urllist_new
    urllist_new=[]
    for a in range(3,len(urllist)):
        urllist.pop(1)
print (count)
#web that could be used: http://python-data.dr-chuck.net/known_by_Rhuaridh.html
