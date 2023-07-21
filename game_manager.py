import cards
import numpy as np

class GameManager:

    def __init__(self, player):
        self.enemies = None
        self.player = player
        self.card_list = [cards.Slash(), cards.Block(), cards.Cleave()]

    def configure_enemy(self, enemies):
        self.enemies = enemies

    def take_action(self):
        choice1 = self.card_list[np.random.randint(len(self.card_list))]
        choice2 = self.card_list[np.random.randint(len(self.card_list))]
        choice3 = self.card_list[np.random.randint(len(self.card_list))]
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

    def enemies_turn(self):
        for enemy in self.enemies:
            enemy.take_action(self.player)

    def print_stats(self):
        print('Player Stats:')
        print('Health: ' + str(self.player.hp))
        print('Armour: ' + str(self.player.armour))
        if self.player.vuln_turns > 0:
            print('Vulnerable for ' + str(self.player.vuln_turns) + ' turns')
        print('\nEnemy Stats:')
        for enemy in self.enemies:
            print(enemy.name + ' health: ' + str(enemy.hp))

    def end_turn(self):
        self.player.armour = 0
        self.player.vuln_turns = self.player.vuln_turns - 1 if self.player.vuln_turns > 0 else 0
