import time

def miniMax(state, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or isGoal(state):
        return evaluationOfState(state)

    if maximizingPlayer:
        maxEval = float('-inf')
        for action in getAvaliableMoves(state):
            childState = getChildState(state, action)
            eval = miniMax(childState, depth-1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        for action in getAvaliableMoves(state):
            childState = getChildState(state, action)
            eval = miniMax(childState, depth-1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

def evaluationOfState(state):
    # TODO
    return None

def getChildState(state, action):
    # TODO
    return None

def isGoal(state):
    if(getPlayerOfCurrentTurn(state).score >= state.playTo):
        return True
    return False

def getAvaliableMoves(state):
    for i, row in enumerate(match.board):
        for j, peice in enumerate(row):
            if(piece == state.getPlayerOfCurrentTurn().piece):
                # Check for avaliable moves
                print(piece)
    return None

def getAIMove(match):
    try:
        print("\t[AI] thinking ...")
        time.sleep(1)
    except KeyboardInterrupt:
        exit()

    # steps:
    # 1. find possible move
    # 2. check it with logic.checkMove(match, move)
    # 3. return move as array, either:
    # [newPieceX, newPieceY] places a new piece
    # [fromX, fromY, toX, toY] moves a piece from -> to
    # [fromX, fromY, "e"] moves a piece from somewhere to the end (scoring a point)
    # e.g. return [1, 0, "e"] will move a piece from upper middle to the end (if logic.checkMove() approves of it)

    raise Exception("Not implemented yet")
