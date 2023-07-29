from enemies.enemies import Enemy
import numpy as np


class MutantBrawler(Enemy):

    def __init__(self):
        super().__init__('Mutant Brawler', 74 + np.random.randint(3))
        self.prepared = False

    def punch(self, combat_manager):
        damage = 8
        self.deal_damage(combat_manager.player, damage)
        return combat_manager.resolution_check()

    def slam(self, combat_manager):
        damage = 20
        recoil = 5
        self.deal_damage(combat_manager.player, damage)
        self.deal_damage(self, 5)
        return combat_manager.resolution_check()

    def prepare(self):
        self.prepared = True

    def deflect(self, combat_manager):
        armour = 6 + self.strength * 3
        self.strength = 0
        self.self_armour(armour)
        return combat_manager.resolution_check()

    def take_action(self, combat_manager):

        if self.hp/self.max_hp <= 0.6 and not self.prepared:
            return self.prepare()

        if self.prepared:
            self.prepared = False
            return self.slam(combat_manager)
        else:
            if self.strength < 5:
                return self.punch(combat_manager)
            else:
                return self.deflect(combat_manager)

    def on_start_turn(self, combat_manager):
        self.strength += 1
        if self.prepared:
            prep_armour = 15
            self.self_armour(prep_armour)
