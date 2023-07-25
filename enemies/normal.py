import numpy as np
from enemies.enemies import Enemy


class Rooster(Enemy):

    def __init__(self):
        super().__init__('Rooster', 40 + np.random.randint(6))

    def claw(self, combat_manager):
        print('The Rooster claws at you.')
        damage = 8
        return combat_manager.deal_damage(self, combat_manager.player, damage)

    def screech(self, combat_manager):
        print('The Rooster screeches at you.')
        duration = 1
        return combat_manager.apply_vuln(combat_manager.player, duration)

    def take_action(self, combat_manager):
        return self.claw(combat_manager) if np.random.randint(4) < 3 else self.screech(combat_manager)


class Roostling(Enemy):

    def __init__(self):
        super().__init__('Roostling', 15 + np.random.randint(3))

    def peck(self, combat_manager):
        print('The Roostling pecks at you.')
        damage = 3
        return combat_manager.deal_damage(self, combat_manager.player, damage)

    def take_action(self, combat_manager):
        return self.peck(combat_manager)

    def death(self, combat_manager):
        strength_gain = 2
        for enemy in combat_manager.enemies:
            if isinstance(enemy, Rooster):
                combat_manager.grant_str(enemy, strength_gain)
