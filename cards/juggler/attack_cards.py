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
                         'Deal 3 damage to an enemy. Draw a card. Discard when drawn. Whenever an attack is played, '
                         'play this from the discard pile.',
                         0)
        self.damage = 3
        self.tags = ['targetable', 'knife', 'token', 'purge']

    def effect(self, player, enemies, game_manager, target):
        print('The Juggler uses Knife.')
        if game_manager.deal_damage(player, enemies[target], self.damage):
            return True
        game_manager.draw()

    def effect_upon_attack(self, player, enemies, game_manager):
        print('Knife triggered!')
        if game_manager.deal_damage(player, enemies[np.random.randint(len(enemies))], self.damage):
            return True
