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
   
    def reproduce(self):
        pass

    def hunt(self):
        pass
    
    def shark_dead(self, world):
            # Si la case actuelle [x,y] a un objet Fish et si l'energie du requi est < 7
        if self[self.x][self.y] and isinstance(self[self.x][self.y], Fish) and self.energy < 7:
            # Augmente l'énergie du requin
            self.energy += 1
            # Enléve -1 du nombre des fish dans l'objet "world"
            world.fishes -= 1
            # Supprime le poisson de la liste de poissons dans l'objet "world"
            world.fishes.remove(self[self.x][self.y])
        else:
            # Sinon, enléve - 1 à l'énergie du requin
            self.energy -= 1
            # Vérifie si l'énergie du requin est inférieure ou égale à 0
        if self.energy <= 0:
            # Si oui, enléve -1 du nombre des requins dans l'objet "world"
            world.sharks -= 1
            # Supprime l'objet requin de la liste de requins dans l'objet "world"
            world.sharks.remove(self[self.x][self.y])
  