"""
Author: Shingai Dzinotyiweyi
Date: 2024/03/05

Tic Tac Toe Game:
I created this Tic-Tac-Toe game through the terminal.
To play the game, each player must select an index to play their move.
The index selected must be emtpty to be a valid move.
The first player to match three symbols diagonally, vertically or horizontally wins.

Enjoy 😃
"""

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
print("Player 1: X\n"
      "Player 2: O")
print(board)


def match(board):
    # Check for Player 1 matches
    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        return "Player 1 Wins"
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        return "Player 1 Wins"
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        return "Player 1 Wins"
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        return "Player 1 Wins"
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        return "Player 1 Wins"

    # Check for Player 2 matches
    if board[0] == "O" and board[3] == "O" and board[6] == "O":
        return "Player 2 Wins"
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        return "Player 2 Wins"
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        return "Player 2 Wins"
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        return "Player 2 Wins"
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        return "Player 2 Wins"


order = [1, 2, 1, 2, 1, 2, 1, 2, 1]


def move(order):
    for play in order:
        if play == 1:
            player_1 = int(input("P1: Choose a position between 0 - 8"))
            # valid = False
            # while valid:
            if player_1 >= 0 or player_1 <= 8:
                if board[player_1] == " ":
                    board[player_1] = "X"
                    valid = True
                else:
                    print("Invalid Move....Try Again.")
                    player_1 = int(input("P1: Choose a position between 0 - 8"))
            else:
                print("Out Of Range....Try Again.")
                player_1 = int(input("P1: Choose a position between 0 - 8"))

        if play == 2:
            player_2 = int(input("P2: Choose a position between 0 - 8"))
            # valid = False
            # while valid:
            if player_2 >= 0 or player_2 <= 8:
                if board[player_2] == " ":
                    board[player_2] = "O"
                    valid = True
                else:
                    print("Invalid Move....Try Again.")
                    player_2 = int(input("P2: Choose a position between 0 - 8"))
            else:
                print("Out Of Range....Try Again.")
                player_2 = int(input("P2: Choose a position between 0 - 8"))

        print(f"|{board[0]}|{board[1]}|{board[2]}|\n"
              f"|{board[3]}|{board[4]}|{board[5]}|\n"
              f"|{board[6]}|{board[7]}|{board[8]}|\n")

        # Check for Player 1 matches
        if board[0] == "X" and board[3] == "X" and board[6] == "X":
            return "Player 1 Wins"
        elif board[1] == "X" and board[4] == "X" and board[7] == "X":
            return "Player 1 Wins"
        elif board[2] == "X" and board[5] == "X" and board[8] == "X":
            return "Player 1 Wins"
        elif board[0] == "X" and board[1] == "X" and board[2] == "X":
            return "Player 1 Wins"
        elif board[3] == "X" and board[4] == "X" and board[5] == "X":
            return "Player 1 Wins"
        elif board[6] == "X" and board[7] == "X" and board[8] == "X":
            return "Player 1 Wins"
        elif board[0] == "X" and board[4] == "X" and board[8] == "X":
            return "Player 1 Wins"
        elif board[2] == "X" and board[4] == "X" and board[6] == "X":
            return "Player 1 Wins"

        # Check for Player 2 matches
        if board[0] == "O" and board[3] == "O" and board[6] == "O":
            return "Player 2 Wins"
        elif board[1] == "O" and board[4] == "O" and board[7] == "O":
            return "Player 2 Wins"
        elif board[2] == "O" and board[5] == "O" and board[8] == "O":
            return "Player 2 Wins"
        elif board[0] == "O" and board[1] == "O" and board[2] == "O":
            return "Player 1 Wins"
        elif board[3] == "O" and board[4] == "O" and board[5] == "O":
            return "Player 1 Wins"
        elif board[6] == "O" and board[7] == "O" and board[8] == "O":
            return "Player 1 Wins"
        elif board[0] == "O" and board[4] == "O" and board[8] == "O":
            return "Player 2 Wins"
        elif board[2] == "O" and board[4] == "O" and board[6] == "O":
            return "Player 2 Wins"


# while match(board) != "Draw":

print(move(order))

print(board)