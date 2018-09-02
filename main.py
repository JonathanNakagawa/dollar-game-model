from gamefuncs import rollNum
from gamefuncs import getLeftPos
from gamefuncs import getRightPos
from gamefuncs import rollDie
from player import Player

numActive = 0


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


if __name__ == "__main__":
    main()