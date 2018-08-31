import random


class Player:
    def __init__(self, pos):
        self.active = True
        self.value = 3
        self.pos = pos

    def retState(self):
        return self.active

    def retValue(self):
        return self.value

    def retPos(self):
        return self.pos

    def changeValue(self, change):
        new = self.value + change
        if(new <= 0):
            self.value = 0
            self.state = False
        else:
            self.value = new
            self.state = True


def genTable(num):
    table = []
    for x in range(0,num):
        temp = Player(x)
        table.append(temp)
        print("test")
    return table


def playTurn(table, pos):
    curPlayer = table[pos]
    if not curPlayer.retState():
        return


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
    playerCount = input("How many players? ")
    playerCount = int(playerCount)
    table = genTable(playerCount)
    numActive = playerCount
    pos = 0
    while numActive != 1:
        playTurn(table, pos)
        if pos == playerCount - 1:
            pos = 0
        else:
            pos += 1


if __name__ == "__main__":
    main()