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
        self.verification_move(world)          
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1]) if dx == 0 else 0
        world.table[self.x][self.y] = '  '
        self.x = (self.x + dx) % world.rows
        self.y = (self.y + dy) % world.cols
        world.table[self.x][self.y] = '🐠'
        return old_x , old_y
        

    def reproduce(self, day, world, old_x, old_y):
        list_number = len(world.fishes)
        i = 0
        if day % 4 == 0:
            while i <= list_number:
                fish = Fish(old_x, old_y)
                print(fish)
                world.table[old_x][old_y] = '🐠'
                world.fishes.append(fish)
                print(len(world.fishes))
                i += 1
            
            
        
    def verification_move(self, world):             
        if world.table[self.x - 1 ][self.y] == '🐠🦈':
            print("Coup dur")       