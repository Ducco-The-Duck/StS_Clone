from cards.cards import *
from random import shuffle


class GameManager:

    def __init__(self, player):
        self.enemies = None
        self.player = player
        self.card_list = self.player.cards
        self.deck = self.player.deck
        self.draw_pile = self.deck.copy()
        self.hand = []
        self.discard_pile = []
        self.purge_pile = []
        self.mana = self.player.mana

        # Mechanics switches. Using switches for non-omnipresent mechanics for efficiency.
        self.are_knives_being_used = False

    def start_turn(self):

        for enemy in self.enemies:
            enemy.vuln_turns = enemy.vuln_turns - 1 if enemy.vuln_turns > 0 else 0

        self.player.armour = 0
        for _ in range(5):
            self.draw()
        self.mana = 3

    def take_action(self):
        while True:
            self.print_stats()
            print('You have ' + str(self.mana) + ' mana.')
            hand_msg = 'Your hand is '
            for card in self.hand[:-1]:
                hand_msg += card().name + ', '
            hand_msg += self.hand[-1]().name + '.'
            print(hand_msg)
            print('Please enter a card position, or End Turn, or View Piles.')

            pos = input('')
            while pos not in list(map(lambda x: str(x), range(len(self.hand) + 1)[1:])) + ['End Turn']:
                if pos == 'View Piles':
                    print(self.draw_pile)
                    print(self.hand)
                    print(self.discard_pile)
                    print(self.purge_pile)
                else:
                    print('Please enter card position, or End Turn, or View Piles.')
                pos = input('')
            if pos == 'End Turn':
                break

            pos = int(pos) - 1
            if self.play(pos):
                return True

    def end_turn(self):
        for _ in range(len(self.hand)):
            self.discard(0)
        self.player.vuln_turns = self.player.vuln_turns - 1 if self.player.vuln_turns > 0 else 0

        for enemy in self.enemies:
            enemy.armour = 0

    def enemies_turn(self):
        for enemy in self.enemies:
            if enemy.take_action(self.player, self):
                return True

    # =============== Combat cycle functions end here =================

    def play(self, hand_index):
        action = self.hand[hand_index]()
        if action.cost <= self.mana:
            self.mana -= action.cost
            if action.on_play(self):
                del action
                return True

            # If chosen card is an Attack
            if 'attack' in action.types:

                # Knife triggers
                if self.are_knives_being_used:
                    if self.knife_trigger():
                        del action
                        return True

            if 'purge' in action.keywords:
                if self.purge(hand_index, self.hand):
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
        if not self.draw_pile:
            print('Reshuffling discard pile into draw pile.')
            self.draw_pile = self.discard_pile
            self.discard_pile = []
            shuffle(self.draw_pile)
        card = self.draw_pile.pop(draw_index)
        if len(self.hand) <= 10:
            self.hand.append(card)
            card = card()
            if card.on_draw(self):
                del card
                return True
            del card
        else:
            print('Hand is full!')
            self.discard_pile.insert(0, card)
            del card

    def draw_by_type(self, card_type):
        for i, card in enumerate(reversed(self.draw_pile)):
            if card_type in card().types:
                print('Drew a ' + card().name + '!')
                if self.draw(len(self.draw_pile) - 1 - i):
                    return True
                return
        print('You have no ' + card_type + 's in your draw pile.')

    def discard(self, hand_index):
        card = self.hand.pop(hand_index)
        self.discard_pile.insert(0, card)
        card = card()
        if card.on_discard(self):
            del card
            return True
        del card

    def purge(self, index, pile):
        card = pile.pop(index)
        self.purge_pile.insert(0, card)
        card = card()
        if card.on_purge(self):
            del card
            return True
        del card

    def juggle(self, num=1):
        if self.are_knives_being_used:
            print('Juggling ' + str(num) + ' knives.')
            for i, card in enumerate(reversed(self.draw_pile)):
                if isinstance(card(), KnifeCard):
                    self.discard_pile.insert(0, self.draw_pile.pop(len(self.draw_pile) - 1 - i))
                    num -= 1
                    if num == 0:
                        return
            print('Not enough knives to Juggle! Couldn\'t juggle ' + str(num) + ' knives.')
        else:
            print('No knives to Juggle!')

    def knife_trigger(self):
        for i, card in enumerate(self.discard_pile):
            if isinstance(card(), KnifeCard):
                if self.purge(i, self.discard_pile):
                    return True
                return card().on_trigger(self)

        print('You have no knives in your discard pile.')

    def deal_damage(self, dealer, dealee, damage):
        dealer.deal_damage(dealee, damage)
        return self.resolution_check()

    def gain_armour(self, unit, armour):
        unit.gain_armour(armour)

    def apply_vuln(self, unit, duration):
        unit.increase_vuln(duration)

    def grant_str(self, unit, strength):
        unit.gain_str(strength)

    # =========================== Interaction functions end here ===================

    def print_stats(self):
        print('Player Stats:')
        self.player.print_status()
        print('\nEnemy Stats:')
        for enemy in self.enemies:
            enemy.print_status()

    def resolution_check(self):
        del_index = []
        for i, enemy in enumerate(self.enemies):
            if enemy.hp <= 0:
                del_index.append(i)
                if enemy.death(self):
                    return True
        for i in del_index:
            del self.enemies[i]

        return self.player.hp <= 0 or self.enemies == []

    def combat_start(self):
        self.draw_pile = self.deck.copy()
        self.hand = []
        self.discard_pile = []
        shuffle(self.draw_pile)
        self.turn_mechanics_off()

    def turn_mechanics_off(self):
        self.are_knives_being_used = False

    def encounter_turn(self):
        if self.start_turn():
            return False
        if self.take_action():
            return False
        if self.end_turn():
            return False
        if self.enemies_turn():
            return False
        return True

    def encounter(self, enemies):

        self.enemies = enemies
        del enemies
        msg = 'Your enemy is '
        for enemy in self.enemies[:-1]:
            msg += enemy.name + ', '
        msg += self.enemies[-1].name + '.\n'
        print(msg)
        self.combat_start()
        encounter_on = True
        while encounter_on:
            encounter_on = self.encounter_turn()

        print('The encounter is finished.')
