from fish import Fish
from world import World
import random as rd

class Shark(Fish):
    def __init__(self, x , y):
        super().__init__(x, y)
        self.reproduction_number = 7
        self.energy = 7

    def move(self, world):
        # Enregistre les coordonnées actuelles du requin
        old_x = self.x
        old_y = self.y
        # Retourne les anciennes coordonnées du requin pour la reproduction
        return old_x , old_y
    

   
    def reproduce(self, day, world, old_x, old_y):
        # Si c'est le jour de reproduction (tous les 4 jours)
        if day % 6 == 0:
            # Si la case où se trouve le requin parent est vide
            if world.table[old_x][old_y] == '  ':
                # On crée un nouveau requin à la position du parent
                new_shark = Shark(old_x, old_y)
                # On met à jour la grille
                world.table[old_x][old_y] = '🦈'
                # On ajoute le nouveau requin à la liste des requins
                world.sharks.append(new_shark)  
                     
    def hunt(self,world):      
        # Recherche les cases pour trouver un poisson
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = self.x + dx, self.y + dy
            if (x >= 0 and x < world.cols) and (y >= 0 and y < world.rows) and isinstance(world.table[x][y], Fish):
            # Si un poisson est trouvé bouge le requin vers cette case
                self.x, self.y = x, y
                return
        # Si aucun poisson n'est trouvé utilise un mouvement aléatoire
        self.x, self.y = self.x + rd.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        # Pas de else donc si pas de case disponible pas de mouement
                    

    
    def shark_dead(self, world):
            # Si la case actuelle ([x,y]) a un objet Fish et si l'energie du requin est < 7
        if  world.table[self.x][self.y] and isinstance([self.x][self.y], Fish) and self.energy < 7:
            # Augmente l'énergie du requin
            self.energy += 1                    
            # Enléve -1 du nombre des fish dans world    
            world.fishes -= 1  
        else:  
            # Supprime le poisson de la liste de poissons dans world                      
            world.fishes.remove(self[self.x][self.y]) 
            # Sinon, enléve - 1 à l'énergie du requin 
            self.energy -= 1                        
            # Vérifie si l'énergie du requin est inférieure ou égale à 0   
        if  self.energy <= 0:              
            # Si oui enléve -1 du nombre des requins dans l'objet world            
            world.sharks -= 1                       
             # Supprime l'objet requin de la liste de requins dans l'objet world 
            world.sharks.remove([self.x][self.y]) 