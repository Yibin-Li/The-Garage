suits = ['spades', 'clubs', 'hearts', 'diamonds']
numbers = [x for x in range(2, 11)]
special_card = ['Ace', 'Jack', 'Queen', 'King']

def card_generator():
	"""a card with number 11 and suit spades represents as 11 of spades"""
	deck = []
	for color in suits:
		for number in numbers:	
			deck.append('%s of %s' %(number, color))
		for spe in special_card:
			deck.append('%s of %s' %(spe, color))
	for _ in range(2):
		deck.append('Joker')
	return deck
	
deck_with_joker = card_generator()
deck_without_joker = card_generator()[:52]
