import time
i=2

print ('This program can help you determine the prime number.' )
time.sleep(1)
number=eval(input('Please enter a number:'))

if number==0 or number==1 or number<0:
    print ('This number is NOT a prime number.')
else:
    while i< number:
        if number%i!=0:
            i=i+1
        else:
            print ('This number is NOT a prime number.')
            break
    else:
        print ('This number is a prime number.')
