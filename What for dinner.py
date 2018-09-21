import random
a = 2
total = []
dinner = {1:'肯德基', 2:'手工面', 3:'炒饼', 4:'兰州拉面', 5:'滋烩', 6:'食堂',
          7:'周淑真', 8:'羊肉粉'}
while a == 2:
    if len(total) == len(dinner):
        print ('No other choices.')
        break

    else:
        b = random.randint(1, len(dinner))
        while b in total:
            b = random.randint(1, len(dinner))
        total.append(b)
        print (dinner[b])
        print ('Do you satisfy with the option?')
        print ('1:Yes 2:No')
        print ('Press the enter to confirm.')
        a = int(input())
        print ('')
        
