import random
class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        chance = random.randint(1,10)

        if chance > ninja.speed:
            damage = random.randint(0,self.strength)
            ninja.health -= damage
            print(f"{self.name} damaged {ninja.name} by {damage}!")
        else: 
            print(f"{self.name} missed!")
        return self

