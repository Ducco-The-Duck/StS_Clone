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
        return combat_manager.gain_armour(combat_manager.player, self.armour)


class JuggleKnives(Card):
    
    def __init__(self):
        super().__init__('Juggle Knives',
                         'Add a Knife to your draw and discard piles each, then Juggle once and draw an attack.',
                         1)
        self.tags = []
        self.types = ['skill']
        self.keywords = ['juggle']
        self.rarity = 'common'

    def on_play(self, combat_manager):
        print('The Juggler uses Juggle Knives.')
        pos1 = np.random.randint(len(combat_manager.draw_pile)) if combat_manager.draw_pile else 0
        pos2 = np.random.randint(len(combat_manager.discard_pile)) if combat_manager.discard_pile else 0
        combat_manager.draw_pile = combat_manager.draw_pile[:pos1] + [Knife] + combat_manager.draw_pile[pos1:]
        combat_manager.discard_pile = combat_manager.discard_pile[:pos2] + [Knife] + combat_manager.discard_pile[pos2:]
        combat_manager.mm.knives = True
        combat_manager.mm.juggle()
        combat_manager.mm.draw_by_type('attack')


class TailsIWin(Card):

    def __init__(self):
        super().__init__('Tails, I win...',
                         'Add a ... Heads, you lose to your draw pile. Gain 6 armour.',
                         1)
        self.armour = 6
        self.tags = []
        self.types = ['skill']
        self.keywords = []
        self.rarity = 'uncommon'

    def on_play(self, combat_manager):
        print('The Juggler uses Tails, I win...')
        pos1 = np.random.randint(len(combat_manager.draw_pile)) if combat_manager.draw_pile else 0
        combat_manager.draw_pile = combat_manager.draw_pile[:pos1] + [HeadsYouLose] + combat_manager.draw_pile[pos1:]
        combat_manager.mm.knives = True
        return combat_manager.gain_armour(combat_manager.player, self.armour)
