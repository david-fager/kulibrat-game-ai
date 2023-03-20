import classes
import computer
import config
import gameManager as gman
import logic
import userInput

# defining the configuration
config.CUSTOM_MATCH = False
config.AI_TESTING = False
config.DEPTH_TESTING = True
config.SUPPRESS_PRINT = False


def gameLoop(preMatch=None):
    preMatch = preMatch if config.AI_TESTING or config.DEPTH_TESTING else classes.Match()
    match = gman.createMatch(None if config.CUSTOM_MATCH else preMatch)

    while True:
        try:
            gman.printGame(match)

            # Check if current player can move, if not check opponent, neither then break
            if not computer.getAvailableMoves(match):
                gman.printMsg("\t{0} has no available moves - skipping turn".format(match.getCurrentPlayer().name))
                match.turnNumber += 1
                if not computer.getAvailableMoves(match):
                    name = match.getCurrentPlayer().name
                    gman.printMsg("\t{0} also has no available moves".format(name))
                    gman.printMsg("\t{0} has lost the game, due to inducing a deadlock".format(name))
                    break
                continue

            move = computer.getAIMove(match) if match.getCurrentPlayer().isAI else userInput.getUserMove(match)

            # Override match for custom position
            if move[0] == "override":
                skipTurn = gman.overrideMatch(match)
                if skipTurn:
                    match.turnNumber += 1
                continue

            logic.checkMove(match, move, True)

            # End game if conditions are met
            if match.getCurrentPlayer().score >= match.playTo:
                gman.printEndGame(match)
                break

            match.turnNumber += 1

        except Exception as e:
            gman.printMsg("\t[RESULT] " + e.__str__(), True)

    return match


def testLoop():
    config.SUPPRESS_PRINT = config.DEPTH_TESTING
    config.AI_SLEEP_TIME = 0

    depths = [3, 4, 5, 6, 7, 8, 9, 10]
    results = dict.fromkeys(depths, "")

    for i, testDepth in enumerate(depths):
        for compDepth in depths[i + 1:]:
            print("MATCHING DEPTH {0} AGAINST {1}".format(testDepth, compDepth))

            players = [classes.Player("AI 1", "X", True, testDepth),
                       classes.Player("AI 2", "O", True, compDepth)]
            players = gameLoop(classes.Match(" ", players, 30)).players

            score1 = players[0].score
            score2 = players[1].score

            if score1 > score2:
                results[testDepth] += "{0} (vs. {1}), ".format((score1 - score2), compDepth)
            elif score2 > score1:
                results[compDepth] += "{0} (vs. {1}), ".format((score2 - score1), testDepth)
            else:
                results[testDepth] += "tied (vs. {0}), ".format(compDepth)
                results[compDepth] += "tied (vs. {0}), ".format(testDepth)

            print("\tTEST RESULTS:")
            for k, v in results.items():
                print("\tDEPTH {0} LEAPS: {1}".format(str(k).zfill(2), v))


gameLoop() if not config.DEPTH_TESTING else testLoop()
