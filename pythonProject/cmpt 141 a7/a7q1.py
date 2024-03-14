# Will Bushell, abc123, 12345678, Jeffrey Long
# this is designed to help with question 1 of A7

import numpy as np

board = np.array([[2, 0, 0], [0, 1, 0], [7, -1, 0]]) # this is a 2D 3x3 array

def print_board(board):
    for y in board:
        print(y)

def board_sum(board):
    sum = 0
    for y in board:
        for x in y:
            sum += x
    return sum

print_board(board)
print(board_sum(board))
