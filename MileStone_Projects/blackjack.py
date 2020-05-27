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
'''
Creates a Chip class
In addition to decks of cards and hands, we need to keep track of a Player's starting chips, bets, and ongoing winnings.
This could be done using global variables, but in the spirit of object oriented programming, let's make a Chips class instead!
'''
class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        pass

    def lose_bet(self):
        pass

'''
Function for taking bets
Since we're asking the user for an integer value, this would be a good place to use try,except.
Remember to check that a Player's bet can be covered by their available chips.
'''
def take_bet():

    pass

'''
Function for taking hits
Either player can take hits until they bust. This function will be called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17.
It should take in Deck and Hand objects as arguments, and deal one card off the deck and add it to the Hand.
You may want it to check for aces in the event that a player's hand exceeds 21.
'''
def hit(deck,hand):

    pass

'''
Function prompting the Player to Hit or Stand
This function should accept the deck and the player's hand as arguments, and assign playing as a global variable.
If the Player Hits, employ the hit() function above. If the Player Stands, set the playing variable to False - this will control the behavior of a while
loop later on in our code.
'''
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

    pass

'''
Functions to display cards
When the game starts, and after each time Player takes a card, the dealer's first card is hidden and all of Player's cards are visible.
At the end of the hand all cards are shown, and you may want to show each hand's total value. Write a function for each of these scenarios.
'''
def show_some(player,dealer):

    pass

def show_all(player,dealer):

    pass

'''
Functions to handle end of game scenarios. Remember to pass player's hand, dealer's hand and chips as needed.
'''
def player_busts():
    pass

def player_wins():
    pass

def dealer_busts():
    pass

def dealer_wins():
    pass

def push():
    pass



while True:
    # Print an opening statement


    # Create & shuffle the deck, deal two cards to each player



    # Set up the Player's chips


    # Prompt the Player for their bet


    # Show cards (but keep one dealer card hidden)


    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand


        # Show cards (but keep one dealer card hidden)


        # If player's hand exceeds 21, run player_busts() and break out of loop


            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17


        # Show all cards

        # Run different winning scenarios


    # Inform Player of their chips total

    # Ask to play again

        break
