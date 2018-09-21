num = int(input(""))
count = 0
while num != 1:
	if num%2== 0:
		num = num / 2
		count = count + 1
		continue
	if num%2 ==1:
		num = (3*num + 1)/2
		count = count + 1
		continue
print (count)