class World:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.table = self.create_2d_table(cols, rows)
        self.sharks = []
        self.fishes = []

    def create_2d_table(self, cols, rows):
        table = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append('  ')
            table.append(row)
        return table
    
    def display_grid(self):
        for row in self.table:
            print("|".join(row))

    def add_shark(self, shark):
        self.sharks.append(shark)

    def add_fish(self, fish):
        if len(self.fishes) >= (self.cols * self.rows):
            return
        self.fishes.append(fish)
        self.table[fish.x][fish.y] = '🐠'