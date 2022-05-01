import random


class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 20
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        chance = random.randint(1,10)

        if chance > pirate.speed:
            damage = random.randint(0,self.strength)
            pirate.health -= damage
            print(f"{self.name} damaged {pirate.name} by {damage}!")
        else:
            print(f"{self.name} missed!")
        return self

    @classmethod
    def warCry(cls):
        
        print("Counter!")

    # def attBoost(cls):
