import Dice as dd

#class Battle:
#
#    def __init__(self, at, df):
#        self.at = at
#        self.df = df

def attack(attacker,defensor):
    defensor.life -=  dd.dmgLucky(attacker.atck, attacker.lucky, attacker.dex)

def heal(character, healValue):
    heal = dd.heal(healValue)
    print(heal)
    if character.life + heal > character.maxHP:
        character.life = character.maxHP
    else:
        character.life += heal

#magias
def duel(ch1, ch2):
    while ch1.life > 0 and ch2.life > 0:
        attack(ch1, ch2)
        attack(ch2, ch1)
        print(ch1.toString())
        print(ch2.toString())
        print("----------------------")
    if ch1.life > 0:
        winner = ch1
    else:
        winner = ch2
    return winner