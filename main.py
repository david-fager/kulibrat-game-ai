import classes
import computer
import gameManager
import logic
import userInput

customizeMatch = False


def gameLoop():
    match = gameManager.customMatch() if customizeMatch else classes.Match()

    while True:
        match.turnNumber += 1

        while True:
            try:
                gameManager.printGame(match)

                if not gameManager.canMoveAnything(match):
                    break

                move = computer.getAIMove(match) if match.current().isAI else userInput.getUserMove(match)

                if move[0] == "override":
                    skipTurn = gameManager.overrideMatch(match)
                    if skipTurn:
                        break

                    continue

                if logic.checkMove(match, move, True):
                    break

            except Exception as e:
                print("\t[RESULT] " + e.__str__())

        if match.current().score >= match.playTo:
            gameManager.printGame(match)
            print("{0} has won the game".format(match.current().name))
            break


gameLoop()
