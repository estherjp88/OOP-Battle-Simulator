import random

class Hero:

    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name):
        self.name=name
        self.health=random.randint(100,151)
        self.attackPower=random.randint(10,26)

    def attack(self):
        return random.randint(1,self.attackPower)

    def takeDamage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def isAlive(self):
        return self.health > 0