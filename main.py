import numpy as np

import classes
import customize

customizeMatch = False


def printGame(match):
    print(match.players[0].name)

    rowBorder = ["+", "-", "-", "-", "-", "-", "+"]
    print(*rowBorder)
    for row in match.board:
        cpy = np.copy(row)
        cpy[cpy == " "] = match.emptySymbol
        print("| {:} |".format(" | ".join(cpy)))
        print(" ".join(rowBorder))

    print(match.players[1].name)
    print()


def userTurn():
    pass


def aiTurn():
    pass


def gameLoop():
    match = customize.customMatch() if customizeMatch else classes.Match()

    while True:
        printGame(match)
        aiTurn() if match.current().isAI else userTurn()
        match.turnNumber += 1

        if match.turnNumber > 10:
            break

    print('Game Over')


gameLoop()
