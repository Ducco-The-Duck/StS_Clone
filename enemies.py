import numpy as np
from unit import Unit


class Enemy(Unit):

    def __init__(self, name, hp):
        super().__init__(name, hp)


class Rooster(Enemy):

    def __init__(self):
        super().__init__('Rooster', 40 + np.random.randint(6))

    def claw(self, player, game_manager):
        print('The Rooster claws at you.')
        damage = 8
        game_manager.deal_damage(self, player, damage)

    def screech(self, player, game_manager):
        print('The Rooster screeches at you.')
        debuff = 'vulnerable'
        duration = 1
        game_manager.apply_debuff(player, debuff, duration)

    def take_action(self, player, game_manager):
        self.claw(player, game_manager) if np.random.randint(4) < 3 else self.screech(player, game_manager)
