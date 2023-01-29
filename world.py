class World:
    """
        Classe représentant un monde océanique.
    """
    def __init__(self, cols, rows):
        """Initialise un monde océanique avec des dimensions données.

        Args:
            cols (int): Le nombre de colonnes dans le monde.
            rows (int): Le nombre de lignes dans le monde.
        """
        self.cols = cols
        self.rows = rows
        self.table = self.create_2d_table(cols, rows)
        self.sharks = []
        self.fishes = []

    def create_2d_table(self, cols, rows):
        """Crée une table à deux dimensions pour représenter le monde.

        Args:
            cols (int): Le nombre de colonnes dans le monde.
            rows (int): Le nombre de lignes dans le monde.

        Retourne:
            list: La table à deux dimensions qui représente le monde.
        """
        table = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append('  ')
            table.append(row)
        return table
    
    def display_grid(self):
        """Affiche la grille de la table à deux dimensions représentant le monde.
        """
        for row in self.table:
            print("|".join(row))

    def add_shark(self, shark):
        """Ajoute un requin à la position donnée.

        Args:
            shark (objet): Un objet représentant un requin avec des attributs x et y.
        """
        if not self.is_valid_position(shark.x, shark.y):
            return
        if len(self.sharks) >= (self.cols * self.rows):
            return
        self.sharks.append(shark)
        self.table[shark.x][shark.y] = '🦈'

    def add_fish(self, fish):
        """Ajoute un poisson à la position donnée.

        Args:
            fish (objet): Un objet représentant un poisson avec des attributs x et y.
        """
        if not self.is_valid_position(fish.x, fish.y):
            return
        if len(self.fishes) >= (self.cols * self.rows):
            return
        self.fishes.append(fish)
        self.table[fish.x][fish.y] = '🐠'
        
    def is_valid_position(self, x, y):
        """Vérifie si la position donnée est valide dans le monde.

        Args:
            x (int): La coordonnée x de la position.
            y (int): La coordonnée y de la position.

        Returns:
            bool: True si la position est valide dans le monde, False sinon
        """
        if x >= self.rows or y >= self.cols:
            return False
        return True