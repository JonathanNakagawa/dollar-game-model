from gamefuncs import rollNum
from gamefuncs import getLeftPos
from gamefuncs import getRightPos
from gamefuncs import rollDie
from player import Player


class Game:
    def __init__(self, plyrCount):
        self.plyrCount = plyrCount
        self.numActive = plyrCount
        self.turnCount = 0
        self.winnerPos = 0
        self.table = self.genTable()

    def genTable(self):
        table = []
        for x in range(0, self.plyrCount):
            temp = Player(x)
            table.append(temp)
        return table

    def playTurn(self, pos):
        curPlayer = self.table[pos]
        curPlayer.wasChanged = 0
        if not curPlayer.getState():
            return
        rollCount = rollNum(curPlayer)
        for i in range(0, rollCount):
            result = rollDie()
            if result == 0:
                curPlayer.changeValue(-1)
                self.table[getLeftPos(pos, self.plyrCount)].changeValue(1)
                self.numActive += self.table[getLeftPos(pos, self.plyrCount)].getWasChanged()
            elif result == 1:
                curPlayer.changeValue(-1)
                self.table[getRightPos(pos, self.plyrCount)].changeValue(1)
                self.numActive += self.table[getRightPos(pos, self.plyrCount)].getWasChanged()
            elif result == 2:
                curPlayer.changeValue(-1)
            self.numActive += curPlayer.getWasChanged()


    def playGame(self):
        pos = 0
        while self.numActive != 1:
            self.playTurn(pos)
            pos = getRightPos(pos, self.plyrCount)


