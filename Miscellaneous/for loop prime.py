print ('This program serves to test prime numbers.')
a=eval(input('Please enter a test number:'))
total=0
for i in range(1,a):
    if a % i!=0:
        total=total+1
        
if total>=a-2 and a!=1 and a!=0 and a>0:
    print ('This number is a Prime Number')
else:
    print ('This number is Not a Prime Number')

