# Function prints outs the board
def display_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

# Function takes in a player input and assigns their marker.
def player_input():
    marker  = ''
    while (marker != "X" and marker != 'O'):
        marker = raw_input("Pick a marker X or O: ").upper()

    if (marker == 'X'):
        marker = ('X','O')
    else:
        marker = ('O','X')
    return marker

# Function that takes in the board list object and assigns it to the desired next_position
def place_marker(board, marker, position):
    board[position] = marker
    return board[position]

# Function checks to see if a player has won with their mark choice
def win_check(board, mark):
    return( (board[1] == mark) and (board[2] == mark) and (board[3] == mark) or #top row
            (board[4] == mark) and (board[5] == mark) and (board[6] == mark) or #middle row
            (board[7] == mark) and (board[8] == mark) and (board[9] == mark) or #bottom row
            (board[1] == mark) and (board[4] == mark) and (board[7] == mark) or #left column
            (board[2] == mark) and (board[5] == mark) and (board[8] == mark) or # middle column
            (board[3] == mark) and (board[6] == mark) and (board[9] == mark) or #right column
            (board[1] == mark) and (board[5] == mark) and (board[9] == mark) or #diagonal from left to right
            (board[3] == mark) and (board[5] == mark) and (board[7] == mark) ) #diagonal from right to left

# Function chooses which player will go first
def choose_first():
    player1 = random.randint(1,2)
    print("Player {player} goes first".format(player = player1))

    if player1 == 1:
        player2 = 2
    else:
        player2 = 1
    return [player1, player2]

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
def player_choice(board,marker):
    while True:
        try:
            next_position = int(input("Where would you like to place your next {marker} between 1 and 9: ".format(marker = marker)))
            value = space_check(board, next_position)
            if value == True:
                pass
            else:
                continue
            return next_position
        except ValueError:
            print("Please provide an integer between 1 and 9")
            continue
        except IndexError:
            print("Please provide an index within 1 and 9")
            continue
        else:
            #Correct value given, we're reading to leave the loop
            break

# Asks the player if he or she wants to play again
def replay():
    question = raw_input("Do you want to play again? ")
    if question[0].lower() == 'y':
        return True
    else:
        return False

# Resets/Clears the board
def reset_board():
    board = [''] * 10
    return board


############################################################################################
#                                 RUNNING THE GAME
############################################################################################

if __name__ == '__main__':
    import random
    import sys

    while True:
        print("Welcome to Tic Tac Toe!")
        board = reset_board()
        player1, player2 = choose_first()
        marker1, marker2 = player_input()
        turn = min(player1, player2)
        game_playing = True

        while game_playing:

            if turn == 1:
                position = player_choice(board, marker1)
                place_marker(board, marker1, position)
                display_board(board)
                turn += 1
                if win_check(board, marker1):
                    print("YOU WON!")
                    game_playing = False
                if full_board_check(board):
                    game_playing = False

                if game_playing == False:
                    play_again = replay()
                    if play_again:
                        game_playing = True
                        break
                    else:
                        print("Thank you for playing!")
                        sys.exit()

            else:
                position = player_choice(board, marker2)
                place_marker(board, marker2, position)
                display_board(board)
                turn -= 1
                if win_check(board, marker2):
                    print("YOU WON!")
                    game_playing = False
                if full_board_check(board):
                    game_playing =  False

                if game_playing == False:
                    play_again = replay()
                    if play_again:
                        game_playing = True
                        break
                    else:
                        print("Thank you for playing!")
                        sys.exit()
