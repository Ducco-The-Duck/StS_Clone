from cards.cards import AttackCard, SkillCard
import numpy as np
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

        self.are_knives_being_used = False

    def start_turn(self):
        self.player.armour = 0
        for _ in range(5):
            self.draw()
        self.mana = 3

        return self.resolution_check()

    def take_action(self):
        while True:
            print('You have ' + str(self.mana) + ' mana.')
            hand_msg = 'Your hand is '
            for card in self.hand[:-1]:
                hand_msg += card().name + ', '
            hand_msg += self.hand[-1]().name + '.'
            print(hand_msg)
            print('Please enter a card position, or End Turn, or View Piles.')

            play = input('')
            while play not in list(map(lambda x: str(x), range(len(self.hand) + 1)[1:])) + ['End Turn']:
                if play == 'View Piles':
                    print(self.draw_pile)
                    print(self.hand)
                    print(self.discard_pile)
                    print(self.purge_pile)
                else:
                    print('Please enter card position, or End Turn, or View Piles.')
                play = input('')
            if play == 'End Turn':
                break

            play = int(play) - 1
            action = self.hand[play]()

            if action.cost <= self.mana:
                self.mana -= action.cost
                if 'targetable' in action.tags:
                    if len(self.enemies) > 1:
                        print('Choose a target')
                        target = input('')
                        while target not in map(lambda x: str(x), range(len(self.enemies) + 1)[1:]):
                            print('Please choose a valid target (enter 1, 2, 3 ...)')
                            target = input('')
                        action.effect(self.player, self.enemies, self, int(target) - 1)
                    elif len(self.enemies) == 1:
                        action.effect(self.player, self.enemies, self, 0)
                    else:
                        raise "GameManager.enemies length is not positive"
                else:
                    action.effect(self.player, self.enemies, self)

                # If chosen card is an Attack
                if isinstance(action, AttackCard):

                    # Knife triggers
                    if self.are_knives_being_used:
                        self.knife_trigger()

                if self.resolution_check():
                    return True

                if 'purge' in action.tags:
                    self.purge(play, self.hand)
                else:
                    self.discard(play)
            else:
                print('You dont have enough mana to play this.')

    def end_turn(self):
        for _ in range(len(self.hand)):
            self.discard(0)
        self.player.vuln_turns = self.player.vuln_turns - 1 if self.player.vuln_turns > 0 else 0

        return self.resolution_check()

    def enemies_start_turn(self):
        for enemy in self.enemies:
            enemy.armour = 0

        return self.resolution_check()

    def enemies_turn(self):
        for enemy in self.enemies:
            enemy.take_action(self.player)

        return self.resolution_check()

    def enemies_end_turn(self):
        for enemy in self.enemies:
            enemy.vuln_turns = enemy.vuln_turns - 1 if enemy.vuln_turns > 0 else 0

        return self.resolution_check()

    # =============== Combat cycle functions end here =================

    def draw(self, draw_index=-1):
        if not self.draw_pile:
            self.draw_pile = self.discard_pile
            self.discard_pile = []
            shuffle(self.draw_pile)
        card = self.draw_pile.pop(draw_index)
        self.hand.append(card)
        if 'knife' in card().tags:
            self.discard(-1)
            self.draw()
        del card

    def draw_by_type(self, card_type):
        type_dict = {AttackCard: 'Attack', SkillCard: 'Skill'}
        for i, card in enumerate(reversed(self.draw_pile)):
            if isinstance(card(), card_type):
                self.draw(len(self.draw_pile) - 1 - i)
                print('Drew a ' + card().name + '!')
                return
        print('You have no ' + type_dict[AttackCard] + 's in your draw pile.')

    def discard(self, hand_index):
        self.discard_pile.insert(0, self.hand.pop(hand_index))

    def purge(self, index, pile):
        self.purge_pile.insert(0, pile.pop(index))

    def juggle(self, num=1):
        if self.are_knives_being_used:
            print('Juggling ' + str(num) + ' knives.')
            for i, card in enumerate(reversed(self.draw_pile)):
                if 'knife' in card().tags:
                    self.hand.append(self.draw_pile.pop(len(self.draw_pile) - 1 - i))
                    self.discard(-1)
                    # Changes to draw for full hand considerations must change this too
                    num -= 1
                    if num == 0:
                        return
            print('Not enough knives to Juggle! Couldn\'t juggle ' + str(num) + ' knives.')
        else:
            print('No knives to Juggle!')

    def knife_trigger(self):
        for i, card in enumerate(self.discard_pile):
            print(card().name)
            if 'knife' in card().tags:
                card().effect_upon_attack(self.player, self.enemies, self)
                self.purge(i, self.discard_pile)
                return

        print('You have no knives in your discard pile.')

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
        self.print_stats()
        if self.take_action():
            return False
        if self.end_turn():
            return False
        if self.enemies_start_turn():
            return False
        if self.enemies_turn():
            return False
        if self.enemies_end_turn():
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
