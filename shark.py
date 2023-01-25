from fish import Fish

class Shark(Fish):
    def __init__(self, x , y):
        super().__init__(x, y)
        self.reproduction_number = 7
        self.energy = 7

    def move(self):
        pass

    def reproduce(self):
        pass

    def hunt(self):
        pass
    
    def shark_dead(self):
        pass
    
    def verification_move(self):
        pass