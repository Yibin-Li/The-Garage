print ('Please guess a number. The interval is 1-100.')
print ('You have 5 times to guess!')

import random
rand_number=random.randint(1,100)

turn=0

for n in range(5):
    guess_number=eval(input('Your guess number:'))
    if guess_number==rand_number:
        print ('You win!')
        break
    elif guess_number>100 or guess_number<1:
        print ('Plese enter a number in the interval of 1-100!')
        turn+=1
        print ('You have tried',turn,'times.')
        print ('')
    else:
        if turn ==4:
            print ('Sorry, the answer is',rand_number,'. You lost!')
        else:
            print ('Sorry, this is a wrong answer.Please try again!')
            turn+=1
            print ('You have tried',turn,'times.')
            print ('')
