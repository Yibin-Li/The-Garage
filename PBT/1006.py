num = int(input(''))
times = 0
total = []

for e in range(0,3):
	digit = num % 10
	num = int(num / 10)
	total.append(digit)

for t in range(0, total[2]):
	print ('B', end = '')

for w in range(0, total[1]):
	print ('S', end = '')

for w in range (0, total[0]):
	times = times + 1
	print (times, end = '')	