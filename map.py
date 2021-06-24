class Map:

    def __init__(self, size):
        self.size = size
    
    def create_map(self):
        for _ in range (0,self.size):
            for _ in range (0,self.size):
                print('[X]', end='')
            print('')




map = Map(8)
map.create_map()


