import numpy as np


class Unit:
    
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.armour = 0
        self.vuln_turns = 0
        self.strength = 0

    def deal_damage(self, target, damage):
        if target.armour > 0:
            target.armour -= int(damage + self.strength * (1 + 0.5 * np.sign(target.vuln_turns)))
            if target.armour < 0:
                target.hp += target.armour
        else:
            target.hp -= int(damage + self.strength * (1 + 0.5 * np.sign(target.vuln_turns)))
        print(self.name + ' deals damage to ' + target.name + '.')

    def print_status(self):
        print(self.name + ' Health: ' + str(self.hp))
        if self.armour > 0:
            print(self.name + ' Armour: ' + str(self.armour))
        if self.vuln_turns > 0:
            print('Vulnerable for ' + str(self.vuln_turns) + ' turns')