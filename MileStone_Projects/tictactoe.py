# Function prints outs the board
def display_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

# Function takes in a player input and assigns their marker.
def player_input():
    player1 = 1
    while (player1 != 'X' and player1 != 'O'):
        player1 = input("Please pick a marker 'X' or 'O': ")
    return player1

# Function that takes in the board list object and assigns it to the desired next_position
def place_marker(board, marker, position):
    board[position] = marker
    return board[position]

# Function checks to see if a player has won with their mark choice
def win_check(board, mark):
    if (board[1] == 'X') and (board[2] == 'X') and (board[3] == 'X'):
        print('You won')
    elif (board[4] == 'X') and (board[5] == 'X') and (board[6] == 'X'):
        print('You won')
    elif (board[7] == 'X') and (board[8] == 'X') and (board[9] == 'X'):
        print('You won')
    elif (board[1] == 'X') and (board[4] == 'X') and (board[7] == 'X'):
        print('You won')
    elif (board[2] == 'X') and (board[5] == 'X') and (board[8] == 'X'):
        print('You won')
    elif (board[3] == 'X') and (board[6] == 'X') and (board[9] == 'X'):
        print('You won')
    elif (board[1] == 'X') and (board[5] == 'X') and (board[9] == 'X'):
        print('You won')
    elif (board[3] == 'X') and (board[5] == 'X') and (board[7] == 'X'):
        print('You won')
    else:
        pass

#Function chooses which player will go first
def choose_first():
    player = random.randint(1, 2)
    print("Player {player} goes first")

# Checks if the player's desired position is free
def space_check(board, position):
    for i in board:
        if board[i] == ' ':
            return True
        else:
            return False

# Checks if the board is full and returns a boolean value
def full_board_check(board):
    for i in board:
        if board[i] != ' ':
            return False
        else:
            return True

# Asks for the player's next position and checks if it's a free position
def player_choice(board):
    next_position = int(input("Where would you like to place your next: "))
    space_check(board, next_position)
    return next_position

# Asks the player if he or she wants to play again
def replay():
    question = input("Do you want to play again? ")
    if question[0].lower() == 'y':
        return True
    else:
        return False

def main():
    import random
    print("Welcome to Tic Tac Toe!")
    choose_first()

    while True:
        
