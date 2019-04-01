import Character as chh
import PVE as pv

enemy = chh.Character()
enemy.randomCharacter(1)
print(enemy.toString())

pedro = chh.Character()
pedro.createCharacter('pedro', 'warrior', 100, 5, 5, 10, 15, 200)

while pedro.life > 0 and enemy.life > 0:
    pass
    battle = pv.PVE(pedro, enemy)
    battle.enemyTurn()
    battle.playerTurn()