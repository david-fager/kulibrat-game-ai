import numpy as np

import classes
import computer
import customize
import logic

customizeMatch = False


def printGame(match):
    print()
    print(match.getPlayerInfoString(1))

    rowBorder = ["+", "-", "-", "-", "-", "-", "+"]
    print(*rowBorder)
    for i, row in enumerate(match.board):
        cpy = np.copy(row)
        cpy[cpy == " "] = match.vacant
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
            try:
                printGame(match)

                move = computer.getAIMove(match) if match.current().isAI else logic.getUserMove(match)

                if logic.checkMove(match, move, True):
                    break

            except Exception as e:
                print("\t [RESULT] " + e.__str__())

        if match.current().score >= match.playTo:
            printGame(match)
            print("{0} has won the game".format(match.current().name))
            break


gameLoop()
