from fish import Fish
from shark import Shark
from world import World
import random as rd

####################################
#        Initialization            #
####################################

number_of_fish = 50         #int(input("Enter the number of fish : "))
number_of_sharks = 20       #int(input("Enter the number of sharks : "))

#creation of the world
day = 1
world = World(20, 20)

for i in range(10):
    shark = Shark(rd.randint(1,19), rd.randint(1,19))
    world.add_shark(shark)

fish1 = Fish(10, 10)
world.add_fish(fish1)

#####################################
#              START                #
#####################################
while day < 2:
    print("jour : " + str(day))
    world.display_grid()
    for shark in world.sharks:
        shark.move()
        shark.hunt()
        shark.reproduce()
    for fish in world.fishes:
        fish.move()
        fish.reproduce()
    day += 1
