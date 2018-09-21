from A_Deck import deck_without_joker
import re

deck = deck_without_joker
deck.append(deck_without_joker)
big_or_small = {"high card": 1, "one pair": 2, "two pair": 3, "three of a kind": 4,
				"straight": 5, "flush": 6, "full house": 7, "four of a kind": 8, 
				"straight flush": 9, "royal flush": 10}

def condition (input_deck):
	""" Return the correct condition (level) of input_deck. 
	Divide to three situation: 1. two cards 2. five cards 3. seven cards
	
	>>> new_deck1 = ["1 of spades", "2 of spades", "3 of spades", "4 of spades"]
	>>> result = condition(new_deck1)
	>>> result
	four of a kind
	
	>>> new_deck2 = ["1 of diamond", "2 of spades", "Jack of spades", "9 of clubs"]
	>>> result = condition(new_deck2)
	>>> result
	high card: 11
	
	"""
	if (len(input_deck) == 2):
		if (find_num(input_deck[0]) == find_num(input_deck[1])):
			return "one pair"
	elif ((len(input_deck)) == 5):
		special = []
		four_cards_pair = combination(4, input_deck)
		for x in four_cards_pair:
			if (x[0] == x[1] == x[2] == x[3]):
				special.apppend(x)
		if (len(speical) > 0):
			for j in special: # to find if 4 four cards have different kind
				...
	
def find_num(card):
	""" Return the number of card.
	
	>>> find_num("5 of clubs")
	5
	
	>>> find_num("Jack of spades")
	11
	
	"""
	if (card[0] in str([i for i in range(2, 11)])):
		return re.findall("^[0-9]+", card)[0]
	else:
		num = re.findall("([A-Z][a-z].+)\sof", card)[0]
		if (num == "Ace"):
			return 1
		elif (num == "Jack"):
			return 11
		elif (num == "Queen"):
			return 12
		elif (num == "King"):
			return 13

def find_kind(card):
	""" Return the kind of card.
	
	>>> find_kind("5 of clubs")
	clubs
	
	>>> find_kind("Jack of spades")
	spades
	
	"""
	return re.findall(".+of\s([a-z].+)", card)[0]
	
def combination (set_num, input_list):
	""" Return all non-repeated possible combination 
		(a list of lists) of given set number.
	
	>>> combination(2, ["1", "2", "3", "4"])
	[["1", "2"], ["1", "3"], ["1", "4"], ["2", "3"], ["2", "4"], ["3", "4"]]
	
	>>> combination(1, ["4", "2", "1"])
	[["4"], ["2"], ["1"]]
	
	>>> combination(4, ["4", "2", "1"])
	Invalid Combination
	
	"""
	result = []
	if (len(input_list) == 0):
		return result
	if (set_num > len(input_list)):
		return "Invalid Combination"
	if (set_num == 1):
		for x in input_list:
			e = list(x)
			result.append(e)
		return result
	for i in range(len(input_list)):
		further_result = combination(set_num - 1, input_list[i + 1:])
		for k in further_result:
			e = list(input_list[i])
			result.append(e + k)
	return result
	
	
def who_win (condition_player, condition_computer):
	""" Return the result of game.
	
	>>> condition_player = "royal flush"
	>>> condition_computer = "high card"
	>>> who_win(condition_player, condition_computer)
	Player win!
	
	>>> condition_player = "two pair"
	>>> condition_computer = "full house"
	>>> who_win(condition_player, condition_computer)
	Computer win!
	
	>>> condition_player = "two pair"
	>>> condition_computer = "two pair"
	>>> who_win(condition_player, condition_computer)
	Draw!
	
	"""
	
	player = big_or_small.get(condition_player)
	comp = big_or_small.get(condition_computer)
	if (player > comp):
		return "Player win!"
	elif (player < comp):
		return "Computer win!"
	else:
		return "Draw!"
