import urllib.request, urllib.parse
import bs4
import sqlite3
import time
import os
import socket

conn = sqlite3.connect('spider.sqlite3')
cur = conn.cursor()
# the main table
cur.execute('''
CREATE TABLE IF NOT EXISTS Pages 
(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, url TEXT UNIQUE, html TEXT, error INTEGER, old_rank REAL, new_rank REAL)''')
# the junction table
cur.execute('''
CREATE TABLE IF NOT EXISTS Links (from_id INTEGER, to_id INTEGER)
''')
# the collection of already parsed url
cur.execute('''
CREATE TABLE IF NOT EXISTS Web (url TEXT UNIQUE, parsed INTEGER)
''')
# the collection of unsuccessfull opend page
cur.execute('''
CREATE TABLE IF NOT EXISTS failed_Page (url TEXT UNIQUE)
''')

# Check to see if we are already in progress...
cur.execute('''
SELECT url, parsed FROM Web ORDER BY RANDOM() 
''')
content = cur.fetchall()
if content != []:
	print ('Restarting existing crawl...')
	print ('If you want to start a new crawl, please exit and delete spider.sqlite3')
	for h in content:
		if h[1] == 0:
			starturl = h[0]
			break
	print ('starturl=', starturl)
else:
	starturl = input('please enter the first url:').rstrip('/')
	if len(starturl) < 1:
		starturl = 'http://python-data.dr-chuck.net/'
	print ('starturl =', starturl)	

time.sleep(3)
print ()

cur.execute('''
INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES (?, Null, 1.0)''', (starturl, ))
cur.execute('''
INSERT OR IGNORE INTO Web (url, parsed) VALUES (?, 0)''', (starturl, ))
# 0 stands for we have NOT parsed this web, 1 stands for we have parsed this web
conn.commit()

url_total1 = []
url_total2 = [] # store next level(next round) url
url_total3 = []
url_loop = starturl

# set timeout time(in seconds)
socket.setdefaulttimeout(30)

def urlrank(input_url):
	count = 0
	
	#check to see if we have parsed this url 
	cur.execute('''
	SELECT parsed FROM web WHERE url=?''', (input_url, ))
	uuu = cur.fetchone()
	check = uuu[0]
	if int(check) == 1:
		print ('Page has already retrived')
		
	if int(check) == 0:
		cur.execute('''
		UPDATE Web SET parsed = 1 WHERE url = ?''', (input_url, ))
		cur.execute('''
		SELECT id FROM Pages WHERE url=?''', (input_url, ))
		row = cur.fetchone()
		fromid = row[0]
		print (input_url, 'from id:', fromid)
		conn.commit()
		print ()
		
		try:
			kkk = urllib.request.urlopen(input_url).read().decode()
			w = bs4.BeautifulSoup(kkk, "html.parser")
			tags = w('a')
			for tag in tags:
				q = tag.get('href', None)
				up = urllib.parse.urlparse(q) # for detail please view python document: urllib.parse.urlparse
				if ( len(up.scheme) < 1 ) :
					q = urllib.parse.urljoin(input_url, q)
				v = q.rstrip('/')
				print (v)
				cur.execute('''
				INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES (?, Null, 1.0)''', (v, ))
				if ( v.endswith('.png') or v.endswith('.jpg') or v.endswith('.gif') or v.endswith('.mp4') or v.endswith('.mp3')): 
					print ('Download available')
				else:	
					try:
						t = urllib.request.urlopen(v).read()
						print ('open url successfully')
						if v != input_url.strip('/'):
							if v not in url_total3:
								url_total3.append(v)
							count += 1
							cur.execute('''
							INSERT OR IGNORE INTO Web (url, parsed) VALUES (?, 0)''', (v, ))
							cur.execute('''
							SELECT id FROM Pages WHERE url=?''', (v, ))
							row2 = cur.fetchone()
							toid = row2[0]
							cur.execute('''INSERT OR IGNORE INTO Links (from_id, to_id) VALUES ( ?, ? )''', ( fromid, toid ) )
							print ('insert url successfully')
							print ('to id:', toid)
							print ()
							conn.commit()
					except:
						print ('open page unsuccessfully')
						print ()
						cur.execute('''
						INSERT OR IGNORE INTO failed_Page (url) VALUES (?)''', (v, ))
						cur.execute('''UPDATE Pages SET error=-1 WHERE url=?''', (v, ) )
						conn.commit()
			
			print (count, 'links available')
		except:
			print ('Unable to retrive page')
	
urlrank(url_loop)
print ('==========')
print ('==========')
print ('==========')
for w in url_total3:
	url_total1.append(w)
	url_total2.append(w)

while True:
	if url_total2 != []:
		for i in url_total2:
			web = i.rstrip('/')
			print ('Processing', web)
			print ()
			cur.execute('''
			INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES (?, Null, 1.0)''', (web, ))
			count =0
			urlrank(web)
			print ('===')
			print ()

		print (url_total3)
		url_total2 = url_total3
		for w in url_total3:
			url_total1.append(w)
		print (url_total2)
		print ()
		url_total3 = []

		conn.commit()
	if url_total2 == []:
		break

cur.close()
os.system(r'python C:\Users\hp-pc\Desktop\pagerank.py')