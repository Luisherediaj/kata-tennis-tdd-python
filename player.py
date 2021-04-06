class Player:
    scores = ["0", "15", "30", "40", "Winner"]
    def __init__(self, score = 0):
        self.score = score

    def isWinner(self):
        return self.score == 4

    def winPoint(self, other = None):
        if other == None:
            self.score+=1
            return    

        if self.getScore() == "40" and other.getScore() != "40":
            self.score += 2
        else:
            self.score+=1