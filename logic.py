import numpy as np


def getUserMove(match):
    try:
        move = input("[{0}] Perform a move (e.g. 'a1' or 'a1-a2'): ".format(match.current().name)).split("-")
    except KeyboardInterrupt:
        exit()

    if not 1 <= len(move) <= 2:
        raise Exception("Move length error: make sure that input is of the format 'a1' or 'a1-a2'")

    interpretedMove = []
    cols = {'a': 0, 'b': 1, 'c': 2}
    for m in move:
        if len(interpretedMove) == 2 and m == "e":
            interpretedMove.append(m)
            continue

        char = m[0]
        num = int(m[1])

        if char not in cols.keys() or num not in range(1, 5):
            raise Exception("Move interpretation error: make sure to write a, b or c and numbers 1-4")

        interpretedMove.append(cols[char])
        interpretedMove.append(num - 1)

    if 2 <= len(interpretedMove) <= 4:
        return interpretedMove

    raise Exception("Unexpected input error")


def checkMove(match, move, perform=False):
    abc = ['a', 'b', 'c']

    fromX = move[0]
    fromY = move[1]

    opponent = match.players[1] if match.current() == match.players[0] else match.players[0]
    startRow = len(match.board) - 1 if match.current() == match.players[0] else 0
    endRow = 3 - startRow

    if len(move) == 2:
        if match.current().onBoard >= 4:
            raise Exception("You can have a maximum of 4 pieces on the board at a time")

        if not fromY == startRow:
            raise Exception("You must place new pieces in row {0}".format(startRow + 1))

        if not match.board[fromY][fromX] == match.vacant:
            raise Exception("This slot is already occupied")

        if 0 <= fromX <= 2 and fromY == startRow:
            if perform:
                match.board[fromY][fromX] = match.current().piece
                match.current().onBoard += 1

            return True

    else:
        moveAllowed = False

        if not match.board[fromY][fromX] == match.current().piece:
            raise Exception("You do not have a piece at {0}{1}".format(abc[fromY], fromX + 1))

        # if player wants to move a piece to the end of the board (score a point)
        if move[2] == "e":
            # if the piece is not at the end row, then check that they can jump all rows
            if not fromY == endRow:
                moveAllowed = _checkJumpPath(match, opponent, fromX, fromY, endRow, False)

            # if they are at the end row, then allow to move
            if fromY == endRow or moveAllowed:
                if perform:
                    match.current().score += 1
                    match.current().onBoard -= 1
                    match.board[fromY][fromX] = match.vacant

                return True

        toX = move[2]
        toY = move[3]

        # if player only moved vertically
        if fromX == toX:
            rowsMoved = np.abs(fromY - toY)

            # one vertical step means attack
            if rowsMoved == 1 and match.board[toY][toX] == opponent.piece:
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
            if perform:
                match.board[fromY][fromX] = match.vacant
                match.board[toY][toX] = match.current().piece

            return True

    raise Exception("Unexpected move error")


def _checkJumpPath(match, opponent, fromX, fromY, toY, include):
    moveAllowed = False

    steps = np.abs(fromY - toY) if not include else np.abs(fromY - toY) + 1
    for i in range(1, steps + 1):
        step = fromY + i if fromY - toY < 0 else fromY - i
        moveAllowed = match.board[step][fromX] == opponent.piece
        print(step)
        if not moveAllowed:
            break

    return moveAllowed
