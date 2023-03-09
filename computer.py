import logic
import copy

bestMove = None
DEPTH = 1

def miniMax(match, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or isGoal(match):
        return evaluationOfGame(match)

    if maximizingPlayer:
        maxEval = float('-inf')
        print(getAvaliableMoves(match))
        for move in getAvaliableMoves(match):
            performAction(match, move)
            eval = miniMax(match, depth-1, alpha, beta, False)
            if(eval > maxEval and depth == DEPTH):
                global bestMove
                bestMove = move
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        print(getAvaliableMoves(match))
        for move in getAvaliableMoves(match):
            performAction(match, move)
            eval = miniMax(match, depth-1, alpha, beta, True)
            if(eval < minEval and depth == DEPTH):
                bestMove = move
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

def evaluationOfGame(match):
    eval = 0
    playerIndex = 0 if match.getCurrentPlayer() == match.players[0] else 1

    # Check if the game is over
    if(isGoal(match)):
        if(playerIndex == 0):
            return float('inf')
        else:
            return float('-inf')
    
    # Check if the game is a draw
    # TODO
    # return 0

    # Evaluation of board
    for i, row in enumerate(match.board):
        advanceGain = len(match.board) - i if playerIndex == 0 else i + 1
        for j, piece in enumerate(row):

            # Evaluation of position
            if(piece == match.players[playerIndex].piece):
                eval += 10 + advanceGain
            else:
                eval -= 10 + advanceGain

            # Evaluation of number of pieces
            if(piece == match.players[playerIndex].piece):
                eval += 10
            else:
                eval -= 10
    
    # Evaluation of score
    if(playerIndex == 0):
        eval += match.players[playerIndex].score * 50
        eval -= match.players[1 - playerIndex].score * 50
    else:
        eval -= match.players[playerIndex].score * 50
        eval += match.players[1 - playerIndex].score * 50

    return eval

def performAction(match, move):
    logic.checkMove(match, move, True)
    # match.turnNumber += 1

def isGoal(match):
    if(match.getCurrentPlayer().score >= match.playTo):
        return True
    return False

def getAvaliableMoves(match):
    legalMoves = []
    rowMovement = -1 if match.getCurrentPlayer() == match.players[0] else 1
    startRow = len(match.board)-1 if rowMovement == -1 else 0

    # [0, 0] is top left corner
    # [col, row]

    # Place piece
    for i in range(3):
        try:
            if(logic.checkMove(match, [i, startRow])):
                legalMoves.append([i, startRow])
        except:
            pass
    
    # Move piece
    for i, row in enumerate(match.board):
        for j, piece in enumerate(row):
            if(piece == match.getCurrentPlayer().piece):
                try:
                    # Attack move
                    if(logic.checkMove(match, [j, i, j, i+rowMovement])):
                        legalMoves.append([j, i, j, i+rowMovement])
                except:
                    pass

                try:
                    # Move diagonally to the right
                    if(logic.checkMove(match, [j, i, j+1, i+rowMovement])):
                        legalMoves.append([j, i, j+1, i+rowMovement])
                except:
                    pass

                try:
                    # Move diagonally to the left
                    if(logic.checkMove(match, [j, i, j-1, i+rowMovement])):
                        legalMoves.append([j, i, j-1, i+rowMovement])
                except:
                    pass

                # Jump move
                for k in range(2, 4):
                    try:
                        if(logic.checkMove(match, [j, i, j+k, i+rowMovement*k])):
                            legalMoves.append([j, i, j+k, i+rowMovement*k])
                    except:
                        pass
                
                # Score a point
                try:
                    if(logic.checkMove(match, [j, i, "e"])):
                        legalMoves.append([j, i, "e"])
                except:
                    pass
    return legalMoves

def getAIMove(match):
    try:
        print("\t[AI] thinking ...")
        cpyOfMatch = copy.deepcopy(match)

        # player at index 0 will be the maximizing player
        maxOrMinPlayer = True if match.getCurrentPlayer() == match.players[0] else False
        miniMax(cpyOfMatch, DEPTH, float('-inf'), float('inf'), maxOrMinPlayer)
        print(bestMove)
        return bestMove
    except KeyboardInterrupt:
        exit()

    # steps:
    # 1. find possible move
    # 2. check it with logic.logic.checkMove(match, move)
    # 3. return move as array, either:
    # [newPieceX, newPieceY] places a new piece
    # [fromX, fromY, toX, toY] moves a piece from -> to
    # [fromX, fromY, "e"] moves a piece from somewhere to the end (scoring a point)
    # e.g. return [1, 0, "e"] will move a piece from upper middle to the end (if logic.logic.checkMove() approves of it)

    raise Exception("Not implemented yet")
