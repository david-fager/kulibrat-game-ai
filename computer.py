import random
import time

import logic
import copy

actualCurrentIdx = None
actualOpponentIdx = None

bestMove = None
DEPTH = 7
noPositions = 0


def isGoal(match):
    return match.getCurrentPlayer().score >= match.playTo


def miniMax(match, depth, alpha, beta, maximize):
    global bestMove, noPositions
    noPositions += 1

    # if depth limit of search tree reached or the node has reached the winning score, then evaluate board
    if depth == 0 or isGoal(match):
        return evaluationOfGame(match)

    endEval = float('-inf') if maximize else float('inf')
    availableMoves = getAvailableMoves(match)

    # Skip turn if no available moves
    if not availableMoves:
        return miniMax(match, depth - 1, alpha, beta, not maximize)

    for move in availableMoves:
        cpyMatch = copy.deepcopy(match)

        # actually perform the move in this "pretend" match
        logic.checkMove(cpyMatch, move, True)
        cpyMatch.turnNumber += 1

        # get evaluation of this move's subtree
        eval = miniMax(cpyMatch, depth - 1, alpha, beta, not maximize)

        # when maximizing the highest possible eval result for all subtrees is returned
        if maximize:
            if eval > endEval and depth == DEPTH:
                bestMove = move
            endEval = max(endEval, eval)
            alpha = max(alpha, eval)

        # when minimizing the lowest possible eval result for all subtrees is returned
        else:
            if eval < endEval and depth == DEPTH:
                bestMove = move
            endEval = min(endEval, eval)
            beta = min(beta, eval)

        if beta <= alpha:
            break

    return endEval


def evaluationOfGame(match):
    global actualCurrentIdx, actualOpponentIdx
    isPretenderActual = match.getCurrentPlayer() == match.players[actualCurrentIdx]
    isPretenderAtTop = match.getCurrentPlayer() == match.players[1]
    opponentEnd = len(match.board) if isPretenderAtTop else 0

    eval = 0

    # If current node means someone wins, then for AI return great evaluation, for opponent return bad evaluation
    if isGoal(match):
        return 999999 if isPretenderActual else -999999

    # TODO: check if the game is deadlocked

    # Evaluation of board
    for i, row in enumerate(match.board):
        # the greater the distance from opponents end, the greater the consideration for the looked at move
        advanceGain = len(match.board) - i if isPretenderAtTop else i + 1
        scoreGain = 10 if i == opponentEnd else 0

        for j, piece in enumerate(row):

            # promote for every piece on the board, and promote the ones farther away more (with the adv. gain)
            if piece == match.players[actualCurrentIdx].piece:
                eval += 10 + advanceGain + scoreGain

            # demote eval for every opponent piece on board
            if piece == match.players[actualOpponentIdx].piece:
                eval -= 10 + advanceGain + scoreGain

    # promote moves leading to this board's score - demote the higher the opponent's score is
    eval += match.players[actualCurrentIdx].score * 50
    eval -= match.players[actualOpponentIdx].score * 50

    return eval


def getAvailableMoves(match):
    legalMoves = []
    rowMovement = -1 if match.getCurrentPlayer() == match.players[0] else 1
    startRow = len(match.board) - 1 if rowMovement == -1 else 0

    # [0, 0] is top left corner
    # [col, row]

    # Place piece
    for i in range(3):
        try:
            if (logic.checkMove(match, [i, startRow])):
                legalMoves.append([i, startRow])
        except:
            pass

    # Move piece
    for i, row in enumerate(match.board):
        for j, piece in enumerate(row):
            if (piece == match.getCurrentPlayer().piece):
                try:
                    # Attack move
                    if (logic.checkMove(match, [j, i, j, i + rowMovement])):
                        legalMoves.append([j, i, j, i + rowMovement])
                except:
                    pass

                try:
                    # Move diagonally to the right
                    if (logic.checkMove(match, [j, i, j + 1, i + rowMovement])):
                        legalMoves.append([j, i, j + 1, i + rowMovement])
                except:
                    pass

                try:
                    # Move diagonally to the left
                    if (logic.checkMove(match, [j, i, j - 1, i + rowMovement])):
                        legalMoves.append([j, i, j - 1, i + rowMovement])
                except:
                    pass

                # Jump move
                for k in range(2, 4):
                    try:
                        if (logic.checkMove(match, [j, i, j, i + rowMovement * k])):
                            legalMoves.append([j, i, j, i + rowMovement * k])
                    except:
                        pass

                # Score a point
                try:
                    if (logic.checkMove(match, [j, i, "e"])):
                        legalMoves.append([j, i, "e"])
                except:
                    pass

    return legalMoves


def getAIMove(match):
    global DEPTH, actualCurrentIdx, actualOpponentIdx
    actualCurrentIdx = 0 if match.getCurrentPlayer() == match.players[0] else 1
    actualOpponentIdx = 1 - actualCurrentIdx

    depthRandomizer = 0
    if random.randint(0, 99) < 5:
        depthRandomizer = 1
    DEPTH = match.getCurrentPlayer().aiDepth + depthRandomizer

    try:
        print("\tThinking (depth {0}) ...".format(DEPTH))
        time.sleep(.5)  # gives human & program time to see & print the game
        cpyOfMatch = copy.deepcopy(match)

        # player at index 0 will be the maximizing player
        miniMax(cpyOfMatch, DEPTH, float('-inf'), float('inf'), True)

        global noPositions
        print("\tCalculated {0} positions".format(str(noPositions)))
        noPositions = 0

        return bestMove

    except KeyboardInterrupt:
        exit()
