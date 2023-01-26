from fish import Fish
from world import World
import random as rd

class Shark(Fish):
    def __init__(self, x , y):
        super().__init__(x, y)
        self.reproduction_number = 7
        self.energy = 7

    def move(self):
       pass
   
    def reproduce(self,day,world):
        pass
        # if day % self.reproduction_number  == 0 : #and isinstance(self[self.x][self.y], Fish):
        #     new_shark = Shark()
        #     world.sharks.append(new_shark)
        #     world.table[self.y][self.x] = '🦈'
    def hunt(self):
        pass
    
    def shark_dead(self, world):
            # Si la case actuelle ([x,y]) a un objet Fish et si l'energie du requin est < 7
        if  world.table[self.x][self.y] and isinstance([self.x][self.y], Fish) and self.energy < 7:
            self.energy += 1                            # Augmente l'énergie du requin
            world.fishes -= 1                           # Enléve -1 du nombre des fish dans l'objet "world"
            world.fishes.remove(self[self.x][self.y])   # Supprime le poisson de la liste de poissons dans l'objet "world"
        else:
            self.energy -= 1                            # Sinon, enléve - 1 à l'énergie du requin
        if  self.energy <= 0:                           # Vérifie si l'énergie du requin est inférieure ou égale à 0
            world.sharks -= 1                           # Si oui, enléve -1 du nombre des requins dans l'objet "world"
            world.sharks.remove(self[self.x][self.y])   # Supprime l'objet requin de la liste de requins dans l'objet "world"
  