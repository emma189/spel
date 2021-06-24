import random

class Room:

    def __init__(self):
        self.treasures = 1
        self.monsters = 2
    

def randomizer(list):
    return (random.choice(list))

treasures = ['']