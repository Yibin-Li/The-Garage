total = []

for w in range(1,100):
	d = w
	times = 0
	u = 100
	l = 0
	x = 50
	while True:
		if x < d:
			l = x
			x = x+int((u-x)/2)
			times = times + 1
		if x > d:
			u = x
			x = x-int((x-l)/2)
			times = times + 1
		if x == d:
			times = times + 1
			break
	total.append(times)

s = max(total)
print (s)
