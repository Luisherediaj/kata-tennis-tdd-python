class Player:
    scores = ["0", "15", "30", "40"]
    def __init__(self, score = 0):
        self.score = score

    def getScore(self):
        return self.scores[self-score]

    def winPoint(self):
        self.score+=1