from cards.cards import SkillCard, AttackCard
from cards.juggler.attack_cards import Knife, HeadsYouLose
import numpy as np


class Block(SkillCard):

    def __init__(self):
        super().__init__('Block',
                         'Gain 6 armour.',
                         1)
        self.armour = 6
        self.tags = []

    def effect(self, player, enemies, game_manager):
        print('The Juggler uses Block.')
        if game_manager.gain_armour(player, self.armour):
            return True


class JuggleKnives(SkillCard):
    
    def __init__(self):
        super().__init__('Juggle Knives',
                         'Add a Knife to your draw and discard piles each, then Juggle once and draw an attack.',
                         1)
        self.tags = []

    def effect(self, player, enemies, game_manager):
        print('The Juggler uses Juggle Knives.')
        pos1 = np.random.randint(len(game_manager.draw_pile)) if game_manager.draw_pile else 0
        pos2 = np.random.randint(len(game_manager.discard_pile)) if game_manager.discard_pile else 0
        game_manager.draw_pile = game_manager.draw_pile[:pos1] + [Knife] + game_manager.draw_pile[pos1:]
        game_manager.discard_pile = game_manager.discard_pile[:pos2] + [Knife] + game_manager.discard_pile[pos2:]
        game_manager.are_knives_being_used = True
        game_manager.juggle()
        game_manager.draw_by_type(AttackCard)


class TailsIWin(SkillCard):

    def __init__(self):
        super().__init__('Tails, I win...',
                         'Add a ... Heads, you lose to your draw pile. Gain 6 armour.',
                         1)
        self.armour = 6
        self.tags = []

    def effect(self, player, enemies, game_manager):
        print('The Juggler uses Tails, I win...')
        pos1 = np.random.randint(len(game_manager.draw_pile)) if game_manager.draw_pile else 0
        game_manager.draw_pile = game_manager.draw_pile[:pos1] + [HeadsYouLose] + game_manager.draw_pile[pos1:]
        game_manager.are_knives_being_used = True
        if game_manager.gain_armour(player, self.armour):
            return True
