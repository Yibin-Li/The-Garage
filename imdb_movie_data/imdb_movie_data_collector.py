import urllib.request, urllib.parse
import bs4
import re
import sqlite3
import socket
import time
import json

conn = sqlite3.connect('C:\\Users\\lyb\\Desktop\\imdb movie rating.sqlite3')
cur = conn.cursor()
# the main table
cur.execute('''
CREATE TABLE IF NOT EXISTS Pages (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 
url TEXT UNIQUE, 
name TEXT, 
genre TEXT,
director TEXT,
contentRating TEXT,
datePublished TEXT,
keywords TEXT,
description TEXT,
averageRating INTEGER,
ratingCount INTEGER,
releasedCountry TEXT,
duration TEXT)''')

# the collection of already parsed url
cur.execute('''
CREATE TABLE IF NOT EXISTS Web (url text UNIQUE, parsed INTERGER)''')
		
		
# check to see if we are already in progress...
cur.execute('''
SELECT url, parsed FROM Web ORDER BY RANDOM()''')
content = cur.fetchall()
if content != []:
	for h in content:
		if h[1] == 0:
			starturl = h[0]
else:
	starturl = input('Please enter the web link:')
	if len(starturl) < 1:
		starturl = 'https://www.imdb.com/title/tt0371746/?ref_=tt_rec_tti'
#print ('Start with', starturl)
		
# set timeout time(in seconds)
# socket.setdefaulttimeout(30)

while True:
	urlTotal = []
	cur.execute('''
	SELECT url, parsed FROM Web ORDER BY RANDOM()''')
	content = cur.fetchall()
	if content != []:
		for h in content:
			if h[1] == 0:
				starturl = h[0]
	
	print ('Retrieving...', starturl)
	cur.execute('''
	INSERT OR IGNORE INTO Web (url, parsed) VALUES (?, 0)''', (starturl, ))
	conn.commit()

	web = urllib.request.urlopen(starturl).read().decode()
	web_content = web.strip()
	parsing_content = bs4.BeautifulSoup(web, "html.parser")

	data = json.loads(parsing_content.find('script', type='application/ld+json').text)
	try:
		name = data["name"]
		print ('Movie name: ', name)
	except:
		name = None
		print ('Movie name: unable to find movie name')
	
	try:
		genre = ', '.join(data["genre"])
	except:
		genre = None
	
	try:
		director = data["director"]["name"]
	except:
		director = None
	
	try:
		contentRating = data["contentRating"]
	except:
		contentRating = None
	
	try:
		datePublished = data["datePublished"][:4]
	except:
		datePublished = None
	
	try:
		keywords = data["keywords"]
	except:
		keywords = None
	
	try:
		description = data["description"]
	except:
		description = None
		
	try:
		aggregateRating = data["aggregateRating"]
		averageRating = aggregateRating["ratingValue"]
		ratingCount = aggregateRating["ratingCount"]
	except:
		averageRating = None
		ratingCount = None
		
	try:
		releasedCountryandDate = re.findall('title="See more release dates" >(.*)', web_content)[0]
		releasedCountry = re.findall('\((.*)\)', releasedCountryandDate)[0]
	except:
		releasedCountry = None
	
	try:
		duration = data["duration"][2:].lower()
	except:
		duration = None
	
	tags = parsing_content('a')
	for tag in tags:
		x = tag.get('href')
		try:
			url = re.findall("^/title/tt[0-9.]+/\?ref_=tt_rec_tti", x)
		except:
			url = None
		if url:
			url = "https://www.imdb.com/" + url[0]
			urlTotal.append(url)

	"""print("name: ", name)
	print("genre: ", genre)
	print("director: ", director)
	print("contentRating: ", contentRating)
	print("datePublished: ", datePublished)
	print("keywords: ", keywords)
	print("description", description)
	print("averageRating: ", averageRating)
	print("ratingCount: ", ratingCount)
	print("releasedCountry: ", releasedCountry)
	print("duration: ", duration)
	"""
	
	cur.execute('''
	INSERT OR IGNORE INTO Pages (url, name, genre, director, contentRating, 
	datePublished, keywords, description, averageRating, ratingCount, releasedCountry,
	duration) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (starturl, name, genre,
	director, contentRating, datePublished, keywords, description, averageRating, 
	ratingCount, releasedCountry, duration))
	cur.execute('''
	UPDATE Web SET parsed = 1 WHERE url = ?''', (starturl, ))
	conn.commit()

	# extract other movies link
	for i in urlTotal:
		cur.execute('''
		INSERT OR IGNORE INTO Web (url, parsed) VALUES (?, 0)''', (i, ))
		conn.commit()
	print ('Done')
	#time.sleep(0.5)
	
cur.close()		
print ('end')
