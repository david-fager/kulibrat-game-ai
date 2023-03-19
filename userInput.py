def getUserMove(match):
    try:
        move = input("[{0}] Perform a move (e.g. 'a4' or 'c3-c1'): ".format(match.getCurrentPlayer().name)).split("-")
        if move[0] == "override":
            return ["override"]
    except KeyboardInterrupt:
        exit()

    if not 1 <= len(move) <= 2:
        raise Exception("Move length error: make sure that input is of the format 'a1' or 'a1-a2'")

    interpretedMove = []
    cols = {'a': 0, 'b': 1, 'c': 2}
    for m in move:
        # move a piece out of the board (score a point)
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


def askLoop(prompt, condition=None):
    # keep asking till the response matches criteria
    while True:
        response = input(prompt)

        # either the response match the condition, or it must be 1 char in length
        if (response in condition if condition is not None else False) or len(response) == 1:
            return response
