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
