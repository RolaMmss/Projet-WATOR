from fish import Fish
from shark import Shark
from world import World
import random as rd
import time
import os

####################################
#        Initialisation           #
####################################

number_of_fish = 100
number_of_sharks = 70

# Création de l'environnement
day = 1
rows = 40
cols = 40
world = World(rows, cols)

# Ajout aléatoire de requins et de poissons dans l'environnement
for i in range(number_of_sharks):
    shark = Shark(rd.randint(1,rows - 1), rd.randint(1,cols - 1))
    world.add_shark(shark)

for i in range(number_of_fish):
     fish = Fish(rd.randint(1, rows - 1), rd.randint(1, cols - 1))
     world.add_fish(fish)

# Boucle principale de la simulation
while True:
    for shark in world.sharks.copy():
          old_x , old_y = shark.move(world)
          shark.reproduce(world,old_x , old_y)
    if len(world.sharks) == 0 and len(world.fishes) == 0:
        print("All fish and sharks have died, simulation stopping.")
        exit()
    for fish in world.fishes.copy():
          old_x , old_y = fish.move(world)
          fish.reproduce(world,day,old_x , old_y)
    if (world.cols * world.rows) == len(world.fishes):
        print("Fishes Win")
        exit()
    world.display_grid()
    print("jours : {}".format(day))
    print("poissons : {} requins: {}".format(len(world.fishes), len(world.sharks)))
    time.sleep(0.3)
    day += 1
    os.system("clear")