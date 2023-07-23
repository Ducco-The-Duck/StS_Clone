from cards.cards import AttackCard


class Slash(AttackCard):

    def __init__(self):
        super().__init__('Slash', 'Deal 8 damage to an enemy.')
        self.damage = 8
        self.tags = ['targetable']

    def effect(self, player, enemies, target):
        print('The Player uses Slash.')
        player.deal_damage(enemies[target], self.damage)


class Bash(AttackCard):

    def __init__(self):
        super().__init__('Bash', 'Deal 10 damage and apply 2 Vulnerable to an enemy.')
        self.tags = ['targetable']
        self.damage = 10
        self.vuln_turns = 2

    def effect(self, player, enemies, target):
        print('The Player uses Bash.')
        player.deal_damage(enemies[target], self.damage)
        enemies[target].vuln_turns += self.vuln_turns
