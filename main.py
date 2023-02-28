import numpy as np

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]


def userTurn():
    ends = ["-", "-", "-"]
    sides = np.transpose([["+", "|", "|", "|", "|", "+"]])
    bordered = np.vstack([ends, board, ends])
    bordered = np.hstack([sides, bordered, sides])

    for line in bordered:
        print(*line)

def aiTurn():
    print('not implemented yet')


def gameLoop():
    while True:
        userTurn()
        aiTurn()
        break

    print('Game Over')


gameLoop()
