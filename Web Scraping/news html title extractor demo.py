import bs4
import re

"""Find all titiles in this news html file. The title are contained in 
<h2> or <h3> tag.There are total 20 titles."""

file = open("/news.html", encoding='utf-8').read()
content = bs4.BeautifulSoup(file, "html.parser")
k = content.findAll("div", class_="title") # Find all div section
for i in k:
	div_cleaned = str(i).strip('<div class="title">').strip()
	#print(i)
	more_cleaned = re.findall('>(.+\s.+)</', div_cleaned)
	cleaned = more_cleaned[0].replace("\n", "").replace("</h3>", "").replace("</h2>", "").replace("<h3>", "").replace("<h2>", "")
	not_with_p = re.findall("(.+)<p>", cleaned)
	if (not_with_p != []):
		cleaned = not_with_p[0]
	print(cleaned)
	#print(not_with_p)
	print()