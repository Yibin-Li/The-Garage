import urllib.request, urllib.parse
import sqlite3
import socket
import re

conn = sqlite3.connect('gmane_content.sqlite3')
cur = conn.cursor()
# the main table
cur.execute('''
CREATE TABLE IF NOT EXISTS Messages (id INTEGER UNIQUE, url TEXT UNIQUE, email TEXT, sent_at TEXT, subject TEXT, headers TEXT, body TEXT)''')

baseurl = "http://mbox.dr-chuck.net/sakai.devel/"

# check to see if we are already in progress...
cur.execute('''
SELECT max(id) FROM Messages ''')
content = cur.fetchone()
if content[0] is None:
	start = 0
else:
	start = content[0]
	
# set timeout time(in seconds)
socket.setdefaulttimeout(10)

while True:
	start += 1
	url = baseurl + str(start) + '/' + str(start+1)
	print (url)
	try:
		document = urllib.request.urlopen(url)
		text = document.read().decode()
		pos = text.find('\n\n')

		if pos > 0 : 
			hdr = text[:pos]
			body = text[pos+2:]
		else:
			print (text)
			print ("Could not find break between headers and body")

		#print ('hdr', hdr)
		#print ('===========')
		#print ('body', body)
		#print ('===========')
		x = re.findall('From: .* <(\S+@\S+)>', hdr)
		email = x[0]
		#print ('email: ', email)
		#print ('===========')
		y = re.findall('Date: .*, (.*)', hdr)
		sent_at = y[0]
		#print ('sent at: ', sent_at)
		#print ('===========')
		z = re.findall('Subject: (.*)', hdr)
		subject = z[0]
		#print ('Subject: ', subject)
			
		cur.execute('''
		INSERT OR IGNORE INTO Messages (id, url, email, sent_at, subject, headers, body) 
		VALUES ( ?, ?, ?, ?, ?, ?, ?)''', (start, url, email, sent_at, subject, hdr, body))
		conn.commit()
		print ('inserted')
		print ()
	except:
		print ('open unsuccessfully')
		print ()

cur.close()
