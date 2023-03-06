import time

import numpy as np

import classes
import userInput


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


def customMatch():
    playerCount = 2
    players = []

    matchVacancy = userInput.askLoop("How should a vacant board slot look? (single char): ")
    matchLength = userInput.askLoop("The score to win the game (3-30): ", np.arange(3, 31).astype(str))

    for i in range(playerCount):
        name = input("[Player {0}] name: ".format(i + 1))
        piece = userInput.askLoop("[{0}] piece character (single char): ".format(name))
        yn = userInput.askLoop("[{0}] is computer? (y/n): ".format(name), ["y", "n"])
        players.append(classes.Player(name, piece, yn == "y"))

    return classes.Match(matchVacancy if matchVacancy else " ", players, int(matchLength))


def canMoveAnything(match):
    # TODO: check that current player can move. If not simulate turn change and check their movability
    # simulate, something like: matchCopy = copy.copy(match), matchCopy.turnNumber += 1

    # print("\t[INFO] {0} is unable to move: skipping turn".format(match.current().name))
    # time.sleep(2)
    return True


def overrideMatch(match):
    # match.current().score = 30
    modified = [[match.vacant] * 3 for i in range(4)]
    modified[3][1] = match.players[0].piece
    modified[3][0] = modified[3][2] = match.players[1].piece
    modified[2][0] = modified[2][2] = match.players[1].piece
    match.board = modified

    # TODO: make it so that certain board scenarios can be setup, to check code correctness
    
    # Return value is whether to skip the turn or not
    return False
