import random

numActive = 0

class Player:
    def __init__(self, pos):
        self.active = True
        self.value = 3
        self.pos = pos

    def getState(self):
        return self.active

    def getValue(self):
        return self.value

    def getPos(self):
        return self.pos

    def changeValue(self, change):
        global numActive
        new = self.value + change
        if(new <= 0):
            self.active = False
            numActive -= 1
        elif self.value == 0 & new > 0:
            self.active = True
            numActive += 1
        self.value = new



def genTable(num):
    table = []
    for x in range(0, num):
        temp = Player(x)
        table.append(temp)
    return table


def playTurn(table, pos):
    curPlayer = table[pos]
    tableSize = len(table)
    if not curPlayer.getState():
        return
    rollCount = rollNum(curPlayer)
    for i in range(0, rollCount):
        result = rollDie()
        if result == 0:
            table[getLeftPos(pos, tableSize)].changeValue(1)
        elif result == 1:
            table[getRightPos(pos, tableSize)].changeValue(1)
        elif result == 2:
            curPlayer.changeValue(-1)


def rollNum(curPlayer):
    if curPlayer.getValue() < 3:
        return curPlayer.getValue()
    return 3

def getLeftPos(curPos, tableSize):
    if curPos == 0:
        return tableSize - 1
    return curPos - 1


def getRightPos(curPos, tableSize):
    if curPos == tableSize - 1:
        return 0
    return curPos + 1


def rollDie():
    val = random.randint(1, 6)
    if val == 1:
        return 0  # represents left roll
    elif val == 2:
        return 1  # represents right roll
    elif val == 3 or val == 4:
        return 2  # represents center roll
    else:
        return 3  # represents blank roll


def main():
    global numActive
    playerCount = 8
    table = genTable(playerCount)
    numActive = playerCount
    pos = 0
    while numActive != 1:
        playTurn(table, pos)
        pos = getRightPos(pos, playerCount)
        print(numActive)
    print()

if __name__ == "__main__":
    main()