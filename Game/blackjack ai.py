import re 
import time
import matplotlib.pyplot as plt
import numpy as np
from random import randint
from a_deck import deck_without_joker

#Initiate all global variables
deck = deck_without_joker
player_total_card = []
player_1_total_card = []

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
	
	#delete this card in the deck list
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
def count_card_and_judge(total_player_0, total_player_1):
	"""Compare the sum of player's card and player_1's. 
	
	>>> count_card_and_judge(19, 20)
	player_0 Lost!
	>>> count_card_and_judge(22, 20)
	player_0 Lost!
	>>> count_card_and_judge(21, 20)
	player_0 Won!
	>>> count_card_and_judge(13, 25)
	player_0 Won!
	>>> count_card_and_judge(25, 22)
	Tie!
	>>> count_card_and_judge(19, 19)
	Tie!
	"""
	#print ("player_0 total card point is:", total_player_0)
	#print ("player_1's total card point is:", total_player_1)

	if total_player_1 > 21 and total_player_0 <= 21:
		return 'player_0 Won!'
	elif (total_player_1 > 21 and total_player_0 > 21) or total_player_0 == total_player_1:
		return 'Tie!'
	elif total_player_1 < total_player_0 and total_player_0 <= 21:
		return 'player_0 Won!'
	else:
		return 'player_0 Lost!'
	
def lose_or_win(bet_money, total_money, result):
	"""Return total money in one bet.

	win: Return double bet money with total money
	lose: Return total money only
	tie: Return the sum of bet money and total money 
	
	>>>result_win = 'player_0 Won!'
	>>>result_lose = 'player_0 Lost!'
	>>>result_tie = 'Tie!'
	>>>lose_or_win(5, 95, result_win)
	105
	>>>lose_or_win(5, 95, result_lose)
	95
	>>>lose_or_win(5, 95, result_tie)
	100
	"""
	if result == 'player_0 Won!':
		total_money += 2 * bet_money
		return total_money
	elif result == 'player_0 Lost!':
		return total_money
	else:
		total_money += bet_money
		return total_money

def take_turn(card, judge, strategy_player_0, strategy_player_1, player_1_card, 
	total_player_1=0, total_player_0=0, money=1000, bet_money=0):
	"""Run one game. Return result and current money.
	
	card: Get new card function
	judge: A function that compare each player's card and return the result
	strategy: The strategy of player_1
	total_player_1: The sum of player_1's card
	total_player_0: The sum of player's card
	money: Initial money
	bet_money: The bet in one game
	deck: A deck of card
	"""
	global player_total_card
	global player_1_total_card
	while True:
			if total_player_1 > 21 or total_player_0 > 21:
				if 11 not in player_total_card or 11 not in player_1_total_card:
					result = judge(total_player_0, total_player_1)
					current_money = lose_or_win(bet_money, money, result)
					#print(result)
					#print("player_1's second card is:", player_1_card)
					#print('player_0 current money is:', current_money)
					return result, current_money
				else:
					if 11 in player_total_card:
						player_total_card, total_player_0 = change_eleven_to_one(player_total_card)
					if 11 in player_1_total_card:
						player_1_total_card, total_player_1 = change_eleven_to_one(player_1_total_card)
			else:
				
				#time.sleep(1)
				#print()
				if strategy_player_0(total_player_0):
					player_0_choice = '1'
					#print('player_0 chooses to hit')
				else:
					player_0_choice = '2'
					#print('player_0 chooses to stand')
				
				if player_0_choice == '1':
					new_card = hit(card, player_total_card)
					player_total_card.append(new_card)
					player_total_card, total_player_0 = change_eleven_to_one(player_total_card)
					#print ('player_0 card is:', new_card)
					#print ('player_0 total card point is:', total_player_0)
				
				elif player_0_choice == '2':
					#print("player_1's second card is:", player_1_card)
					
					while strategy_player_1(total_player_1):
						new_card = hit(card, player_1_total_card)
						player_1_total_card.append(new_card)
						player_1_total_card, total_player_1 = change_eleven_to_one(player_1_total_card)
						#print("player_1's card is:", new_card)
					
					result = judge(total_player_0, total_player_1)
					current_money = lose_or_win(bet_money, money, result)
					#print(result)
					#print('player_0 current money is:', current_money)
					return result, current_money	
				else:
					print('Invalid Answer')
		
def play(card, judge, strategy_player_0, strategy_player_1, turns):
	"""Play BlackJack"""
	initial_money = 1000000000
	turn = 0
	result_lst = []
	while turn < turns:
		global deck
		global player_total_card
		global player_1_total_card
		deck = deck_without_joker
		player_total_card = []
		player_1_total_card = []
		
		#set player's two initial cards, append them to player's card list
		player_first_card, player_second_card = eleven_or_one(card(), []), eleven_or_one(card(), [])
		player_total_card.append(player_first_card)
		player_total_card.append(player_second_card)
		player_total_card, total_player_0 = change_eleven_to_one(player_total_card)
		#print ('player_0 first card is:', player_first_card)
		#print ('player_0 second card is:', player_second_card)
		#print ('player_0 total card point is:', total_player_0)
		
		#set player_1's two initial cards, append them to player_1's card list
		player_1_first_card, player_1_second_card = eleven_or_one(card(), []), eleven_or_one(card(), [])
		player_1_total_card.append(player_1_first_card)
		player_1_total_card.append(player_1_second_card)
		player_1_total_card, total_player_1 = change_eleven_to_one(player_1_total_card)
		#print ("player_1's first card is:", player_1_first_card)
		
		#print('player_0 have:', initial_money)
		#print('player_0 bet?')
		
		#time.sleep(1)
		#print('player_0 bet 100')
		bet_money = 100		
		
		initial_money = initial_money - bet_money
		result, initial_money = take_turn(card, judge, strategy_player_0, 
		strategy_player_1, player_1_second_card, total_player_1, total_player_0, 
		initial_money, bet_money)
		
		#print("player_1's card", player_1_total_card) 
		#print("player's card", player_total_card)
		#print()
		if initial_money <= 0:
			print('player_0 run out of player_0 money!')
			break
		#print(len(deck_without_joker), len(deck)) check the length of deck 
		
		#time.sleep(1)
		turn += 1
		#print('%s turns'%(turn))
		#print()
		result_lst.append(result)
	return result_lst	
		

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
def strategy_card_total_number(number):
	"""A strategy that stand when the sum of current card is greater than number"""
	def check_total(total):
		if total > number:
			return False
		else:
			return True
	return check_total

def strategy_14(total):
	"""A strategy that stand when the sum of current card is greater than 14"""
	if total > 14:
		return False
	else:
		return True

def strategy_15(total):
	"""A strategy that stand when the sum of current card is greater than 15"""
	if total > 15:
		return False
	else:
		return True

def strategy_16(total):
	"""A strategy that stand when the sum of current card is greater than 16"""
	if total > 16:
		return False
	else:
		return True

def strategy_17(total):
	"""A strategy that stand when the sum of current card is greater than 17"""
	if total > 17:
		return False
	else:
		return True		

def strategy_18(total):
	"""A strategy that stand when the sum of current card is greater than 18"""
	if total > 18:
		return False
	else:
		return True		
		
def strategy_19(total):
	"""A strategy that stand when the sum of current card is greater than 19"""
	if total > 19:
		return False
	else:
		return True
		
def strategy_20(total):
	"""A strategy that stand when the sum of current card is greater than 20"""
	if total > 20:
		return False
	else:
		return True		

####################
# Drawing function #
####################
def bar_graph(category, *data):
	"""Draw bar graph.
	
	category: A list of category represented as number, the length of list is
	the length of category e.g. [1, 2, 3, 4]
	data: List(s) of data e.g. [5, 6, 7 ,8]
	The length of category and the length of each data must be equal.
	"""
	for o in data:
		assert len(o) == len(category), 'You must have same length list for category and data'
	plt.figure()
	data1_x_val = []
	data2_x_val = []
	for x in category:
		data1_x_val.append(x - 0.15)
	plt.bar(data1_x_val, data[0], width = 0.3)
	
	for x in category:
		data2_x_val.append(x + 0.15)
	plt.bar(data2_x_val, data[1], width=0.3, color='red')
	
	plt.xlabel('The number of play turns')
	plt.ylabel('The number of lose and win')
	plt.title('Analysis of the relationship between game turns and result')
	plt.legend(['normal', 'quardratic'])
	#ax = plt.gca()
	#ax.axis([])
	#plt.savefig('C:\\Users\\lyb\\Desktop\\MyFig4.png')
	plt.show()

#########################
# Count result function #
#########################
def count_result(result):
	"""Convert result list to a dictionary.
	
	>>> count_result(['win', 'win', 'tie', 'lose', 'lose'])
	{'win':2, 'tie':1, 'lose':2}
	"""
	count = {}
	for x in result:
		count[x] = count.get(x,0) + 1
	return count

def get_average(play_turns, loop_turns, player_0_strategy, player_1_strategy):
	"""A function that returns average win, lose and tie times 
	in given play turns and loop turns.
	
	"""
	win_number, lose_number, tie_number = [], [], []
	
	while loop_turns > 0:
		lst_of_result = play(regular_card, count_card_and_judge, 
		player_0_strategy, player_1_strategy, play_turns)
		
		result_dict = count_result(lst_of_result)
		lose_number.append(result_dict.get('player_0 Lost!',0))
		win_number.append(result_dict.get('player_0 Won!',0))
		tie_number.append(result_dict.get('Tie!',0))
		loop_turns -= 1
	
	win = np.round(np.mean(win_number), 2)
	lose = np.round(np.mean(lose_number), 2)
	tie = np.round(np.mean(tie_number), 2)
	return win, lose, tie

 	
def win_lose_or_tie(result):
	return 
	
print("Let's play BlackJack!")
#play(regular_card, count_card_and_judge, strategy_14, strategy_20, 100)


#card_new = make_test_card()
#play(card_new, count_card_and_judge, strategy_17, strategy_15, 1000)

#k = play(user_defined_card, count_card_and_judge, strategy_17, strategy_17, 1000)

#bar_graph([1], [3], [6])
print(get_average(100, 1000, strategy_20, strategy_20))
