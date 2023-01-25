from world import World
import random

class Fish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reproduction_number = 4

    def move(self, world):
        old_x = self.x
        old_y = self.y
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1]) if dx == 0 else 0
        world.table[self.y][self.x] = '  '
        self.x = (self.x + dx) % world.cols
        self.y = (self.y + dy) % world.rows
        world.table[self.y][self.x] = '🐠'
        return old_x , old_y
        

    def reproduce(self,day,world, old_x, old_y):
        if day  == 4 : #and isinstance(self[self.x][self.y], Fish):
             fish = Fish(old_x , old_y)
             world.fishes.append(fish)
             world.table[old_x][old_y] = '🐠'
            
            
        
    def verification_move(self):
        pass
