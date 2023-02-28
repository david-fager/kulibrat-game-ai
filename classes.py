class Player:
    score = 0
    onHand = 5

    def __init__(self, name, isAI=False):
        self.name = name
        self.isAI = isAI


class Match:
    turnNumber = 1
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    players = []

    def __init__(self, emptySymbol=" ", p1=Player("Player1"), p2=Player("Player2")):
        self.emptySymbol = emptySymbol
        self.players.append(p2)
        self.players.append(p1)

    def current(self):
        return self.players[self.turnNumber % 2]
