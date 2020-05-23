if __name__ == '__main__':
    import random
    import sys

    print("Welcome to Tic Tac Toe!")
    board = reset_board()
    player1, player2 = choose_first()
    marker1, marker2 = player_input()
    turn = min(player1, player2)

    while True:

        if turn == 1:
            # First player's turn
            position = player_choice(board, marker1)
            place_marker(board, marker1, position)
            #Checks if the player has won with the given marker

            if (win_check(board, marker1)):
                print("YOU WON!")
                display_board(board)
                play_again = replay()
                if play_again:
                    board = reset_board()
                    break
                else:
                    print("Thank you for playing!")
                    sys.exit()
            else:
            # Check whether the board is full
            # If full, it'll ask the player to play again or quit.
            if(full_board_check(board) == True):
                # Players are asked if they want to play again. If not, the program will terminate
                play_again = replay()
                if play_again:
                    board = reset_board(board)
                    break
                else:
                    print("Thank you for playing!")
                    sys.exit()

            display_board(board)
            turn += 1

        else:
            # Second player's turn
            position = player_choice(board, marker2)
            place_marker(board, marker2, position)
            if (win_check(board, marker2)):
                display_board(board)
                print("YOU WON!")
                play_again = replay()
                if play_again:
                    board = reset_board()
                    break
                else:
                    print("Thank you for playing!")
                    sys.exit()
            # Checks whether the board is full
            else:
                if (full_board_check(board) == True):
                    # Players are asked if they want to play again. If not, the program will terminate
                    play_again = replay()
                    if play_again:
                        reset_board(board)
                        break
                    else:
                        print("Thank you for playing!")
                        sys.exit()
                else:
                    display_board(board)
                    turn -= 1
