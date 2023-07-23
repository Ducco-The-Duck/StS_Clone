from cards.cards import AttackCard, SkillCard
import numpy as np


class GameManager:

    def __init__(self, player):
        self.enemies = None
        self.player = player
        self.card_list = self.player.cards

    def start_turn(self):
        self.player.armour = 0

        for enemy in self.enemies:
            enemy.vuln_turns = enemy.vuln_turns - 1 if enemy.vuln_turns > 0 else 0

    def take_action(self):
        choice1 = self.card_list[np.random.randint(len(self.card_list))]()
        choice2 = self.card_list[np.random.randint(len(self.card_list))]()
        choice3 = self.card_list[np.random.randint(len(self.card_list))]()
        play_dict = {choice1.name: choice1, choice2.name: choice2, choice3.name: choice3}
        print('Pick a card: ' + choice1.name + ", " + choice2.name + ", " + choice3.name)

        play = input('')
        while play not in [choice1.name, choice2.name, choice3.name]:
            print('Please enter card choice name.')
            play = input('')
        action = play_dict[play]

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

        del choice1
        del choice2
        del choice3

    def end_turn(self):
        self.player.vuln_turns = self.player.vuln_turns - 1 if self.player.vuln_turns > 0 else 0
        for enemy in self.enemies:
            enemy.armour = 0

    def enemies_turn(self):
        for enemy in self.enemies:
            enemy.take_action(self.player)

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

    def encounter_turn(self):
        self.start_turn()
        if self.resolution_check():
            return False
        self.print_stats()
        self.take_action()
        if self.resolution_check():
            return False
        self.end_turn()
        if self.resolution_check():
            return False
        self.enemies_turn()
        if self.resolution_check():
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
        encounter_on = True
        while encounter_on:
            encounter_on = self.encounter_turn()

        print('The encounter is finished.')
