from fish import Fish
from shark import Shark
from world import World
import random as rd
import time
import os

####################################
#        Initialization            #
####################################

number_of_fish = 300 #int(input("Enter the number of fish : "))
number_of_sharks = 100  #int(input("Enter the number of sharks : "))

#creation of the world
day = 1
rows = 30
cols = 30
world = World(rows, cols)

for i in range(number_of_sharks):
    shark = Shark(rd.randint(1,rows - 1), rd.randint(1,cols - 1))
    world.add_shark(shark)

for i in range(number_of_fish):
    fish = Fish(rd.randint(1, rows - 1), rd.randint(1, cols - 1))
    world.add_fish(fish)

#####################################
#              START                #
#####################################
while day < 500:
    for shark in world.sharks.copy():
          old_x , old_y = shark.move(world)
          shark.reproduce(world,old_x , old_y)
    for fish in world.fishes.copy():
          old_x , old_y = fish.move(world)
          fish.reproduce(world,day,old_x , old_y)
    if (world.cols * world.rows) == len(world.fishes) or len(world.sharks) == 0 :
            print("Fishes Win")
            exit()
    world.display_grid()
    print("jours : {}".format(day))
    print("poissons : {} requins: {}".format(len(world.fishes), len(world.sharks)))
    time.sleep(0.2)
    day += 1
    os.system("clear")