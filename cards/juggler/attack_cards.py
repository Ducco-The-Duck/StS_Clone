from cards.cards import *
import numpy as np


class KnifeToss(TargetableCard):

    def __init__(self):
        super().__init__('Knife Toss',
                         'Deal 7 damage to an enemy.',
                         1)
        self.damage = 7
        self.tags = ['targetable']
        self.types = ['attack']
        self.keywords = []
        self.rarity = 'common'

    def on_play(self, combat_manager):
        print('The Juggler uses Knife Toss.')
        return combat_manager.deal_damage(combat_manager.player,
                                          combat_manager.enemies[self.pick_target(combat_manager)],
                                          self.damage)


class Flurry(Card):

    def __init__(self):
        super().__init__('Flurry',
                         'Deal 4 x 2 damage to all enemies.',
                         1)
        self.damage = 4
        self.damage_instances = 2
        self.tags = []
        self.types = ['attack']
        self.keywords = []
        self.rarity = 'common'

    def on_play(self, combat_manager):
        print('The Juggler uses Flurry.')
        for _ in range(self.damage_instances):
            for enemy in combat_manager.enemies[:-1]:
                combat_manager.player.deal_damage(enemy, self.damage)
        if combat_manager.deal_damage(combat_manager.player, combat_manager.enemies[-1], self.damage):
            return True


class Knife(KnifeCard):

    def __init__(self):
        super().__init__('Knife',
                         'Deal 3 damage to an enemy. Draw a card. Purge.',
                         0)

    def on_play(self, combat_manager):
        print('The Juggler uses Knife.')
        if combat_manager.deal_damage(combat_manager.player,
                                      combat_manager.enemies[self.pick_target(combat_manager)],
                                      self.damage):
            return True
        return combat_manager.mm.draw()

    def on_trigger(self, combat_manager):
        print('Knife triggered!')
        return combat_manager.deal_damage(combat_manager.player,
                                          combat_manager.enemies[np.random.randint(len(combat_manager.enemies))],
                                          self.damage)


class HeadsYouLose(KnifeCard):

    def __init__(self):
        super().__init__('... Heads, you lose',
                         'Deal 6 damage to an enemy. Trigger a knife. Draw a card. Purge.',
                         0)
        self.damage = 6

    def on_play(self, combat_manager):
        print('The Juggler uses ... Heads, you lose.')
        if combat_manager.deal_damage(combat_manager.player,
                                      combat_manager.enemies[self.pick_target(combat_manager)],
                                      self.damage):
            return True
        if combat_manager.mm.knife_trigger():
            return True
        return combat_manager.mm.draw()

    def on_trigger(self, combat_manager):
        print('... Heads, you lose triggered!')
        if combat_manager.deal_damage(combat_manager.player,
                                      combat_manager.enemies[np.random.randint(len(combat_manager.enemies))],
                                      self.damage):
            return True
        return combat_manager.mm.knife_trigger()
