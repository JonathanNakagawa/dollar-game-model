class Player:
    def __init__(self, pos):
        self.active = True
        self.value = 3
        self.pos = pos
        self.wasChanged = 0

    def getState(self):
        return self.active

    def getValue(self):
        return self.value

    def getPos(self):
        return self.pos

    def getWasChanged(self):
        curVal = self.wasChanged
        self.wasChanged = 0
        return curVal

    def changeValue(self, change):
        global numActive
        new = self.value + change
        if(new <= 0):
            self.active = False
            self.wasChanged = -1
        elif self.value == 0 and new > 0:
            self.active = True
            self.wasChanged = 1
        else:
            self.wasChanged = 0
        self.value = new

