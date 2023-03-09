import numpy as np
import gameManager


def checkMove(match, move, performMove=False):
    abc = ['a', 'b', 'c']

    # print(move)

    fromX = move[0]
    fromY = move[1]

    opponent = match.getCurrentOpponent()
    startRow = len(match.board) - 1 if match.getCurrentPlayer() == match.players[0] else 0
    endRow = 3 - startRow

    # Check for invalid moves
    for m in move:
        if(not isinstance(m, str)):
            if(m > len(match.board)-1 or m < 0):
                raise Exception("You cannot move to a position outside the board")
    
    # If a new piece is placed on the board
    if len(move) == 2:
        if match.getCurrentPlayer().onBoard >= 4:
            raise Exception("You can have a maximum of 4 pieces on the board at a time")

        if not fromY == startRow:
            raise Exception("You must place new pieces in row {0}".format(startRow + 1))

        if not match.board[fromY][fromX] == match.vacant:
            raise Exception("This slot is already occupied")

        if 0 <= fromX <= 2 and fromY == startRow:
            if performMove:
                match.board[fromY][fromX] = match.getCurrentPlayer().piece
                match.getCurrentPlayer().onBoard += 1
                return match
            return True

    # If a piece is moved
    else:
        moveAllowed = False

        if not match.board[fromY][fromX] == match.getCurrentPlayer().piece:
            raise Exception("You do not have a piece at {0}{1}".format(abc[fromX], fromY + 1))

        # if player wants to move a piece out of the board (score a point)
        if move[2] == "e":
            # if the piece is not at the end row, then check that they can jump all rows
            if not fromY == endRow:
                moveAllowed = _checkJumpPath(match, opponent, fromX, fromY, endRow, False)

            # if they are at the end row, then allow to move
            if fromY == endRow or moveAllowed:
                if performMove:
                    match.getCurrentPlayer().score += 1
                    match.getCurrentPlayer().onBoard -= 1
                    match.board[fromY][fromX] = match.vacant
                    return match
                return True

            if not moveAllowed:
                raise Exception("You cannot jump over vacant slots")

        toX = move[2]
        toY = move[3]

        # if player only moved vertically
        if fromX == toX:
            rowsMoved = np.abs(fromY - toY)

            # one vertical step means attack
            if rowsMoved == 1 and match.board[toY][toX] == opponent.piece:
                if performMove:
                    opponent.onBoard -= 1

                moveAllowed = True

            # multiple vertical steps means jump
            elif rowsMoved >= 2 and match.board[toY][toX] == match.vacant:
                moveAllowed = _checkJumpPath(match, opponent, fromX, fromY, toY, True)

            else:
                raise Exception("You cannot move vertically unless you are attacking or jumping")

        # if player moved one step diagonally
        if np.abs(fromX - toX) == 1 and np.abs(fromY - toY) == 1:
            if not match.board[toY][toX] == match.vacant:
                raise Exception("You cannot move a piece diagonally onto another piece")

            moveAllowed = True

        if moveAllowed:
            if performMove:
                match.board[fromY][fromX] = match.vacant
                match.board[toY][toX] = match.getCurrentPlayer().piece
                return match
            return True

    raise Exception("Unexpected move error")


def _checkJumpPath(match, opponent, fromX, fromY, toY, land):
    moveAllowed = False

    goingDown = fromY - toY < 0
    direction = 1 if goingDown else -1
    step = fromY
    towards = toY + (-1 * direction) if land else toY

    while step != towards:
        step += direction
        moveAllowed = match.board[step][fromX] == opponent.piece

        if not moveAllowed:
            break

    return moveAllowed and (match.board[toY][fromX] == match.vacant if land else True)
