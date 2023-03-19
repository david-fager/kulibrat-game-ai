import classes
import computer
import gameManager
import logic
import userInput

customizeMatch = False
testingAI = False


def gameLoop():
    match = gameManager.customMatch(testingAI) if customizeMatch or testingAI else classes.Match()

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


gameLoop()
