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
        self.mana = self.player.mana

    def start_turn(self):
        self.player.armour = 0
        self.draw_cards(5)
        self.mana = 3

        return self.resolution_check()

    def take_action(self):
        while True:
            play_dict = []
            print('You have ' + str(self.mana) + ' mana.')
            hand_msg = 'Your hand is '
            for card in self.hand[:-1]:
                obj = card()
                play_dict.append(obj)
                hand_msg += obj.name + ', '
                del obj
            obj = self.hand[-1]()
            play_dict.append(obj)
            hand_msg += obj.name + '.'
            del obj
            print(hand_msg)
            print('Please enter a card position.')

            play = input('')
            while play not in list(map(lambda x: str(x), range(len(self.hand) + 1)[1:])) + ['End Turn']:
                print('Please enter card position, or End Turn.')
                play = input('')
            if play == 'End Turn':
                break
            play = int(play) - 1
            action = play_dict[play]

            if action.cost <= self.mana:
                self.mana -= action.cost
                if 'targetable' in action.tags:
                    if len(self.enemies) > 1:
                        print('Choose a target')
                        target = input('')
                        while target not in map(lambda x: str(x), range(len(self.enemies) + 1)[1:]):
                            print('Please choose a valid target (enter 1, 2, 3 ...)')
                            target = input('')
                        action.effect(self.player, self.enemies, int(target) - 1)
                    elif len(self.enemies) == 1:
                        action.effect(self.player, self.enemies, 0)
                    else:
                        raise "GameManager.enemies length is not positive"
                else:
                    action.effect(self.player, self.enemies)

                if isinstance(action, AttackCard) and self.player.knives > 0:
                    self.player.deal_damage(self.enemies[np.random.randint(len(self.enemies))], self.player.knives_dmg)

                if self.resolution_check():
                    return True

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

    def draw_cards(self, draw_number):
        while draw_number > 0:
            if not self.draw_pile:
                self.draw_pile = self.discard_pile
                self.discard_pile = []
                shuffle(self.draw_pile)
            self.hand.append(self.draw_pile.pop())
            draw_number -= 1

    def discard(self, hand_index):
        self.discard_pile.append(self.hand.pop(hand_index))

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

    def encounter_turn(self):
        self.print_stats()
        if self.start_turn():
            return False
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
