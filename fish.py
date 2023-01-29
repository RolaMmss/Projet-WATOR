from world import World
import random

class Fish:
    """Classe représentant un poisson dans un monde simulé

    Attributs:
        fish_count (int): Compteur de poissons créés
    """
    fish_count = 0
    def __init__(self, x, y):
        """Initialise un poisson avec des coordonnées x et y

        Args:
            x (int): Coordonnée x de la position du poisson
            y (int): Coordonnée y de la position du poisson
        """
        self.x = x
        self.y = y
        self.reproduction_number = 2


    def move(self, world):
        """Fait bouger le poisson dans le monde simulé

        Args:
            world (World): Le monde simulé où le poisson se déplace

        Returns:
            tuple: Anciennes coordonnées x et y du poisson
        """
        old_x = self.x
        old_y = self.y
        # Génère une liste de positions possibles pour le poisson de se déplacer
        possible_positions = self.verification_move(world)
        #Si il y a des positions possibles pour le poisson de se déplacer
        if len(possible_positions) > 0:
            # Choisit aléatoirement une position de la liste possible_positions
            new_pos = random.choice(possible_positions)
            # Met à jour la grille en enlevant le poisson de sa position actuelle
            world.table[self.x][self.y] = '  '
            # Met à jour les coordonnées du poisson
            self.x = new_pos[0]
            self.y = new_pos[1]
            # Met à jour la grille en ajoutant le poisson à sa nouvelle position
            world.table[self.x][self.y] = '🐠'
        return old_x , old_y
                
    def reproduce(self, world, day, old_x, old_y):
        """Fait reproduire le poisson dans le monde simulé

        Args:
            world (World): Le monde simulé où le poisson se reproduit
            day (int): Le jour actuel de la simulation
            old_x (int): Ancienne coordonnée x de la position du poisson
            old_y (int): Ancienne coordonnée y de la position du poisson
        """
        if day % self.reproduction_number == 0:
            if world.table[old_x][old_y] == "  ":
                new_fish = Fish(old_x, old_y)
                Fish.fish_count += 1
                world.add_fish(new_fish)
                  
    def verification_move(self, world):
        """Vérifie les positions possibles pour le poisson de se déplacer

        Args:
            world (World): Le monde simulé où le poisson se déplace

        Returns:
            list: Liste des positions possibles pour le poisson
        """
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
                if world.table[x][y] != '🦈' and world.table[x][y] != '🐠':
                    # Ajoute les coordonnées de la case cible à la liste de positions possibles
                    possible_positions.append((x, y))
        # Retourne la liste de positions possibles
        return possible_positions
  
                        
  