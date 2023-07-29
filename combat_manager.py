from random import shuffle
from mechanics_manager import MechanicsManager
from ongoing_effect_manager import OngoingEffectManager


class CombatManager:

    def __init__(self, player):
        self.enemies = None
        self.player = player

        # Managers
        self.mm = MechanicsManager(self)
        self.oem = OngoingEffectManager(self)

        # Piles and mana
        self.draw_pile = self.player.deck.copy()
        self.hand = []
        self.discard_pile = []
        self.purge_pile = []
        self.mana = self.player.mana

        # Dict of buffs
        self.ongoing_effect_dict = {'on_draw': []}

    def start_turn(self):

        self.player.vuln_turns = self.player.vuln_turns - 1 if self.player.vuln_turns > 0 else 0
        self.player.armour = 0
        for _ in range(5):
            self.mm.draw()
        self.mana = 3

    def take_action(self):
        while True:
            self.print_stats()
            print('You have ' + str(self.mana) + ' mana.')
            hand_msg = 'Your hand is '
            for card in self.hand[:-1]:
                hand_msg += card.name + ', '
            hand_msg += self.hand[-1].name + '.'
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
            if self.mm.play(pos):
                return True

    def end_turn(self):

        for _ in range(len(self.hand)):
            self.discard_pile.insert(0, self.hand.pop(0))

        for enemy in self.enemies:
            enemy.vuln_turns = enemy.vuln_turns - 1 if enemy.vuln_turns > 0 else 0
            enemy.armour = 0

    def enemies_turn(self):
        for enemy in self.enemies:
            if enemy.take_action(self):
                return True

    # =============== Combat cycle functions end here =================

    def deal_damage(self, dealer, target, damage):
        dealer.deal_damage(target, damage)
        return self.resolution_check()

    def deal_armour(self, dealer, target, armour):
        dealer.deal_armour(target, armour)

    def self_armour(self, armour):
        self.player.self_armour(armour)

    def deal_vuln(self, dealer, target, duration):
        dealer.deal_vuln(target, duration)

    def ally_vuln(self, dealer, target, duration):
        dealer.ally_vuln(target, duration)

    def deal_str(self, dealer, target, strength):
        dealer.deal_str(target, strength)

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
        self.draw_pile = self.player.deck.copy()
        self.hand = []
        self.discard_pile = []
        self.ongoing_effect_dict = {'on_draw': []}
        shuffle(self.draw_pile)
        self.mm.turn_mechanics_off()

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
        del self.hand
        del self.draw_pile
        del self.discard_pile
        del self.enemies
