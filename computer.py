import time
import logic

bestAction = None
DEPTH = 7

def miniMax(match, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or isGoal(match):
        return evaluationOfBoard(match.board)

    if maximizingPlayer:
        maxEval = float('-inf')
        for action in getAvaliableMoves(match):
            child = getChildmatch(match, action)
            eval = miniMax(child, depth-1, alpha, beta, False)
            if(eval > maxEval and depth == DEPTH):
                bestAction = action
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        for action in getAvaliableMoves(match):
            child = getChildmatch(match, action)
            eval = miniMax(child, depth-1, alpha, beta, True)
            if(eval < minEval and depth == DEPTH):
                bestAction = action
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

def evaluationOfBoard(board):
    # TODO
    return None

def getChildmatch(match, move):
    return logic.checkMove(match, move, True)

def isGoal(match):
    if(getPlayerOfCurrentTurn(match).score >= match.playTo):
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
        if(logic.checkMove(match, [i, startRow])):
            legalMoves.append([i, startRow])
    
    # Move piece
    for i, row in enumerate(match.board):
        for j, peice in enumerate(row):
            if(piece == match.getPlayerOfCurrentTurn().piece):
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
                for k in range(2, 3):
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
        miniMax(match, DEPTH, float('-inf'), float('inf'), True) # Not sure who is the maximizing player
        return bestAction
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
