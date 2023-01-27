from fish import Fish
from shark import Shark
from world import World
import random as rd
import time
import os

####################################
#        Initialization            #
####################################

number_of_fish = 3 #int(input("Enter the number of fish : "))
number_of_sharks = 1   #int(input("Enter the number of sharks : "))

#creation of the world
day = 0
rows = 5
cols = 5
world = World(rows, cols)

# Randomly populate grid with sharks and fish
for i in range(number_of_sharks):
    shark = Shark(rd.randint(1,rows - 1), rd.randint(1,cols - 1))
    world.add_shark(shark)

for i in range(number_of_fish):
    fish = Fish(rd.randint(1, rows - 1), rd.randint(1, cols - 1))
    world.add_fish(fish)

#####################################
#              START                #
#####################################
# while day < 500:
while True:
    if len(world.sharks) == 0 and len(world.fishes) == 0:
        print("All fish and sharks have died, simulation stopping.")
        break
    world.display_grid()
    for shark in world.sharks.copy():
          old_x , old_y = shark.move(world)
          shark.reproduce(world,day,old_x , old_y)
    for fish in world.fishes.copy():
        old_x , old_y = fish.move(world)
        fish.reproduce(world,day,old_x , old_y)
    print("jours : {}".format(day))
    print("poissons : {} requins: {}".format(len(world.fishes), len(world.sharks)))
    time.sleep(3)
    day += 1
    if
    # os.system("clear")