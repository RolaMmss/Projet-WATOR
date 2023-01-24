class World:
    def display_world(length : int, width : int):
        pass
    def add_animals():
        pass
    def play_turn():
        pass
    

class Animal:
    def move():
        up : y = y+1
        down : y = y-1
        right : x = x+1
        left : x = x-1
        freeze : x == x and y == y 
    def reproduce():
        reproduction_time : int
        pass
    def die():
        pass

class Shark(Animal):
    nb_sharks : int
    energy : int
    shark_reproduction_time : int
    shark_position (x,y)
    def search_fish():
        pass
        else move()
    def eat_fish():
        pass
    

class Fish(Animal):
    nb_fish : int
    fish_reproduction_time : int
    fish_position (x,y)
    def search_empty_case():
        pass


def main():
    display_world()
    add_animals()
    turn()
    

    turn = 0


    main()

