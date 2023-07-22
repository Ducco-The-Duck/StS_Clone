import numpy as np


class Enemy:

    def __init__(self, name='Dummy', hp=0, strength=0):
        self.name = name
        self.hp = hp
        self.strength = strength

    @staticmethod
    def damage(player, damage):
        if player.armour > 0:
            player.armour -= damage + damage * (0.5 * np.sign(player.vuln_turns))
            if player.armour < 0:
                player.hp += player.armour
        else:
            player.hp -= damage + damage * (0.5 * np.sign(player.vuln_turns))


class Rooster(Enemy):

    def __init__(self):
        super().__init__('Rooster', 40 + np.random.randint(6))

    def claw(self, player):
        damage = 8
        self.damage(player, damage)
        print('a')

    def screech(self, player):
        player.vuln_turns += 1
        print('b')

    def take_action(self, player):
        self.claw(player) if np.random.randint(4) < 3 else self.screech(player)
