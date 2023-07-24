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
        player.deal_damage(enemies[target], self.damage)


class Knife(AttackCard):

    def __init__(self):
        super().__init__('Knife',
                         'Deal 3 damage. Draw a card. Discard when drawn. Whenever an attack is played, '
                         'play this from the discard pile.',
                         0)
        self.damage = 3
        self.tags = ['targetable', 'knife', 'token', 'purge']

    def effect(self, player, enemies, game_manager, target):
        print('The Juggler uses Knife.')
        player.deal_damage(enemies[target], self.damage)
        game_manager.draw()

    def effect_upon_attack(self, player, enemies, game_manager):
        print('Knife triggered!')
        player.deal_damage(enemies[np.random.randint(len(enemies))], self.damage)