import time


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
