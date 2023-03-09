class Player:
    score = 0
    onBoard = 0

    def __init__(self, name, piece, isAI=False):
        self.name = name
        self.piece = piece
        self.isAI = isAI

    def toString(self):
        name = self.name + (" (AI)" if self.isAI else "")
        return " ".join([name, "-piece:", self.piece, "-score:", str(self.score), "-onBoard:", str(self.onBoard)])


class Match:
    turnNumber = 1
    players = []

    def __init__(self, vacant=" ", players=None, playTo=5):
        self.vacant = vacant
        self.players = [Player("Player1", "O"), Player("Player2", "X", True)] if players is None else players
        self.playTo = playTo
        self.board = [[vacant] * 3 for i in range(4)]

    def getCurrentPlayer(self):
        return self.players[1 - (self.turnNumber % 2)]

    def getCurrentOpponent(self):
        return self.players[self.turnNumber % 2]

    def getPlayerInfoString(self, index):
        player = self.players[index]
        return "[TURN] " + player.toString() if player == self.getCurrentPlayer() else player.toString()
