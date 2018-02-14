# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:13:14 2018

@author: Surojit
"""

import random
from IPython.display import clear_output

# Display the board
def display_board(board):
    clear_output()
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] )
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] )
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] )
    print('   |   |   ')

# Numbered display for 
def numbered_display_board():
    clear_output()
    print("Use below matrix to select your position in the board\n")
    print(' 7 | 8 | 9 ')
    print('-----------')
    print(' 4 | 5 | 6 ')
    print('-----------')
    print(' 1 | 2 | 3 ')

# Choose marker for players
def choose_marker():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1! Please choose marker('X' or 'O'): ").upper()
    if marker == 'X':
        return ('X', 'O')
    elif marker == 'O':
        return ('O', 'X')
    
# Check board if a player has won the game
def check_win(board, player_marker):
    if board[7] == board[8] == board[9] == player_marker or \
        board[4] == board[5] == board[6] == player_marker or \
        board[1] == board[2] == board[3] == player_marker or \
        board[7] == board[4] == board[1] == player_marker or \
        board[8] == board[5] == board[2] == player_marker or \
        board[9] == board[6] == board[3] == player_marker or \
        board[7] == board[5] == board[3] == player_marker or \
        board[9] == board[5] == board[1] == player_marker:
            return True
    else:
        return False

# Choosing randomly a player to play first
def choose_first():
    if random.randint(0, 1) == 0:
        return('Player 1')
    else:
        return('Player 2')

# Check if a position is available in the board
# Here returning ' ' so that calling function can check whether ' ' is present
def check_space(board, position):
    return board[position] == ' '

# Fill the board once a player has made a valid position
def fill_board(board, pos, player_marker):
    board[pos] = player_marker

# Ask players to choose position in the board
def choose_position(board, turn):
    position = ''
    player = turn
    # plyer should enter a number between 1 to 9
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not check_space(board, int(position)):
        position = input(player + ', Choose your position in the board (1-9): ')
    return int(position)
    

def board_full_check(board):    
    for pos in range(1, 10):
        if board[pos] == ' ':
            return False
    return True
    
def replay():
    play_again = input("Play Again? (Yes or No): ").lower()
    if play_again == 'yes' or play_again == 'y':
        return True
    elif play_again == 'no' or play_again == 'n':
        print("Thank you for playing!\n")
        return False
    

def play():
    print()
    print('Welcome to Tic Tac Toe!')
    print('-----------------------\n')

    while True:
        board = [' ']*10
        display_board(board)
        player1_marker, player2_marker = choose_marker()
        print("\nPlayer 1's marker is " + player1_marker)
        print("Player 2's marker is " + player2_marker + "\n")
        turn = choose_first()
        print(turn + " will play first!\n")
        numbered_display_board()
        print("\nLet's Begin\n")
        game_on = True

        while game_on:
            if turn == 'Player 1':
                player1_position = choose_position(board, turn)
                fill_board(board, player1_position, player1_marker)
                display_board(board)
                if check_win(board, player1_marker):
                    print(turn + ' has won the game. Congratulations!')
                    game_on = False
                else:
                    if board_full_check(board):
                        print("Game draw!")
                        game_on = False
                    else:
                        turn = 'Player 2'
            else:
                player2_position = choose_position(board, turn)
                fill_board(board, player2_position, player2_marker)
                display_board(board)
                if check_win(board, player2_marker):
                    print(turn + ' has won the game. Congratulations!')
                    game_on = False
                else:
                    if board_full_check(board):
                        print("Game draw!")
                        game_on = False
                    else:
                        turn = 'Player 1'
        
        if not replay():
            break

play()