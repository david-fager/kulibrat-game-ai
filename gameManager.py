import numpy as np

import classes
import userInput


def printGame(match, testingAI=False):
    if testingAI:
        print("{0} ({1}/{2})".format(match.getCurrentPlayer().name, match.getCurrentPlayer().score, match.playTo))
        return

    print("\n" + match.getPlayerInfoString(1))
    printBoard(match)
    print(match.getPlayerInfoString(0) + "\n")


def printBoard(match):
    rowBorder = ["+", "-", "-", "-", "-", "-", "+"]
    print(*rowBorder)
    for i, row in enumerate(match.board):
        print("| {} | {}".format(" | ".join(row), i + 1))
        print(*rowBorder)
    print("  {}  ".format("   ".join(["a", "b", "c"])))


def printEndGame(match):
    print()
    print("Final board:")
    printBoard(match)
    print()
    print("WINNER: {0}".format(match.getCurrentPlayer().toString()))
    print("VERSUS: {0}".format(match.getCurrentOpponent().toString()))


def customMatch(testingAI):
    playerCount = 2
    players = []

    if testingAI:
        players.append(classes.Player("AI 1", "X", True))
        players.append(classes.Player("AI 2", "O", True))
        return classes.Match(" ", players, 20)

    matchVacancy = userInput.askLoop("How should a vacant board slot look? (single char): ")
    matchLength = userInput.askLoop("The score to win the game (3-30): ", np.arange(3, 31).astype(str))

    for i in range(playerCount):
        name = input("[Player {0}] name: ".format(i + 1))
        piece = userInput.askLoop("[{0}] piece character (single char): ".format(name))
        yn = userInput.askLoop("[{0}] is computer? (y/n): ".format(name), ["y", "n"])
        players.append(classes.Player(name, piece, yn == "y"))

    return classes.Match(matchVacancy if matchVacancy else " ", players, int(matchLength))


def overrideMatch(match):
    modified = [[match.vacant] * 3 for i in range(4)]
    modified[3][1] = match.players[0].piece
    modified[3][0] = modified[3][2] = match.players[1].piece
    modified[2][0] = modified[2][2] = match.players[1].piece
    match.board = modified

    # TODO: make it so that certain board scenarios can be setup, to check code correctness
    
    # Return value is whether to skip the turn or not
    return False
