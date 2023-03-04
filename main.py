import numpy as np

import classes
import customize
import logic

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


def gameLoop():
    match = customize.customMatch() if customizeMatch else classes.Match()

    while True:
        match.turnNumber += 1

        while True:
            printGame(match)

            (move, msg) = logic.getAndCheckMove(match)
            if move:
                success, msg = logic.performMove(match, move)
                if success:
                    break

            print(msg)

        if match.current().score >= 5:
            printGame(match)
            print("{0} has won the game".format(match.current().name))
            break


gameLoop()
