import numpy as np
from enemies.enemies import Enemy


class Rooster(Enemy):

    def __init__(self):
        super().__init__('Rooster', 40 + np.random.randint(6))

    def claw(self, combat_manager):
        print('The Rooster claws at you.')
        damage = 8
        self.deal_damage(combat_manager.player, damage)
        return combat_manager.resolution_check()

    def screech(self, combat_manager):
        print('The Rooster screeches at you.')
        duration = 1
        self.deal_vuln(combat_manager.player, duration)

    def take_action(self, combat_manager):
        return self.claw(combat_manager) if np.random.randint(4) < 3 else self.screech(combat_manager)


class Roostling(Enemy):

    def __init__(self):
        super().__init__('Roostling', 15 + np.random.randint(3))

    def peck(self, combat_manager):
        print('The Roostling pecks at you.')
        damage = 3
        self.deal_damage(combat_manager.player, damage)
        return combat_manager.resolution_check()

    def take_action(self, combat_manager):
        return self.peck(combat_manager)

    def death(self, combat_manager):
        strength_gain = 2
        for enemy in combat_manager.enemies:
            if isinstance(enemy, Rooster):
                self.deal_str(enemy, strength_gain)
