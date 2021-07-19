import random, time, os, sys
from msvcrt import getch

class Skill:
    def __init__(self, number, name, cost, tipo, bonificador, calculo):
        self.number = number
        self.name = name
        self.cost = cost
        self.tipo = tipo
        self.bonificador = bonificador
        self.calculo = calculo


class Player:
    def __init__(self, skill_list, hasball, x, y, number, position, stamina, passe, dodge, shoot, intercept, entry, block):
        self.skill_list = skill_list
        self.hasball = hasball
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
            obj = Player([Skill(False, "Normal", 20, "Remate", 0, ""), Skill(False, "Normal", 20, "Entrada", 0, ""), Skill(False, "Normal", 20, "Bloqueo", 0, ""), Skill(False, "Normal", 20, "Intercepcion", 0, "")], False, random.randint(1, 4),random.randint(1, 9), random.randint(0,9), 'DEF', random.randint(100,900), random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100))
        elif position == 'MF':
            obj = Player([Skill(False, "Normal", 20, "Remate", 0, ""), Skill(False, "Normal", 20, "Entrada", 0, ""), Skill(False, "Normal", 20, "Bloqueo", 0, ""), Skill(False, "Normal", 20, "Intercepcion", 0, "")], False, random.randint(1, 4),random.randint(1, 9), random.randint(0,9), 'MF', random.randint(100,900), random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100))
        elif position == 'FW':
            obj = Player([Skill(False, "Normal", 20, "Remate", 0, ""), Skill(False, "Normal", 20, "Entrada", 0, ""), Skill(False, "Normal", 20, "Bloqueo", 0, ""), Skill(False,"Normal", 20, "Intercepcion", 0, "")], False, random.randint(1, 4),random.randint(1, 9), random.randint(0,9), 'FW', random.randint(100,900), random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100))
        return obj
    def cpu_update(self):
        if self.x == 1:
            obj = Player(self.skill_list, self.hasball, self.x+1, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
            return obj
        if self.x==9:
            obj = Player(self.skill_list, self.hasball, self.x-1, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
            return obj
        if self.x != 9 or self.x != 1:
            obj = Player(self.skill_list, self.hasball, self.x+1, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
            return obj
    def useskill(self):
        for i in range(len(self.skill_list)):
            self.skill_list[i].number=i
            print(self.skill_list[i].__dict__)
        entry = int(input("\nSkill to use: "))
        return self.skill_list[entry].cost
    
    def update(self, direction):
        if direction == 97:
            if self.x > 0:
                obj = Player(self.skill_list, self.hasball, self.x-1, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
                return obj
            else:
                obj = Player(self.skill_list, self.hasball, self.x, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
                return obj
        elif direction == 100:
            if self.x < 19:
                obj = Player(self.skill_list, self.hasball, self.x+1, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
                return obj
            else:
                obj = Player(self.skill_list, self.hasball, self.x, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
                return obj
        elif direction == 115:
            if self.y < 9:
                obj = Player(self.skill_list, self.hasball, self.x, self.y+1, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
                return obj
            else:
                obj = Player(self.skill_list, self.hasball, self.x, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
                return obj
        elif direction == 119:
            if self.y > 0:
                obj = Player(self.skill_list, self.hasball, self.x, self.y-1, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
                return obj
            else:
                obj = Player(self.skill_list, self.hasball, self.x, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
                return obj
        elif direction == 49:
            skill_cost=self.useskill()
            obj = Player(self.skill_list, self.hasball, self.x, self.y, self.number, self.position, self.stamina-skill_cost, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
            return obj
        else:
            obj = Player(self.skill_list, self.hasball, self.x, self.y, self.number, self.position, self.stamina, self.passe, self.dodge, self.shoot, self.intercept, self.entry, self.block)
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
class InputX:
    def getinput():
        key = ord(getch())
        if key == 97:
            return key
        elif key == 100:
            return key
        elif key == 115:
            return key
        elif key == 119:
            return key
        elif key == 49:
            return key
        else:
            pass
class Game():
    def main():
        players = [Player.generate('DEF') for i in range(3)]
        players[0].hasball = True
        fmap = FMAP(20,10)
        inputx = InputX
        while True:
            put = inputx.getinput()
            players[0] = players[0].update(put)
            os.system('cls')
            print((players[0].hasball, players[0].number, players[0].pos, players[0].stamina))
            tmap = fmap.update(players, fmap.y, fmap.x)
            for i in range(1, len(players)):
                players[i] = players[i].cpu_update()
                print((players[i].hasball, players[i].number, players[i].pos, players[i].stamina))
            fmap.render(tmap)
            time.sleep(0.3)

game = Game
game.main()