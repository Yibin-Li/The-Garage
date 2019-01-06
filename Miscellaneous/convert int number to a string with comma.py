u =986437009961
count0 = len(str(u))
count1 = 0
remain = count0 % 3
print (remain)
new = []
count = 0
for x in str(u):
	new.append(x)
	count1 += 1
	count += 1
	if count1 == remain:
		new.append(',')
		count = 0
	if count == 3 and count1 != remain:
		new.append(',')
		count = 0
if new[-1] == ',':
	del(new[-1])
print (new)
s = ''
y = s.join(new)
print (y)