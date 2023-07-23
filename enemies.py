import numpy as np
from unit import Unit


class Enemy(Unit):

    def __init__(self, name, hp):
        super().__init__(name, hp)


class Rooster(Enemy):

    def __init__(self):
        super().__init__('Rooster', 40 + np.random.randint(6))

    def claw(self, player):
        print('The Roosters claws at you.')
        damage = 8
        self.deal_damage(player, damage)

    def screech(self, player):
        print('The Rooster screeches at you.')
        player.vuln_turns += 1

    def take_action(self, player):
        self.claw(player) if np.random.randint(4) < 3 else self.screech(player)
