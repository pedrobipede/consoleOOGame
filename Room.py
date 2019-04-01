class Room:

    #type:
    # 1 - dungeon
    # 2 - tavern
    # 3 - land

    def __init__(self, enemys, pill, hidden, type):
        self.enemys = enemys
        self.pill = pill
        self.hidden = hidden

    def toString(self):
        return ""

