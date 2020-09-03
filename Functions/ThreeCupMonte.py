from random import shuffle

# Shuffle Function
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# Will ask player to guess a number. Either 0, 1, 2.
def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0 , 1 , or 2: ")
    
    return int(guess)

# Check if guess is correct or not
def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)

# Initial List
mylist = ['','O','']
# Shuffle List
mixedup = shuffle_list(mylist)
# User Guess
guess = player_guess()
# Check Guess
check_guess(mylist, guess)