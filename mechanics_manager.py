from random import shuffle
from cards.cards import *


class MechanicsManager:

    def __init__(self, combat_manager):
        self.cm = combat_manager

        # Mechanics switches.
        self.knives = False

    def play(self, hand_index):
        action = self.cm.hand[hand_index]
        if action.cost <= self.cm.mana:
            self.cm.mana -= action.cost
            if action.on_play(self.cm):
                del action
                return True

            # If chosen card is an Attack
            if 'attack' in action.types:

                # Knife triggers
                if self.knives:
                    if self.knife_trigger():
                        del action
                        return True

            if 'purge' in action.keywords:
                if self.purge(hand_index, self.cm.hand):
                    del action
                    return True
            else:
                if self.discard(hand_index):
                    del action
                    return True

        else:
            print('You dont have enough mana to play this.')
        del action

    def draw(self, draw_index=-1):
        if not self.cm.draw_pile:
            print('Reshuffling discard pile into draw pile.')
            self.cm.draw_pile = self.cm.discard_pile
            self.cm.discard_pile = []
            shuffle(self.cm.draw_pile)
        card = self.cm.draw_pile.pop(draw_index)
        if len(self.cm.hand) <= 10:
            self.cm.hand.append(card)
            if card.on_draw(self.cm):
                del card
                return True

            for buff in self.cm.ongoing_effect_dict['on_draw']:
                print(buff.__name__ + ' triggered!')
                if buff(card):
                    return True
            del card
        else:
            print('Hand is full!')
            self.cm.discard_pile.insert(0, card)
            del card

    def draw_by_type(self, card_type):
        for i, card in enumerate(reversed(self.cm.draw_pile)):
            if card_type in card.types:
                print('Drew a ' + card.name + '!')
                if self.draw(len(self.cm.draw_pile) - 1 - i):
                    return True
                return
        print('You have no ' + card_type + 's in your draw pile.')

    def discard(self, hand_index):
        card = self.cm.hand.pop(hand_index)
        self.cm.discard_pile.insert(0, card)
        if card.on_discard(self.cm):
            del card
            return True
        del card

    def purge(self, index, pile):
        card = pile.pop(index)
        self.cm.purge_pile.insert(0, card)
        if card.on_purge(self.cm):
            del card
            return True
        del card

    def juggle(self, num=1):
        if self.knives:
            print('Juggling ' + str(num) + ' knives.')
            for i, card in enumerate(reversed(self.cm.draw_pile)):
                if isinstance(card, KnifeCard):
                    self.cm.discard_pile.insert(0, self.cm.draw_pile.pop(len(self.cm.draw_pile) - 1 - i))
                    num -= 1
                    if num == 0:
                        return
            print('Not enough knives to Juggle! Couldn\'t juggle ' + str(num) + ' knives.')
        else:
            print('No knives to Juggle!')

    def knife_trigger(self):
        for i, card in enumerate(self.cm.discard_pile):
            if isinstance(card, KnifeCard):
                if self.purge(i, self.cm.discard_pile):
                    return True
                return card.on_trigger(self.cm)

        print('You have no knives in your discard pile.')

    # ======================== Turn off mechanics switch =============================

    def turn_mechanics_off(self):
        self.knives = False
