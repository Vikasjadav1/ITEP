'''
20. Gaming Characters
Character
Warrior
SuperWarrior

Add special powers.
'''

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def character_details(self):
        print("Character Name:", self.name)
        print("Health:", self.health)

class Warrior(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def warrior_details(self):
        print("Weapon:", self.weapon)
        print("Warrior Attack!")


class SuperWarrior(Warrior):
    def special_powers(self):
        print("Special Powers:")
        print("1. Fire Attack")
        print("2. Super Strength")
        print("3. Flying Ability")
        print("4. Healing Power")

obj = SuperWarrior("Thor", 100, "Hammer")

obj.character_details()
obj.warrior_details()
obj.special_powers()