total = []
def add_num(w):
	if w not in total:
		total.append(w)

for x in range(1,100):
	num = x
	while num != 1:
		if num%2== 0:
			num = num / 2
			add_num(int(num))
			continue
		if num%2 ==1:
			num = (3*num + 1)/2
			add_num(int(num))
			continue
total.sort()
print (total)