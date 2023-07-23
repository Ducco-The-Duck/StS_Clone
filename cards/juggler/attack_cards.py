from cards.cards import AttackCard
import numpy as np


class BallToss(AttackCard):

    def __init__(self):
        super().__init__('Ball Toss', 'Deal 7 damage to an enemy and then 2 to a random enemy.')
        self.damage = 7
        self.bounce_dmg = 2
        self.tags = ['targetable']

    def effect(self, player, enemies, target):
        print('The Juggler uses Ball Toss.')
        player.deal_damage(enemies[target], self.damage)
        player.deal_damage(enemies[np.random.randint(len(enemies))], self.bounce_dmg)


class Cleave(AttackCard):

    def __init__(self):
        super().__init__('Cleave', 'Deal 8 damage to all enemies.')
        self.damage = 8

    def effect(self, player, enemies):
        print('The Juggler uses Cleave.')
        for enemy in enemies:
            player.deal_damage(enemy, self.damage)
