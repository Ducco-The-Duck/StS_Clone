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

    def on_play(self, game_manager):
        print('The Juggler uses Block.')
        return game_manager.gain_armour(game_manager.player, self.armour)


class JuggleKnives(Card):
    
    def __init__(self):
        super().__init__('Juggle Knives',
                         'Add a Knife to your draw and discard piles each, then Juggle once and draw an attack.',
                         1)
        self.tags = []
        self.types = ['skill']
        self.keywords = ['juggle']
        self.rarity = 'common'

    def on_play(self, game_manager):
        print('The Juggler uses Juggle Knives.')
        pos1 = np.random.randint(len(game_manager.draw_pile)) if game_manager.draw_pile else 0
        pos2 = np.random.randint(len(game_manager.discard_pile)) if game_manager.discard_pile else 0
        game_manager.draw_pile = game_manager.draw_pile[:pos1] + [Knife] + game_manager.draw_pile[pos1:]
        game_manager.discard_pile = game_manager.discard_pile[:pos2] + [Knife] + game_manager.discard_pile[pos2:]
        game_manager.are_knives_being_used = True
        game_manager.juggle()
        game_manager.draw_by_type('attack')


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

    def on_play(self, game_manager):
        print('The Juggler uses Tails, I win...')
        pos1 = np.random.randint(len(game_manager.draw_pile)) if game_manager.draw_pile else 0
        game_manager.draw_pile = game_manager.draw_pile[:pos1] + [HeadsYouLose] + game_manager.draw_pile[pos1:]
        game_manager.are_knives_being_used = True
        return game_manager.gain_armour(game_manager.player, self.armour)
