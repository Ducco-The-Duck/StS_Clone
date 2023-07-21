import numpy as np


class Enemy:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class Rooster(Enemy):

    def __init__(self):
        super().__init__('Rooster', 40 + np.random.randint(6))

    def claw(self, player):
        damage = 8
        player.hp -= damage + damage * (0.5 * np.sign(player.vuln_turns))
        print('Rooster clawed player.')

    def screech(self, player):
        player.vuln_turns += 1
        print('Rooster screeched at player.')

    def take_action(self, player):
        self.claw(player) if np.random.randint(4) < 3 else self.screech(player)
