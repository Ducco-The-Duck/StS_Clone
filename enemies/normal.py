import numpy as np
from enemies.enemies import NormalEnemy


class Rooster(NormalEnemy):

    def __init__(self):
        super().__init__('Rooster', 40 + np.random.randint(6))

    def claw(self, player, game_manager):
        print('The Rooster claws at you.')
        damage = 8
        return game_manager.deal_damage(self, player, damage)

    def screech(self, player, game_manager):
        print('The Rooster screeches at you.')
        duration = 1
        return game_manager.apply_vuln(player, duration)

    def take_action(self, player, game_manager):
        return self.claw(player, game_manager) if np.random.randint(4) < 3 else self.screech(player, game_manager)


class Roostling(NormalEnemy):

    def __init__(self):
        super().__init__('Roostling', 15 + np.random.randint(3))

    def peck(self, player, game_manager):
        print('The Roostling pecks at you.')
        damage = 3
        return game_manager.deal_damage(self, player, damage)

    def take_action(self, player, game_manager):
        return self.peck(player, game_manager)

    def death(self, game_manager):
        strength_gain = 2
        for enemy in game_manager.enemies:
            if isinstance(enemy, Rooster):
                game_manager.grant_str(enemy, strength_gain)
