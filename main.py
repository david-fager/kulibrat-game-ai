import classes
import computer
import gameManager
import logic
import userInput

customizeMatch = False
testingAI = False


def gameLoop(depthsTest=None):
    match = gameManager.customMatch(testingAI, depthsTest) if customizeMatch or testingAI else classes.Match()

    while True:
        try:
            gameManager.printGame(match, testingAI)

            # Check if current player can move, if not check opponent, neither then break
            if not computer.getAvailableMoves(match):
                print("{0} has no available moves - skipping turn".format(match.getCurrentPlayer().name))
                match.turnNumber += 1
                if not computer.getAvailableMoves(match):
                    print("{0} also has no available moves".format(match.getCurrentPlayer().name))
                    print("{0} has lost the game, due to inducing a deadlock".format(match.getCurrentPlayer().name))
                    break
                continue

            move = computer.getAIMove(match) if match.getCurrentPlayer().isAI else userInput.getUserMove(match)

            # Override match for custom position
            if move[0] == "override":
                skipTurn = gameManager.overrideMatch(match)
                if skipTurn:
                    match.turnNumber += 1
                continue

            logic.checkMove(match, move, True)

            # End game if conditions are met
            if match.getCurrentPlayer().score >= match.playTo:
                gameManager.printEndGame(match)
                break

            match.turnNumber += 1

        except Exception as e:
            print("\t[RESULT] " + e.__str__())

    return match


def testLoop():
    data = {}
    depths = [3, 4, 5, 6, 7, 8, 9, 10]
    for d in depths:
        data[d] = ""

    biggestScoreLeap = 0
    prevBestDepth = depths[0]

    for i, depth in enumerate(depths):
        if depth == depths[0]:
            continue

        print("\nSTARTING DEPTH TEST MATCH BETWEEN {0} and {1}".format(prevBestDepth, depth))
        players = gameLoop([prevBestDepth, depth]).players

        if players[0].score > players[1].score:
            leap = players[0].score - players[1].score
            data[prevBestDepth] += ("{0}, ".format(leap))

            if leap > biggestScoreLeap:
                biggestScoreLeap = leap
                prevBestDepth = depth
        else:
            leap = players[1].score - players[0].score
            data[depth] += ("{0}, ".format(leap))

            if leap > biggestScoreLeap:
                biggestScoreLeap = leap
                prevBestDepth = depth

    print("BEST DEPTH: {0} WITH BIGGEST LEAP OF: {1}".format(prevBestDepth, biggestScoreLeap))
    print("Complete test results - higher leaps are better:")
    for k, v in data.items():
        print("Depth {0} leaps: {1}".format(str(k), v))


gameLoop() if not (testingAI and False) else testLoop()  # set True to run the depth test loop
