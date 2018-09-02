import random

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