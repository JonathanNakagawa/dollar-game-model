from main import Game

class Analysis:
    def __init__(self, trialNum, playerNum):
        self.playerWins = [0 for i in range(playerNum)]
        self.trialCount = trialNum
        self.numTurns = 0
        self.playerCount = playerNum

    def getNumTurns(self):
        return self.numTurns

    def playGame(self):
        for i in range(0, self.trialCount):
            curGame = Game(self.playerCount)
            curGame.playGame()
            self.playerWins[curGame.winnerPos] += 1

    def displayPercentages(self):
        print([i/self.trialCount for i in self.playerWins])

    #def blackScholes(self):



def main():
    a = Analysis(1000000, 9)
    a.playGame()
    a.displayPercentages()


if __name__ == "__main__":
    main()
