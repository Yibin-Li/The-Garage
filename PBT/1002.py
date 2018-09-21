a = input('')
sum = 0
def pingying(x):
	if x == 1:
		print ('yi', end = ' ')
	elif x == 2:
		print ('er', end = ' ')
	elif x == 3:
		print ('san', end = ' ')
	elif x == 4:
		print ('si', end = ' ')
	elif x == 5:
		print ('wu', end = ' ')
	elif x == 6:
		print ('liu', end = ' ')
	elif x == 7:
		print ('qi', end = ' ')
	elif x == 8:
		print ('ba', end = ' ')
	elif x == 9:
		print ('jiu', end = ' ')
	elif x == 0:
		print ('ling', end = ' ')
	else:
		print ("No", end = ' ')


for w in a:
	sum = sum + int(w)
total = str(sum)
for k in total:
	pingying(int(k))