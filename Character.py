class Character:
    def __init__(self, name, clss, life, atck, lucky, dex, armor, maxHP):
        self.name = name
        self.clss = clss
        self.life = life
        self.atck = atck
        self.lucky = lucky
        self.dex = dex
        self.armor = armor
        self.maxHP = maxHP

    def toString(self):
        return "[Name: {}, Class: {}; life: {}; armor: {}; atack: {}; lucky: {}; dex: {}, maxHP: {}]".format(self.name, self.clss, self.life, self.armor, self.atck, self.lucky, self.dex, self.maxHP)

    def randomEnemy(self, maxLvl):
        return 0