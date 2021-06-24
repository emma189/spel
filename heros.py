class Hero:
    def __init__(self):
        self.health = None
        self.attack = None
        self.initiative = None
        self.agility = None
    
    def take_damage(self):
        pass


class Knight(Hero):

    def __init__(self):
        super().__init__()
        self.health = 9
        self.attack = 6
        self.initiative = 5
        self.agility = 4


class Wizard:

    def __init__(self):
        super().__init__()
        self.health = 4
        self.attack = 9
        self.initiative = 6
        self.agility = 5


class Thief:
    def __init__(self):
        super().__init__()
        self.health = 5
        self.attack = 5
        self.initiative = 7
        self.agility = 7


my_hero = Knight()
print(my_hero.health)