class Hability:

    #types:
    # 1 - common: used in rooms
    # 2 - battle: used in battles
    # 3 - misc  : miscelanius used in both rooms and battles
    #
    #Habilities
    # 1 - Reveal.....: Reveals hidden objects in the room
    # 2 - ultraAtck..: Upgrades passively the phys atck for 3 atcks
    # 2 - nyanCat....: Upgrades passively the atckspeed for 10 atcks
    # 2 - goBrasil...: Halfes the maxHP and double the atack for 5 atcks, after 5 atcks maxHP returns but LIFE not
    # 3 - Heal.......: Heals the character in X points   

    def __init__(self, name, description, lucky, points, type):
        self.name = name