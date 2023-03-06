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
        # End game if conditions are met
        # TODO: End game if no player can make a move. 
        if match.getPlayerOfCurrentTurn().score >= match.playTo:
            gameManager.printGame(match)
            print("{0} has won the game".format(match.getPlayerOfCurrentTurn().name))
            break

        try:
            gameManager.printGame(match)

            # Check if player can make a valid move
            if not gameManager.canMoveAnything(match):
                continue

            move = computer.getAIMove(match) if match.getPlayerOfCurrentTurn().isAI else userInput.getUserMove(match)

            # Override match for custom position
            if move[0] == "override":
                skipTurn = gameManager.overrideMatch(match)
                if skipTurn:
                    continue
                match.turnNumber -= 1
                continue

            if logic.checkMove(match, move, True):
                continue

        except Exception as e:
            print("\t[RESULT] " + e.__str__())
            # Retake turn
            match.turnNumber -= 1

gameLoop()
