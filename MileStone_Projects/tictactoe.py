# Function prints outs the board
def display_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

# Function takes in a player input and assigns their marker.
def player_input(player1):
    marker = ['']
    while (marker[0] != "X" and marker[0] != 'O'):
        marker = raw_input("Player {name_of_player} pick a marker X or O: ".format(name_of_player = player1))
    return marker[0]

# Function that takes in the board list object and assigns it to the desired next_position
def place_marker(board, marker, position):
    board[position] = marker
    return board[position]

# Function checks to see if a player has won with their mark choice
def win_check(board, mark):
    if (board[1] == 'X') and (board[2] == 'X') and (board[3] == 'X'):
        return 1
    elif (board[4] == 'X') and (board[5] == 'X') and (board[6] == 'X'):
        return 1
    elif (board[7] == 'X') and (board[8] == 'X') and (board[9] == 'X'):
        return 1
    elif (board[1] == 'X') and (board[4] == 'X') and (board[7] == 'X'):
        return 1
    elif (board[2] == 'X') and (board[5] == 'X') and (board[8] == 'X'):
        return 1
    elif (board[3] == 'X') and (board[6] == 'X') and (board[9] == 'X'):
        return 1
    elif (board[1] == 'X') and (board[5] == 'X') and (board[9] == 'X'):
        return 1
    elif (board[3] == 'X') and (board[5] == 'X') and (board[7] == 'X'):
        return 1
    else:
        pass

# Function chooses which player will go first
def choose_first():
    player = random.randint(1, 2)
    print("Player {player} goes first".format(player = player))
    return player

# Checks if the player's desired position is free
def space_check(board, position):
    if board[position] != 'X' and board[position] != 'O':
        return True
    else:
        return False

# Checks if the board is full and returns a boolean value
def full_board_check(board):
    spots = 0
    for i in range(len(board)):
        if board[i] == 'X' or board[i] == 'O':
            spots += 1
        else:
            continue
    if spots == 9:
        return True
    else:
        return False

# Asks for the player's next position and checks if it's a free position
def player_choice(board):
    next_position = int(input("Where would you like to place your next: "))
    value = space_check(board, next_position)
    if value == True:
        pass
    else:
        print("Please choose another position")
    return next_position

# Asks the player if he or she wants to play again
def replay():
    question = raw_input("Do you want to play again? ")
    if question[0].lower() == 'y':
        return True
    else:
        return False

# Resets/Clears the board
def reset_board():
    board = ['','','','','','','','','','']
    return board

############################################################################################
#                                 RUNNING THE GAME
############################################################################################

if __name__ == '__main__':
    import random
    import sys

    print("Welcome to Tic Tac Toe!")
    board = reset_board()
    player1 = choose_first()
    i = 0

    while True:
        marker1 = player_input(player1)

        while (player1 == 1):
            next_position = player_choice(board)
            place_marker(board, marker1,next_position)
            display_board(board)

            if full_board_check(board) == True:
                print('Game Over Board Full')
                break
            else:
                continue

            player1 += 1
            i+=1

            result = win_check(board, marker1)
            if result == 1:
                print("You won!")
                break
            else:
                pass


        while(player1 == 2):
            next_position = player_choice(board)
            place_marker(board, marker1,next_position)
            display_board(board)

            if full_board_check(board) == True:
                print('Game Over Board Full')
                break
            else:
                continue

            player1 -= 1
            i+=1

            result = win_check(board, marker1)
            if result == 1:
                print("You won!")
                break
            else:
                pass

# The script will ask the players if they want to play again. If not, the program will terminate
        play_again = replay()
        if play_again == 'y':
            break
        else:
            print("Thank you for playing!")
            sys.exit()
