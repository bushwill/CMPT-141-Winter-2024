# Will Bushell, abc123, 12345678, Jeffrey Long
# this is designed to help with question 3 of A7

import numpy as np

board = np.array([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]])

def shoot(board, coord):
    if valid(board, coord[0], coord[1]):
        board[coord[0], coord[1]] = 0
    if valid(board, coord[0], coord[1]+1):
        board[coord[0], coord[1]+1] -= 1
    if valid(board, coord[0]+1, coord[1]+1):
        board[coord[0]+1, coord[1]+1] -= 1
    if valid(board, coord[0]+1, coord[1]):
        board[coord[0]+1, coord[1]] -= 1
    if valid(board, coord[0]+1, coord[1]-1):
        board[coord[0]+1, coord[1]-1] -= 1
    if valid(board, coord[0], coord[1]-1):
        board[coord[0], coord[1]-1] -= 1
    if valid(board, coord[0]-1, coord[1]-1):
        board[coord[0]-1, coord[1]-1] -= 1
    if valid(board, coord[0]-1, coord[1]):
        board[coord[0]-1, coord[1]] -= 1
    if valid(board, coord[0]-1, coord[1]+1):
        board[coord[0]-1, coord[1]+1] -= 1
    

def valid(board, x, y):
    if x >= len(board) or x < 0:
        return False
    if y >= len(board) or y < 0:
        return False
    return True

def print_boardcoords(board):
    count = len(board)
    for y in board:   
        print(str(count), y)
        count -= 1 
    print('   ', end='')
    for n in range(1, len(board)+1):
        print(n, '', end='')
    print()

play = True
while play:
    print_boardcoords(board)
    quit = input("Quit? ")
    if quit == 'y':
        play = False
    else:
        x = input("Enter the x coordinate: ")
        y = input("Enter the y coordinate: ")
        shoot(board, (len(board)-(int(y)), int(x)-1) )