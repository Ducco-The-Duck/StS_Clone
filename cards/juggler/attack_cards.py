from cards.cards import AttackCard
import numpy as np


class KnifeToss(AttackCard):

    def __init__(self):
        super().__init__('Knife Toss', 'Deal 6 damage to an enemy and 2 damage to a random enemy.')
        self.damage = 6
        self.bounce_dmg = 2
        self.tags = ['targetable']

    def effect(self, player, enemies, target):
        print('The Juggler uses Knife Toss.')
        player.deal_damage(enemies[target], self.damage)
        player.deal_damage(enemies[np.random.randint(len(enemies))], self.bounce_dmg)
