import numpy as np

import classes
import config
import userInput


def printGame(match):
    if config.AI_TESTING and config.SUPPRESS_PRINT:
        player = match.getCurrentPlayer()
        printMsg("{0} ({1}/{2})".format(player.name, player.score, match.playTo), True)
        return

    printMsg("\nMATCH TO {0} POINTS".format(match.playTo))
    printMsg(match.getPlayerInfoString(1))
    printBoard(match)
    printMsg(match.getPlayerInfoString(0) + "\n")


def printBoard(match):
    rowBorder = ["+", "-", "-", "-", "-", "-", "+"]
    msg = " ".join(rowBorder) + "\n"
    for i, row in enumerate(match.board):
        msg += "| {} | {}\n".format(" | ".join(row), i + 1)
        msg += " ".join(rowBorder) + "\n"
    msg += "  {}  ".format("   ".join(["a", "b", "c"]))
    printMsg(msg)


def printEndGame(match):
    printMsg("\nFinal board:")
    printBoard(match)
    msg = "\n"
    msg += "WINNER: {0}".format(match.getCurrentPlayer().toString())
    msg += "VERSUS: {0}".format(match.getCurrentOpponent().toString())
    printMsg(msg)


def printMsg(msg, neverSuppress=False):
    if neverSuppress or not config.SUPPRESS_PRINT:
        print(msg)


def createMatch(preMatch):
    if preMatch:
        return preMatch

    if config.AI_TESTING:
        players = [classes.Player("AI 1", "X", True),
                   classes.Player("AI 2", "O", True)]
        return classes.Match(" ", players, 10)

    matchVacancy = userInput.askLoop("How should a vacant board slot look? (single char): ")
    matchLength = userInput.askLoop("The score to win the game (3-30): ", np.arange(3, 31).astype(str))

    players = []
    for i in range(2):
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
