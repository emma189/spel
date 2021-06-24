class Treasure:

    def __init__(self):
        self.value = None
        self.commonality = None

class Coins(Treasure):

    def __init__(self):
        super().__init__()
        self.value = 2
        self.commonality = 40
    
class Coin_pouch(Treasure):

    def __init__(self):
        super().__init__()
        self.value = 6
        self.commonality = 20

class Gold_jewelry(Treasure):

    def __init__(self):
        super().__init__()
        self.value = 10
        self.commonality = 15

class Jem(Treasure):

    def __init__(self):
        super().__init__()
        self.value = 14
        self.commonality = 10

class Treasure_chest(Treasure):
    
    def __init__(self):
        super().__init__()
        self.value = 20
        self.commonality = 5
