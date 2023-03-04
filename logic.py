import computer


def getAndCheckMove(match):
    if match.current().isAI:
        move = computer.getAIMove(match)
    else:
        move = input("[{0}] Perform a move (e.g. 'a1' or 'a1-a2'): ".format(match.current().name)).split("-")

    if not 1 <= len(move) <= 2:
        return None, "Move length error: make sure that input is of the format 'a1' or 'a1-a2'"

    interpretedMove = []
    cols = {'a': 0, 'b': 1, 'c': 2}
    for m in move:
        try:
            char = m[0]
            num = int(m[1])

            if char not in cols.keys() or num not in range(1, 5):
                raise Exception("Move interpretation error: make sure to write a, b or c and numbers 1-4")

            interpretedMove.append(cols[char])
            interpretedMove.append(num - 1)
        except Exception as e:
            return None, e

    if len(interpretedMove) == 2 or len(interpretedMove) == 4:
        return interpretedMove, ""

    return None, "Unexpected error"


def performMove(match, move):

    if len(move) == 2:
        if match.current().onBoard >= 4:
            return False, "A maximum of 4 pieces are allowed on the board at a time"

        allowedRow = len(match.board) - 1 if match.current() == match.players[0] else 0
        if not move[1] == allowedRow:
            return False, "A new piece must be placed in row {0}".format(allowedRow + 1)

        if match.board[move[1]][move[0]] == match.current().piece:
            return False, "You already occupy this board slot"

        match.board[move[1]][move[0]] = match.current().piece
        match.current().onBoard += 1
        return True, ""

    else:
        print("")

    return False, "Unexpected error"
