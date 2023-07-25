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

    def on_play(self, game_manager):
        print('The Juggler uses Knife Toss.')
        return game_manager.deal_damage(game_manager.player,
                                        game_manager.enemies[self.pick_target(game_manager)],
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

    def on_play(self, game_manager):
        print('The Juggler uses Flurry.')
        for _ in range(self.damage_instances):
            for enemy in game_manager.enemies[:-1]:
                game_manager.player.deal_damage(enemy, self.damage)
            if game_manager.deal_damage(game_manager.enemies[-1], self.damage):
                return True


class Knife(KnifeCard):

    def __init__(self):
        super().__init__('Knife',
                         'Deal 3 damage to an enemy. Draw a card. Purge.',
                         0)

    def on_play(self, game_manager):
        print('The Juggler uses Knife.')
        if game_manager.deal_damage(game_manager.player,
                                    game_manager.enemies[self.pick_target(game_manager)],
                                    self.damage):
            return True
        return game_manager.mm.draw()

    def on_trigger(self, game_manager):
        print('Knife triggered!')
        return game_manager.deal_damage(game_manager.player,
                                        game_manager.enemies[np.random.randint(len(game_manager.enemies))],
                                        self.damage)


class HeadsYouLose(KnifeCard):

    def __init__(self):
        super().__init__('... Heads, you lose',
                         'Deal 6 damage to an enemy. Trigger a knife. Draw a card. Purge.',
                         0)
        self.damage = 6

    def on_play(self, game_manager):
        print('The Juggler uses ... Heads, you lose.')
        if game_manager.deal_damage(game_manager.player,
                                    game_manager.enemies[self.pick_target(game_manager)],
                                    self.damage):
            return True
        if game_manager.mm.knife_trigger():
            return True
        return game_manager.mm.draw()

    def on_trigger(self, game_manager):
        print('... Heads, you lose triggered!')
        if game_manager.deal_damage(game_manager.player,
                                    game_manager.enemies[np.random.randint(len(game_manager.enemies))],
                                    self.damage):
            return True
        return game_manager.mm.knife_trigger()
