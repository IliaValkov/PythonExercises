from pprint import pprint
from random import shuffle

values = list(range(1,11)) + 'Jack Queen King'.split() 
suits = 'diamonds clubs hearts spades'.split()

deck = ['%s of %s' % (value, suit) for suit in suits for value in values ]

shuffle(deck)

pprint(deck[:12])

while deck: input(deck.pop())