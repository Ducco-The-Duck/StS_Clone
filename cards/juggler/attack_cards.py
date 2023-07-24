from cards.cards import AttackCard
import numpy as np


class KnifeToss(AttackCard):

    def __init__(self):
        super().__init__('Knife Toss',
                         'Deal 7 damage to an enemy.',
                         1)
        self.damage = 7
        self.tags = ['targetable']

    def effect(self, player, enemies, game_manager, target):
        print('The Juggler uses Knife Toss.')
        if game_manager.deal_damage(player, enemies[target], self.damage):
            return True


class Knife(AttackCard):

    def __init__(self):
        super().__init__('Knife',
                         'Deal 3 damage to an enemy. Draw a card. Purge.',
                         0)
        self.damage = 3
        self.tags = ['targetable', 'knife', 'token', 'purge']

    def effect(self, player, enemies, game_manager, target):
        print('The Juggler uses Knife.')
        if game_manager.deal_damage(player, enemies[target], self.damage):
            return True
        game_manager.draw()

    def trigger_effect(self, player, enemies, game_manager):
        print('Knife triggered!')
        if game_manager.deal_damage(player, enemies[np.random.randint(len(enemies))], self.damage):
            return True


class HeadsYouLose(AttackCard):

    def __init__(self):
        super().__init__('... Heads, you lose',
                         'Deal 6 damage to an enemy. Trigger a knife. Draw a card. Purge.',
                         0)
        self.damage = 6
        self.tags = ['targetable', 'knife', 'token', 'purge']

    def effect(self, player, enemies, game_manager, target):
        print('The Juggler uses ... Heads, you lose.')
        if game_manager.deal_damage(player, enemies[target], self.damage):
            return True
        game_manager.knife_trigger()
        game_manager.draw()

    def trigger_effect(self, player, enemies, game_manager):
        print('Knife triggered!')
        if game_manager.deal_damage(player, enemies[np.random.randint(len(enemies))], self.damage):
            return True
        game_manager.knife_trigger()
