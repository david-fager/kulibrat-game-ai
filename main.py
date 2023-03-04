import numpy as np

import classes
import computer
import customize

customizeMatch = False


def printGame(match):
    print(match.getPlayerInfoString(1))

    rowBorder = ["+", "-", "-", "-", "-", "-", "+"]
    print(*rowBorder)
    for i, row in enumerate(match.board):
        cpy = np.copy(row)
        cpy[cpy == " "] = match.emptySymbol
        print("| {:} |".format(" | ".join(cpy)) + f" {i + 1}")
        print(" ".join(rowBorder))
    print("  {:}  ".format("   ".join(["a", "b", "c"])))

    print(match.getPlayerInfoString(0))
    print()


def performMove(match, move):
    pass


def gameLoop():
    match = customize.customMatch() if customizeMatch else classes.Match()

    while True:
        match.turnNumber += 1

        printGame(match)

        if match.current().isAI:
            move = computer.getAIMove(match)
        else:
            move = input("[{0}] Perform a move (e.g. a1-a2): ".format(match.current().name)).split("-")

        performMove(match, move)

        if match.current().score >= 5:
            printGame(match)
            print("{0} has won the game".format(match.current().name))
            break


gameLoop()
