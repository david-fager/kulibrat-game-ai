import numpy as np

import classes


def customMatch():
    playerCount = 2
    players = []

    matchVacancy = askLoop("How should a vacant board slot look? (single char): ")
    matchLength = askLoop("The score to win the game (3-30): ", np.arange(3, 31).astype(str))

    for i in range(playerCount):
        name = input("[Player {0}] name: ".format(i + 1))
        piece = askLoop("[{0}] piece character (single char): ".format(name))
        yn = askLoop("[{0}] is computer? (y/n): ".format(name), ["y", "n"])
        players.append(classes.Player(name, piece, yn == "y"))

    return classes.Match(matchVacancy if matchVacancy else " ", players, int(matchLength))


def askLoop(prompt, condition=None):
    while True:
        response = input(prompt)

        if len(response) == 1 and (response in condition if condition is not None else True):
            return response
