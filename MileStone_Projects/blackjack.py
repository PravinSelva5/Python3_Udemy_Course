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
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

# Card class
class Card:
    def __init__(self,suits,ranks):
        self.suits = suits
        self.ranks = ranks

    def __str__(self):
        return ('{rank} of {suit}'.format(rank = self.ranks, suit=self.suits))

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
        #card from Deck.deal() --> single card (suit, rank)
        self.cards.append(card)
        self.value += values[card.ranks]
        if card.ranks == 'Ace':
            self.aces += 1

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

    def __init__(self, total = 100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

'''
Function for taking bets
Since we're asking the user for an integer value, this would be a good place to use try,except.
Remember to check that a Player's bet can be covered by their available chips.
'''
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Please provide an integer value.")
        else:
            if chips.bet > chips.total:
                print("Sorry you don't have enough chips. You have: {}".format(chips.total))
            else:
                break

'''
Function for taking hits
Either player can take hits until they bust. This function will be called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17.
It should take in Deck and Hand objects as arguments, and deal one card off the deck and add it to the Hand.
You may want it to check for aces in the event that a player's hand exceeds 21.
'''
def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

'''
Function prompting the Player to Hit or Stand
This function should accept the deck and the player's hand as arguments, and assign playing as a global variable.
If the Player Hits, employ the hit() function above. If the Player Stands, set the playing variable to False - this will control the behavior of a while
loop later on in our code.
'''
def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter 'h' or 's': ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        
        elif x[0].lower() == 's':
            print("Player stands, Dealer's Turn")
            playing = False
        else:
            print("Sorry i didn't understand that, please enter h or s only.")
            continue
        break

'''
Functions to display cards
When the game starts, and after each time Player takes a card, the dealer's first card is hidden and all of Player's cards are visible.
At the end of the hand all cards are shown, and you may want to show each hand's total value. Write a function for each of these scenarios.
'''
def show_some(player,dealer):
    print('DEALERS HAND: ')
    print('one card hidden!')
    print(dealer.cards[1])
    print('\n')
    print('PLAYERS HAND:')
    print('\n')
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print('DEALERS HAND: ')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('PLAYERS HAND: ')
    print('\n')
    for card in player.cards:
        print(card)
'''
Functions to handle end of game scenarios. Remember to pass player's hand, dealer's hand and chips as needed.
'''
def player_busts(player,dealer,chips):
    print("BUST PLAYER \n")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player, dealer):
    print("Player and Dealer tie! PUSH!")



while True:
    # Print an opening statement
    print("WELCOME TO BLACK JACK")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print('Player total chips are at: {}'.format(player_chips.total))
    # Ask to play again
    new_game = input("Would you like to play another hand? y/n: ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break
