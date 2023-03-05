'''
Suppose you are designing a game where players can create and manage characters. 
You want to create a class called Character that represents a single character in the game. Each character should have the following attributes:

name: a string representing the name of the character.
level: an integer representing the level of the character.
health: an integer representing the current health of the character.
strength: an integer representing the strength of the character.
agility: an integer representing the agility of the character.

In addition to these attributes, the Character class should have the following methods:

take_damage(amount): removes the specified amount from the character's health.
heal(amount): adds the specified amount to the character's health.
attack(target): reduces the target character's health by an amount determined by the attacking character's strength and the target character's agility.
is_alive(): returns True if the character's health is greater than 0, False otherwise.

'''

class Character:
    def __init__(self, name, level, health, strength, agility):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
        self.agility = agility

    def take_damage(self, amount):
        self.health -= amount

    def heal(self, amount):
        self.health += amount

    def attack(self, target):
        damage = self.strength - target.agility
        if damage > 0:
            target.take_damage(damage)

    def is_alive(self):
        return self.health > 0

# Create instances of two characters
player1 = Character("Alice", 10, 100, 20, 10)
player2 = Character("Bob", 5, 50, 10, 20)

# Player 1 attacks player 2
player1.attack(player2)

# Check if player 2 is still alive
print(player2.is_alive())

# Heal player 1
player2.heal(10)

# Player 1 attacks player 2 again
player1.attack(player2)

# Check if player 2 is still alive
print(player2.is_alive())
