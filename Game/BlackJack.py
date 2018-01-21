import re 
from random import randint
from a_deck import deck_without_joker

#Initiate all global variables
deck = deck_without_joker
player_total_card = []
computer_total_card = []

#################
# Card Function #
#################
def regular_card():
	"""Return a new random card.
	
	Using random index to find an item in the deck 
	list, delete it, and return its numerical value only.
	"""
	global deck
	index = randint(0, len(deck)-1) 
	card = deck[index]
	string = re.findall('(.*) of', card)[0]
	if string in ['Jack', 'Queen', 'King']:
		number = 10
	elif string == 'Ace':
		number = 1
	else:
		number = int(string)
	
	#delete this card in deck list
	deck = deck[:index] + deck[index+1:]
	return number

def regular_card_without_ace():
	"""Return a new random card with ace."""
	new_card = randint(1, 10)
	return new_card

def user_defined_card():
	"""Player defined card."""
	return 11
	
def make_test_card():
	"""Test purpose card.
	>>> card = make_test_card()
	>>> card()
	11
	>>> card()
	10
	>>> card()
	11
	"""
	k = [11, 10]
	index = len(k) - 1
	def c():
		nonlocal index
		index = (index + 1) % len(k)
		return k[index]
	return c

#####################
# Ace Card Function #
#####################
def eleven_or_one(new_card, card_list):
	"""Return 11 if total card plus 11 is less or equal to 21, 
	1 if the sum is greater than 21. Return new card if it is not A.
	
	>>> eleven_or_one(10, 20)
	10
	>>> eleven_or_one(1, 20)
	1
	>>> eleven_or_one(1, 10)
	11
	"""
	if new_card == 1:
		if sum(card_list) + 11 > 21:
			return 1
		else:
			return 11
	else:
		return new_card

def change_eleven_to_one(card_list):
	"""Input a card list with 11, return adjusted (substitute 11 with 1) 
	list and total point.
	
	>>> card, result = change_eleven_to_one([1, 3, 11])
	>>> card
	[1, 3, 1]
	>>> result
	5
	>>> card, result = change_eleven_to_one([1, 3, 10])
	>>> card
	[1, 3, 10]
	>>> result
	14
	"""
	card = card_list[:]
	if 11 in card and sum(card) > 21:
		for i in range(len(card)):
			if card[i] == 11:
				card[i] = 1
				if sum(card) != 22:
					break
		
		return card, sum(card)
	else:
		return card, sum(card)

#################
# Core function #
#################
def count_card_and_judge(total_player, total_computer):
	"""Compare the sum of player's card and computer's. 
	
	>>> count_card_and_judge(19, 20)
	You Lost!
	>>> count_card_and_judge(22, 20)
	You Lost!
	>>> count_card_and_judge(21, 20)
	You Won!
	>>> count_card_and_judge(13, 25)
	You Won!
	>>> count_card_and_judge(25, 22)
	Tie!
	>>> count_card_and_judge(19, 19)
	Tie!
	"""
	print ("Your total card point is:", total_player)
	print ("Computer's total card point is:", total_computer)

	if total_computer > 21 and total_player <= 21:
		return 'You Won!'
	elif (total_computer > 21 and total_player > 21) or total_player == total_computer:
		return 'Tie!'
	elif total_computer < total_player and total_player <= 21:
		return 'You Won!'
	else:
		return 'You Lost!'
	
def lose_or_win(bet_money, total_money, result):
	"""Return total money in one bet

	win: Return double bet money with total money
	lose: Return total money only
	tie: Return the sum of bet money and total money 
	
	>>>result_win = 'You Won!'
	>>>result_lose = 'You Lost!'
	>>>result_tie = 'Tie!'
	>>>lose_or_win(5, 95, result_win)
	105
	>>>lose_or_win(5, 95, result_lose)
	95
	>>>lose_or_win(5, 95, result_tie)
	100
	"""
	if result == 'You Won!':
		total_money += 2 * bet_money
		return total_money
	elif result == 'You Lost!':
		return total_money
	else:
		total_money += bet_money
		return total_money

def take_turn(card, judge, strategy, computer_card, total_computer=0, total_player=0, 
	money=1000, bet_money=0):
	"""Run one game. Return result and current money.
	
	card: Get new card function
	judge: A function that compare each player's card and return the result
	strategy: The strategy of computer
	total_computer: The sum of computer's card
	total_player: The sum of player's card
	money: Initial money
	bet_money: The bet in one game
	deck: A deck of card
	"""
	global player_total_card
	global computer_total_card
	while True:
			if total_computer > 21 or total_player > 21:
				if 11 not in player_total_card or 11 not in computer_total_card:
					result = judge(total_player, total_computer)
					current_money = lose_or_win(bet_money, money, result)
					print(result)
					print("Computer's second card is:", computer_card)
					print('Your current money is:', current_money)
					return result, current_money
				else:
					if 11 in player_total_card:
						player_total_card, total_player = change_eleven_to_one(player_total_card)
					if 11 in computer_total_card:
						computer_total_card, total_computer = change_eleven_to_one(computer_total_card)
			else:
				print('')
				print('1:hit, 2:stand') # more function can be added
				player_choice = input('What is your choice?') # Player chooses an option
				print()
				
				if player_choice == '1':
					new_card = hit(card, player_total_card)
					player_total_card.append(new_card)
					player_total_card, total_player = change_eleven_to_one(player_total_card)
					print ('Your card is:', new_card)
					print ('Your total card point is:', total_player)
				
				elif player_choice == '2':
					print("Computer's second card is:", computer_card)
					
					while strategy(total_computer):
						new_card = hit(card, computer_total_card)
						computer_total_card.append(new_card)
						computer_total_card, total_computer = change_eleven_to_one(computer_total_card)
						print("Computer's card is:", new_card)
					
					result = judge(total_player, total_computer)
					current_money = lose_or_win(bet_money, money, result)
					print(result)
					print('Your current money is:', current_money)
					return result, current_money	
				else:
					print('Invalid Answer')
		
def play(card, judge, strategy):
	"""Play BlackJack"""
	initial_money = 1000
	while True:
		global deck
		global player_total_card
		global computer_total_card
		deck = deck_without_joker
		player_total_card = []
		computer_total_card = []
		
		#set player's two initial cards, append them to player's card list
		player_first_card, player_second_card = eleven_or_one(card(), []), eleven_or_one(card(), [])
		player_total_card.append(player_first_card)
		player_total_card.append(player_second_card)
		player_total_card, total_player = change_eleven_to_one(player_total_card)
		print ('Your first card is:', player_first_card)
		print ('Your second card is:', player_second_card)
		print ('Your total card point is:', total_player)
		
		#set computer's two initial cards, append them to computer's card list
		computer_first_card, computer_second_card = eleven_or_one(card(), []), eleven_or_one(card(), [])
		computer_total_card.append(computer_first_card)
		computer_total_card.append(computer_second_card)
		computer_total_card, total_computer = change_eleven_to_one(computer_total_card)
		print ("Computer's first card is:", computer_first_card)
		
		#user input bet money loop
		while True:
			try:
				print('You have:', initial_money)
				bet_money = int(input('Your bet?'))
				if bet_money > initial_money:
					1/0
				else:
					break
			except:
				print('Invalid Answer')
				print()
		
		initial_money = initial_money - bet_money
		result, initial_money = take_turn(card, judge, strategy, computer_second_card, 
		total_computer, total_player, initial_money, bet_money)
		
		#print("computer's card", computer_total_card) 
		#print("player's card", player_total_card)
		if initial_money <= 0:
			print('You run out of your money!')
			break
		#print(len(deck_without_joker), len(deck)) check the length of deck 
		option=input("Do you want to play again? Enter 'no' to exit")
		if option == 'no':
			break
		for _ in range(3):
			print ()

########
# Mode #
########
def hit(card, card_list):
	"""The basic mode of game, return new card.
	
	card: Get new card function
	"""
	new_card = eleven_or_one(card(), card_list)
	return new_card
	
############
# Strategy #
############
def strategy_a(total):
	"""A computer strategy that stand when the sum of current card is greater than 17"""
	if total > 17:
		print('The computer chooses to stand')
		return False
	else:
		print('The computer chooses to hit')
		return True
	
print("Let's play BlackJack!")
play(regular_card, count_card_and_judge, strategy_a)

#card_new = make_test_card()
#play(card_new, count_card_and_judge, strategy_a)

#play(user_defined_card, count_card_and_judge, strategy_a)
