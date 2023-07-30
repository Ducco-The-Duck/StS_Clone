from cards.cards import *
from cards.juggler.attack_cards import Knife, HeadsYouLose
import numpy as np


class Block(Card):

    def __init__(self):
        super().__init__('Block',
                         'Gain 6 armour.',
                         1)
        self.armour = 6
        self.tags = []
        self.types = ['skill']
        self.keywords = []
        self.rarity = 'common'

    def on_play(self, combat_manager):
        print('The Juggler uses Block.')
        return combat_manager.self_armour(self.armour)


class Counterstep(Card):

    def __init__(self):
        super().__init__('Counterstep',
                         'Gain 11 armour. Trigger a knife.',
                         2)
        self.armour = 11
        self.tags = []
        self.types = ['skill']
        self.keywords = []
        self.rarity = 'common'

    def on_play(self, combat_manager):
        print('The Juggler uses Block.')
        if combat_manager.self_armour(self.armour):
            return True
        return combat_manager.mm.knife_trigger()


# class Conceal(Card):
#
#     def __init__(self):
#         super().__init__('Conceal',
#                          'Conceal yourself. End your turn. Draw 1 less and gain 1 less mana next turn.',
#                          1)
#         self.armour = 8
#         self.tags = []
#         self.types = ['skill']
#         self.keywords = []
#         self.rarity = 'common'
#
#     def on_play(self, combat_manager):
#         print('The Juggler uses Block.')
#         if combat_manager.self_armour(self.armour):
#             return True
#         return combat_manager.mm.knife_trigger()


class JuggleKnives(Card):
    
    def __init__(self):
        super().__init__('Juggle Knives',
                         'Manifest a Knife in your draw and discard piles each, then Juggle once and draw an attack.',
                         1)
        self.tags = []
        self.types = ['skill']
        self.keywords = ['juggle']
        self.rarity = 'common'

    def on_play(self, combat_manager):
        print('The Juggler uses Juggle Knives.')
        pos1 = np.random.randint(len(combat_manager.draw_pile)) if combat_manager.draw_pile else 0
        pos2 = np.random.randint(len(combat_manager.discard_pile)) if combat_manager.discard_pile else 0
        combat_manager.mm.manifest(Knife, 'draw', pos1)
        combat_manager.mm.manifest(Knife, 'discard', pos2)
        combat_manager.mm.knives = True
        combat_manager.mm.juggle()
        combat_manager.mm.draw_by_type('attack')


class TailsIWin(Card):

    def __init__(self):
        super().__init__('Tails, I win...',
                         'Manifest a ... Heads, you lose in your draw pile. Gain 6 armour.',
                         1)
        self.armour = 6
        self.tags = []
        self.types = ['skill']
        self.keywords = []
        self.rarity = 'uncommon'

    def on_play(self, combat_manager):
        print('The Juggler uses Tails, I win...')
        pos1 = np.random.randint(len(combat_manager.draw_pile)) if combat_manager.draw_pile else 0
        combat_manager.mm.manifest(HeadsYouLose, 'draw', pos1)
        combat_manager.mm.knives = True
        return combat_manager.self_armour(self.armour)
