from classes.ninja import Ninja
from classes.pirate import Pirate

mike = Ninja("Michelanglo")

zoro = Pirate("Jack Sparrow")

def battle(pirate, ninja):
    while pirate.health and ninja.health >= 0:
        print(f"{ninja.name} attacks {pirate.name}!")
        ninja.attack(pirate)
        pirate.show_stats()
        print(f"{pirate.name} attacks {ninja.name}!")
        pirate.attack(ninja)
        ninja.show_stats( )
    if pirate.health > ninja.health:
        print(f"{pirate.name} wins!")
    else:
        print(f"{ninja.name} wins!")


battle(zoro, mike)
