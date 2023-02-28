import numpy as np

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
emptySymbol = ""

def userTurn():
    rowBorder = ["+", "-", "-", "-", "-", "-", "+"]
    print(*rowBorder)
    for row in board:
        cpy = np.copy(row)
        cpy[cpy == " "] = emptySymbol if emptySymbol else " "
        print("| {:} |".format(" | ".join(cpy)))
        print(" ".join(rowBorder))

def aiTurn():
    print('not implemented yet')


def gameLoop():
    while True:
        userTurn()
        aiTurn()
        break

    print('Game Over')


gameLoop()
