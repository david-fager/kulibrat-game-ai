class Player:
    score = 0
    onHand = 5

    def __init__(self, name, isAI=False):
        self.name = name
        self.isAI = isAI

    def toString(self):
        name = self.name + (" (AI)" if self.isAI else "")
        return " ".join([name, "-score:", str(self.score), "-onHand:", str(self.onHand)])


class Match:
    turnNumber = 0
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    players = []

    def __init__(self, emptySymbol=" ", players=None):
        self.emptySymbol = emptySymbol
        self.players = [Player("Player1"), Player("Player2")] if players is None else players

    def current(self):
        cpy = self.players.copy()
        cpy.reverse()
        return cpy[self.turnNumber % 2]

    def getPlayerInfoString(self, index):
        player = self.players[index]
        return "[TURN] " + player.toString() if player == self.current() else player.toString()
