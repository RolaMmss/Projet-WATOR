from world import World
import random

class Fish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reproduction_number = 4

    def move(self, world):
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1]) if dx == 0 else 0
        world.table[self.y][self.x] = '  '
        self.x = (self.x + dx) % world.cols
        self.y = (self.y + dy) % world.rows
        world.table[self.y][self.x] = '🐠'

    def reproduce(self):
        pass
        
    def verification_move(self):
        pass
