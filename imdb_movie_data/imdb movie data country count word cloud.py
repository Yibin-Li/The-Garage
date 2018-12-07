import bs4
import re
import sqlite3

conn = sqlite3.connect('C:\\Users\\lyb\\Desktop\\imdb movie rating.sqlite3')
cur = conn.cursor()
count = 0
total = {}
#new = []
print(cur)
cur.execute('''
SELECT releasedCountry, averageRating FROM Pages  ''')
uuu = cur.fetchall()
for w in uuu:
	# retrieve the rating for this movie
	try:
		num = float(w[1])
	except:
		None
	country = w[0]
	total[country] = total.get(country,0) + 1
cur.close()			

# Find the top 100 country
country = sorted(total, key=total.get, reverse=True)
highest = None
lowest = None
for w in country[:100]:
	if highest is None or highest < total[w] :
		highest = total[w]
	if lowest is None or lowest > total[w] :
		lowest = total[w]
print ('Range of counts:',highest,lowest)

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('C:\\Users\\lyb\\Desktop\\gword.js','w')
fhand.write("gword = [")
first = True
for k in country[:100]:
	if not first : fhand.write( ",\n")
	first = False
	size = total[k]
	size = (size - lowest) / float(highest - lowest)
	size = int((size * bigsize) + smallsize)
	try:
		fhand.write("{text: '"+k+"', size: "+str(size)+"}")
	except:
		pass
fhand.write( "\n];\n")

print ("Output written to gword.js")
print ("Open gword.htm in a browser to view")

print ('done')