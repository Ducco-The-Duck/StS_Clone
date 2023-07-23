from cards import AttackCard


class Slash(AttackCard):

    def __init__(self):
        super().__init__('Slash', 'Deal 8 damage to an enemy.')
        self.damage = 8
        self.tags = ['targetable']

    def effect(self, player, enemies, target):
        enemies[target].hp -= self.damage


class Cleave(AttackCard):

    def __init__(self):
        super().__init__('Cleave', 'Deal 8 damage to all enemies.')
        self.damage = 8

    def effect(self, player, enemies):
        for enemy in enemies:
            enemy.hp -= self.damage
