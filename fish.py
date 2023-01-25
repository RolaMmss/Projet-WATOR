from world import World
import random

class Fish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reproduction_number = 4

    def move(self, world):   
        # Enregistre les coordonnées actuelles du poisson
        old_x = self.x
        old_y = self.y
        # Vérifie les cases autour du poisson grâce a la fonction
        self.verification_move(world)
        # Déplace le poisson aléatoirement (dx et dy peuvent prendre les valeurs -1, 0, 1)
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1]) if dx == 0 else 0
        # Met à jour la grille en enlevant le poisson de sa position actuelle
        world.table[self.x][self.y] = '  '
        # Met à jour les coordonnées du poisson en utilisant l'opérateur modulo pour s'assurer 
        # qu'elles restent dans les limites de la grille en bouclant sur les bords
        self.x = (self.x + dx) % world.rows
        self.y = (self.y + dy) % world.cols
        # Met à jour la grille en ajoutant le poisson à sa nouvelle position
        world.table[self.x][self.y] = '🐠'
        # Retourne les anciennes coordonnées du poisson pour la reproduction
        return old_x , old_y
        

    def reproduce(self, day, world, old_x, old_y):
        # Si c'est le jour de reproduction (tous les 4 jours)
        if day % 4 == 0:
            # Si la case où se trouve le poisson parent est vide
            if world.table[old_x][old_y] == '  ':
                # On crée un nouveau poisson à la position du parent
                new_fish = Fish(old_x, old_y)
                # On met à jour la grille
                world.table[old_x][old_y] = '🐠'
                # On ajoute le nouveau poisson à la liste des poissons
                world.fishes.append(new_fish)
            
            
        
    def verification_move(self, world):             
        if world.table[self.x - 1 ][self.y] == '🐠🦈':
            print("Coup dur")       