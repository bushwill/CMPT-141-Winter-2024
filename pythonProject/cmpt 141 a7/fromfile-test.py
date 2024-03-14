import numpy as np

def isLegal(filename):
    file = open(filename, 'r')
    board = []
    for line in file:
        board.append(line.strip("\n").split(" "))

    numpy_board = np.array(board)



isLegal('')