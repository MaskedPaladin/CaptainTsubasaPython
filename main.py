import random, time, os, sys
from msvcrt import getch

class Player:
    def __init__(self, x, y, number, position, stamina, passe, dodge, shoot, intercept, entry, block):
        self.x = x
        self. y = y
        self.pos = (x, y)
        self.number = number
        self.position = position
        self.stamina = stamina
        self.passe = passe
        self.dodge = dodge
        self.shoot = shoot
        self.intercept = intercept
        self.entry = entry
        self.block = block
    def generate(position):
        if position == 'DEF':
            obj = Player(random.randint(1, 4),random.randint(1, 9), random.randint(0,9), 'DEF', random.randint(100,900), random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100))
        elif position == 'MF':
            obj = Player(random.randint(1, 4),random.randint(1, 9), random.randint(0,9), 'MF', random.randint(100,900), random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100))
        elif position == 'FW':
            obj = Player(random.randint(1, 4),random.randint(1, 9), random.randint(0,9), 'FW', random.randint(100,900), random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100))
        return obj
    def cpu_update(self):
        if self.x == 1:
            obj = Player(self.x+1, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
            return obj
        if self.x==9:
            obj = Player(self.x-1, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
            return obj
        if self.x != 9 or self.x != 1:
            obj = Player(self.x+1, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
            return obj
    def update(self, direction):
        if direction == 97:
            obj = Player(self.x-1, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
            return obj
        elif direction == 100:
            obj = Player(self.x+1, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
            return obj
        elif direction == 115:
            obj = Player(self.x, self.y+1, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
            return obj
            
        elif direction == 119:
            obj = Player(self.x, self.y-1, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
            return obj     
        else:
            pass
        obj = Player(self.x, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
        return obj

class FMAP:
    def __init__(self, x, y) -> None:
        self.y = y
        self.x = x
    def update(self, entities, y, x):
        fmap = [['·' for i in range(x)] for j in range(y)]
        for entity in entities:
            i, j = entity.pos
            fmap[j][i] = str(entity.number)
        return fmap
    def render(self, fmap):
        tmap = '\n'.join(''.join(line) for line in fmap)
        print(tmap)
def getinput():
    key = ord(getch())
    if key == 97:
        print(key)
        return key
    elif key == 100:
        print(key)
        return key
    elif key == 115:
        print(key)
        return key
    elif key == 119:
        print(key)
        return key
    else:
        pass
players = [Player.generate('DEF') for i in range(3)]
fmap = FMAP(20,10)
while True:
    put = getinput()
    players[0] = players[0].update(put)
    print(players[0].__dict__)
    tmap = fmap.update(players, fmap.y, fmap.x)
    for i in range(1, len(players)):
        players[i] = players[i].cpu_update()
        print(players[i].__dict__)
    fmap.render(tmap)
    time.sleep(0.3)