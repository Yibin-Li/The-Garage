from random import randint

board = []
board2 = []

for x in range(0, 5):
    board.append(["O"] * 5) # Set a playboard 
    board2.append(["O"] * 5)
def print_board(board):
    for row in board:
        print (" ".join(row)) # Make the playboard obvious to user

print ("Let's play Battleship!")
print ("O stands for ocean, which is a possible choice to guess the battleship!")
print ("Your batttleship hide in the above board,and enemy's is in the below. Find it!")
print ("")
print_board(board)
print ("")
print_board(board)
print ("")

def random_row(board):
    return randint(1, len(board))
def random_col(board):
    return randint(1, len(board[0])) # Randomly choose the row and column number
def random_row_com(board):
    return randint(1, len(board))
def random_col_com(board):
    return randint(1, len(board[0]
                          )) # Randomly choose the number for computer

ship_row = random_row(board)
ship_col = random_col(board)
ship_row_com = random_row_com(board2)
ship_col_com = random_col_com(board2)

for turn in range(7): # Set loop times
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    guess_row_com=randint(1, len(board))
    guess_col_com=randint(1, len(board[0]))
    print ("")
    print ("")
    
    if guess_row==ship_row and guess_col==ship_col and (ship_row_com != guess_row_com or ship_col_com != guess_col_com):
        # Compare the input numbers to the random numbers
        print ("Congratulations! You sank your enemy's battleship!")
        break

    elif ship_row_com == guess_row_com and ship_col_com == guess_col_com and (guess_row !=ship_row or guess_col != ship_col):
        print ("YOU LOST!Your enemy sank your battleship!")
        print ("You tried",turn+1,"times.")
        break

    else:
        print ("Computer guessing location is",guess_row_com,guess_col_com)
        board2[guess_row_com-1][guess_col_com-1] = "H"                                                
        print_board(board2)
        print ("")

        if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
            print ("Oops, that's not even in the ocean.")
            print ("You have played",turn+1,"times.")
            print ("")
            print_board(board)
            print ("")

            if turn == 6:
                print ("Game Over")
                print ("")
                print ("The position of the battleship is",ship_row,ship_col)

                board_user = [] # Show the position of enemy's battleship 
                for x in range(0, 5):
                    board_user.append(["O"] * 5)
                board_user[ship_row-1][ship_col-1]="S"
                print_board(board_user)
                
        elif(board[guess_row-1][guess_col-1] == "X"):
            print ("You guessed that one already.")
            print ("You have played",turn+1,"times.")
            print ("")
            print_board(board)
            print ("")

            if turn == 6:
                print ("Game Over")
                print ("")
                print ("The position of enemy's battleship is",ship_row,ship_col)

                board_user = [] # Show the position of enemy's battleship
                for x in range(0, 5):
                    board_user.append(["O"] * 5)
                board_user[ship_row-1][ship_col-1]="S"
                print_board(board_user)

        else:
            print ("You missed your enemy's battleship!")
            board[guess_row-1][guess_col-1] = "X"
            print ("You have played",turn+1,"times.")
            print ("")
            print_board(board)
            print ("")

            if turn == 6:
                print ("Game Over")
                print ("")
                print ("The position of the enemy's battleship is",ship_row,ship_col)
            
                board_user = [] # Show the position of enemy's battleship 
                for x in range(0, 5):
                    board_user.append(["O"] * 5)
                board_user[ship_row-1][ship_col-1]="S"
                print_board(board_user)
