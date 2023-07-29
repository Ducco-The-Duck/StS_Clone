import numpy as np


class Unit:
    
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.armour = 0
        self.vuln_turns = 0
        self.weak_turns = 0
        self.frail_turns = 0
        self.strength = 0
        self.dexterity = 0

    def deal_damage(self, target, damage):
        true_dmg = int((damage + self.strength) * (1 - 0.25 * np.sign(self.weak_turns)))
        target.take_damage(true_dmg)
        print(self.name + ' deals ' + str(true_dmg) + ' damage to ' + target.name + '.')

    def take_damage(self, damage):
        true_dmg = int(damage * (1 + 0.5 * np.sign(self.vuln_turns)))
        if self.armour > 0:
            self.armour -= true_dmg
            if self.armour < 0:
                self.hp += self.armour
        else:
            self.hp -= true_dmg
        print(self.name + ' takes ' + str(true_dmg) + ' damage.')

    def self_armour(self, armour):
        true_armour = int((armour + self.dexterity) * (1 - 0.25 * np.sign(self.frail_turns)))
        self.armour += true_armour
        print(self.name + ' gains ' + str(true_armour) + ' armour.')

    def deal_armour(self, target, armour):
        true_armour = armour
        target.take_armour(true_armour)
        print(self.name + ' grants ' + target.name + ' ' + str(armour) + ' armour.')

    def take_armour(self, armour):
        true_armour = int(armour * (1 - 0.25 * np.sign(self.frail_turns)))
        self.armour += true_armour
        print(self.name + ' gains ' + str(armour) + ' armour.')

    def deal_vuln(self, target, duration):
        target.vuln_turns += (duration + 1) if target.vuln_turns == 0 else duration
        print(self.name + ' applies ' + str(duration) + ' Vulnerable to ' + target.name)

    def ally_vuln(self, target, duration):
        target.vuln_turns += duration
        print(self.name + ' applies ' + str(duration) + ' Vulnerable to ally ' + target.name + '.')

    def deal_str(self, target, strength):
        target.strength += strength
        print(self.name + ' has ' + str(self.strength) + ' Strength (gained ' + str(strength) + ' Strength).')

    def death(self, game_manager):
        pass

    def print_status(self):
        print(self.name + ' Health: ' + str(self.hp))
        if self.armour > 0:
            print(self.name + ' Armour: ' + str(self.armour))
        if self.vuln_turns > 0:
            print('Vulnerable for ' + str(self.vuln_turns) + ' turns')
        if self.strength > 0:
            print(self.name + ' Strength: ' + str(self.strength))
