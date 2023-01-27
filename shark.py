from fish import Fish
from world import World
import random as rd

class Shark(Fish):
    def __init__(self, x , y):
        super().__init__(x, y)
        self.reproduction_number = 8
        self.energy = 5

    def move(self, world): 
        old_x = self.x
        old_y = self.y
        # Génère une liste de positions possibles pour le poisson de se déplacer
        possible_positions = self.hunt(world)
        #Si il y a des positions possibles pour le poisson de se déplacer
        if len(possible_positions) > 0:
            # Choisit aléatoirement une position de la liste possible_positions
            new_pos = rd.choice(possible_positions)
            # Met à jour la grille en enlevant le poisson de sa position actuelle
            world.table[self.x][self.y] = '  '
            # Met à jour les coordonnées du poisson
            self.x = new_pos[0]
            self.y = new_pos[1]
            # Met à jour la grille en ajoutant le poisson à sa nouvelle position
            world.table[self.x][self.y] = '🦈'
            self.shark_dead(world)
        return old_x , old_y
                
    def reproduce(self, world,day,old_x , old_y):
        # Si le poisson s'est déplacé à une nouvelle position
        if day % self.reproduction_number == 0:
            if world.table[old_x][old_y] == "  ":
                new_shark = Shark(old_x, old_y)
                world.add_shark(new_shark)
                     
    def hunt(self,world):      
        possible_positions = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                x = (self.x + dx) % world.rows
                y = (self.y + dy) % world.cols
                if world.table[x][y] == '🐠':
                    possible_positions.append((x, y))
                    for fish in world.fishes:
                        if fish.x == x and fish.y == y:
                            world.fishes.remove(fish)
                            self.energy += 2
                            world.table[x][y] = "  "
                            break
                elif world.table[x][y] != '🦈' and world.table[x][y] != '🐠':
                    possible_positions.append((x, y))
        self.energy -= 1
        return possible_positions
                    
    def shark_dead(self, world):
        for shark in world.sharks:
            if shark.energy <= 0:
                world.table[shark.x][shark.y] = "  "
                world.sharks.remove(shark)