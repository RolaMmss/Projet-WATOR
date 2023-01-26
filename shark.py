from fish import Fish
from world import World
import random as rd

class Shark(Fish):
    def __init__(self, x , y):
        super().__init__(x, y)
        self.reproduction_number = 7
        self.energy = 7

    def move(self, world, day):
        # Enregistre les coordonnées actuelles du requin
        old_x = self.x
        old_y = self.y
        possible_positions = self.hunt(world)
        if len(possible_positions) > 0:
            print(possible_positions)
            # Choisit aléatoirement une position de la liste possible_positions
            new_pos = rd.choice(possible_positions)
            # Met à jour la grille en enlevant le poisson de sa position actuelle
            world.table[self.x][self.y] = '  '
            # Met à jour les coordonnées du poisson
            self.x = new_pos[0]
            self.y = new_pos[1]
            # Met à jour la grille en ajoutant le poisson à sa nouvelle position
            world.table[self.x][self.y] = '🦈'
            # Retourne les anciennes coordonnées du poisson pour la reproduction
            self.reproduce(day, world, old_x, old_y)
    

   
    def reproduce(self, day, world, old_x, old_y):
        # Si c'est le jour de reproduction (tous les 6 jours)
        if day % 6 == 0:
            # Si la case où se trouve le requin parent est vide
            if world.table[old_x][old_y] == '  ':
                # On crée un nouveau requin à la position du parent
                new_shark = Shark(old_x, old_y)
                # on met a jour la grille et on ajoute le nouveau requin à la liste des requins
                world.add_shark(new_shark)
                     
    def hunt(self,world):      
        # # Recherche les cases pour trouver un poisson
        # for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #     x, y = self.x + dx, self.y + dy
        #     if (x >= 0 and x < world.cols) and (y >= 0 and y < world.rows) and isinstance(world.table[x][y], Fish):
        #     # Si un poisson est trouvé bouge le requin vers cette case
        #         self.x, self.y = x, y
        #         return
        
        #################################################
        ## Si il ne trouve pas de poisson autour delui ##
        #################################################
        # Initialise une liste de positions possibles pour le poisson de se déplacer
        possible_positions = []
        #Boucle à travers les déplacements possibles pour le poisson (dx et dy peuvent prendre les valeurs -1, 0, 1)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # Calcul les nouvelles coordonnées du poisson en utilisant l'opérateur modulo pour s'assurer 
                # qu'elles restent dans les limites de la grille en bouclant sur les bords
                x = (self.x + dx) % world.rows
                y = (self.y + dy) % world.cols
                # Vérifie si la case cible ne contient pas un requin ou un autre poisson
                if world.table[x][y] == '🐠':
                    possible_positions.append((x, y))
                    break
                elif world.table[x][y] != '🦈' and world.table[x][y] != '🐠':
                    # Ajoute les coordonnées de la case cible à la liste de positions possibles
                    possible_positions.append((x, y))
        # Retourne la liste de positions possibles
        return possible_positions
                    

    
    def shark_dead(self, world):
            # Si la case actuelle ([x,y]) a un objet Fish et si l'energie du requin est < 7
        if  world.table[self.x][self.y] and isinstance([self.x][self.y], Fish) and self.energy < 7:
            # Augmente l'énergie du requin
            self.energy += 1                    
            # Enléve -1 du nombre des fish dans world    
            world.fishes -= 1  
            # Supprime le poisson de la liste des fishes dans world                      
            world.fishes.remove([self.x][self.y]) 
        else:  
            # Sinon, enléve - 1 à l'énergie du requin 
            self.energy -= 1                        
            # Vérifie si l'énergie du requin est inférieure ou égale à 0   
        if  self.energy <= 0:              
            # Si oui enléve -1 du nombre des requins dans l'objet world            
            world.sharks -= 1                       
             # Supprime l'objet requin de la liste de requins dans l'objet world 
            world.sharks.remove([self.x][self.y]) 