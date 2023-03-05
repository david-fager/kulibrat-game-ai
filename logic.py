import numpy as np

import computer


def getAndCheckMove(match):
    if match.current().isAI:
        move = computer.getAIMove(match)
    else:
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

        char = m[0]
        num = int(m[1])

        if char not in cols.keys() or num not in range(1, 5):
            raise Exception("Move interpretation error: make sure to write a, b or c and numbers 1-4")

        interpretedMove.append(cols[char])
        interpretedMove.append(num - 1)

    if 2 <= len(interpretedMove) <= 4:
        return interpretedMove

    raise Exception("Unexpected input error")


def performMove(match, move):
    opponent = match.players[1] if match.current() == match.players[0] else match.players[0]
    abc = ['a', 'b', 'c']
    startRow = len(match.board) - 1 if match.current() == match.players[0] else 0
    endRow = 4 - startRow

    if len(move) == 2:
        if match.current().onBoard >= 4:
            raise Exception("You can have a maximum of 4 pieces on the board at a time")

        if not move[1] == startRow:
            raise Exception("You must place new pieces in row {0}".format(startRow + 1))

        if match.board[move[1]][move[0]] == match.current().piece:
            raise Exception("You already occupy this board slot")

        if 0 <= move[0] <= 2 and move[1] == startRow:
            match.board[move[1]][move[0]] = match.current().piece
            match.current().onBoard += 1
            return True

    else:
        moveAllowed = False

        if not match.board[move[1]][move[0]] == match.current().piece:
            raise Exception("You do not have a piece at {0}{1}".format(abc[move[0]], move[1] + 1))

        if move[2] == "e":
            pass

        # if player only moved vertically
        if move[0] == move[2]:
            rowsMoved = np.abs(move[1] - move[3])

            # one vertical step means attack
            if rowsMoved == 1 and match.board[move[3]][move[2]] == opponent.piece:
                opponent.onBoard -= 1
                moveAllowed = True

            # multiple vertical steps means jump
            elif rowsMoved >= 2 and match.board[move[3]][move[2]] == match.vacant:
                for i in range(1, np.abs(move[3]) + 1):
                    step = move[1] + i if move[1] - move[3] < 0 else move[1] - i
                    moveAllowed = match.board[step][move[0]] == opponent.piece
                    if not moveAllowed:
                        break

            else:
                raise Exception("You cannot move vertically unless you are attacking or jumping")

        # if player moved one step diagonally
        if np.abs(move[0] - move[2]) == 1 and np.abs(move[1] - move[3]):
            if not match.board[move[3]][move[2]] == match.vacant:
                raise Exception("You cannot move a piece diagonally onto the opponent's piece")

            moveAllowed = True

        if moveAllowed:
            match.board[move[1]][move[0]] = match.vacant
            match.board[move[3]][move[2]] = match.current().piece
            return True

    raise Exception("Unexpected move error")
