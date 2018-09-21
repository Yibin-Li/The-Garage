print ('This program can calculate the factorial of a number.')
def factorial(n):
    turn = 1
    while n > 1:
        turn = turn*n
        n -= 1
    else:
        print (turn)

factorial(eval(input('Please enter a number:')))
