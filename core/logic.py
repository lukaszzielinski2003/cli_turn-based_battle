import random


class Character:
    """
    A character in the game with health, attack range and healing ability.
    """

    def __init__(self, name: str, hp: int, attack_min: int, attack_max: int, heal: int):
        """
        Creates a new character with given stats.
        """
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.heal_value = heal

    def __str__(self):
        """
        Returns the character's name and current health.
        """
        return f"{self.name} (HP: {self.hp})"

    def reset(self):
        """
        Restores health to the maximum value.
        """
        self.hp = self.max_hp

    def attack(self, opponent: "Character"):
        """
        Deals random damage to the opponent based on attack stats.
        """
        atk = random.randint(self.attack_min, self.attack_max)
        if opponent.hp > 0:
            opponent.hp -= atk
            if opponent.hp <= 0:
                opponent.hp = 0
            print("-----------------------------------------------")
            print(f"{self.name} hit for {atk} damage")
            print(f"{opponent.name} now has {opponent.hp} HP left")
            print("-----------------------------------------------")
        if opponent.hp == 0:
            print(f"{opponent.name} has been defeated")

    def heal(self):
        """
        Restores health points, up to maximum.
        """
        previous_hp = self.hp
        self.hp += self.heal_value
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        healed_amount = self.hp - previous_hp
        if healed_amount > 0:
            print(f"{self.name} healed for {healed_amount} HP.")
        else:
            print(f"{self.name} is already at full health!")
