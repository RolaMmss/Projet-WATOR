from fish import Fish
from world import World

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
    
    def shark_dead(self, world):
        if self[self.x][self.y] and isinstance(self[self.x][self.y], Fish):
           self.energy += 1
        else:
           self.energy -= 1
        if self.energy <= 0:
            world.self.sharks -= 1
            world.sharks.remove(self)
            
    def verification_move(self):
        pass