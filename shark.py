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
        if day % 10 == 0:
            # Si la case où se trouve le requin parent est vide
            if world.table[old_x][old_y] == '  ':
                # On crée un nouveau requin à la position du parent
                new_shark = Shark(old_x, old_y)
                # on met a jour la grille et on ajoute le nouveau requin à la liste des requins
                world.add_shark(new_shark)
                     
    def hunt(self,world):      
    # Initialise une liste de positions possibles pour le poisson de se déplacer
        possible_positions = []
        v = False
    # Boucle à travers les déplacements possibles pour le poisson (dx et dy peuvent prendre les valeurs -1, 0, 1)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
            # Calcul les nouvelles coordonnées du poisson en utilisant l'opérateur modulo pour s'assurer 
            # qu'elles restent dans les limites de la grille en bouclant sur les bords
                x = (self.x + dx) % world.rows
                y = (self.y + dy) % world.cols
            # Vérifie si la case cible ne contient pas un requin ou un autre poisson
                if world.table[x][y] == '🐠':
                    possible_positions.append((x, y))
                    for fish in world.fishes:
                        if fish.x == x and fish.y == y:
                            world.fishes.remove(fish)
                            self.energy += 1
                            world.table[x][y] = "  "
                            break
                elif world.table[x][y] != '🦈' and world.table[x][y] != '🐠':
                    v = True
                # Ajoute les coordonnées de la case cible à la liste de positions possibles
                    possible_positions.append((x, y))
    # Retourne la liste de positions possibles
        if v == True:
            self.energy -= 1
            print(self.energy)
        self.shark_dead(world, x , y)
        return possible_positions
                        

    
    def shark_dead(self, world, x , y):
        if self.energy > 7 :   
            self.energy = 7                       
        elif self.energy <= 0:
            for shark in world.sharks:
                if shark.x == x and shark.y == y:
                    world.sharks.remove(shark)
                    world.table[x][y] = "  "