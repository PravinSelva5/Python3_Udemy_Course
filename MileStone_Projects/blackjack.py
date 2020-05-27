'''
PLAYER GOAL: GET CLOSER TO A TOTAL VALUE OF 21 THAN THE DEALER DOES

POSSIBLE ACTIONS:
    1. Hit - Receive another card
    2. Stay -  Stop receiving cards

Ignore the following actions -- Insurance, Split, Double Down

AFTER PLAYER TURN:
    IF PLAYER IS UNDER 21, DEALER THEN HITS UNTIL THEY EITHER BEAT THE PLAYER OR
    DEALER BUSTS(OVER 21)

POSSIBLE GAME END SCENARIOS:
    - PLAYER CONTINUES TO HITS AND GOES OVER 21
    - COMPUTER DEAL BEATS THE PLAYER BY HAVING A HIGHER SUM THAN PLAYER & IS UNDER 21
    - PLAYER WINS AFTER COMPUTER DEALER'S TURN

SPECIAL RULES:
    - FACES CARD = 10
    - ACES = 1 OR 11 WHICHEVER VALUE IS PREFERABLE TO THE PLAYER
'''

# Importing modules and setting global variables
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}

playing = True

# Card class
class Card:
    def __init__(self,suits,ranks):
        self.suit = suits
        self.rank = ranks

    def __str__(self):
        return ('{rank} of {suit}'.format(rank = self.rank, suit=self.suit))

# Create a Deck of class
class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        complete_deck = ''
        for cards in self.deck:
            complete_deck += '\n' + cards.__str__()
        return 'The deck has:' + complete_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        deal_card = self.deck.pop()
        return deal_card

# Creating a Hand class
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.suit == 'Aces':
            self.aces = 1

    def adjust_for_ace(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
