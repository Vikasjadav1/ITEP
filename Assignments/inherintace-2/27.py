'''
27. Game Character Attack System
Problem Statement

Game characters attack differently.

Create:

abstract class Character

Child:

Archer
Warrior
Mage
'''

from abc import ABC, abstractmethod

class Character(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass


class Archer(Character):

    def attack(self):
        print(self.name, "attacks using Bow and Arrow!")


class Warrior(Character):

    def attack(self):
        print(self.name, "attacks using Sword!")


class Mage(Character):

    def attack(self):
        print(self.name, "attacks using Magic Spell!")

archer = Archer("Robin")
warrior = Warrior("Thor")
mage = Mage("Merlin")

characters = [archer, warrior, mage]

for character in characters:
    character.attack()