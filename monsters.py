class Monster:

    def __init__(self):
        self.initiativ = None
        self.endurance = None
        self.attack = None
        self.flexibility = None
        self.commonality = None

class Spider(Monster):

    def __init__(self):
        super().__init__()
        self.initiativ = 7
        self.endurance = 1
        self.attack = 2
        self.flexibility = 3
        self.commonality = 20


class Skeleton(Monster):

    def __init__(self):
        super().__init__()
        self.initiativ = 4
        self.endurance = 2
        self.attack = 3
        self.flexibility = 3
        self.commonality = 15


class Orc(Monster):

    def __init__(self):
        super().__init__()
        self.initiativ = 6
        self.endurance = 3
        self.attack = 4
        self.flexibility = 4
        self.commonality = 10


class Troll(Monster):

    def __init__(self):
        super().__init__()
        self.initiativ = 2
        self.endurance = 4
        self.attack = 7
        self.flexibility = 2
        self.commonality = 5
