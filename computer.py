import time

# BFS (FIFO queue)
frontier = []
# set of visited states
expandedNodes = {}

def graphSearch(state):
    # clear frontier and expandedNodes
    frontier.clear()
    expandedNodes.clear()

    # add initial state to frontier
    addToFrontier(match.board)

    while True:
        if frontier.isEmpty():
            raise Exception("No solution found")

        state = frontier.rear()
        frontier.dequeue()
        expandedNodes.add(state)

        if(isGoal(state)):
            return state

        for action in getAvaliableMoves(state):
            childState = getChildState(state, action)

            if not childState in expandedNodes and not childState in frontier:
                addToFrontier(childState)

def getChildState(state, action):
    # TODO
    return None

def isGoal(state):
    # TODO 
    return None

def getAvaliableMoves(state):
    state = match.board

    # for i, row in enumerate(match.board):
    #     print(row)
    #     for j, col in enumerate(row):
    #         print(col)
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
