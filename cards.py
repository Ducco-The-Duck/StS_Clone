
class Card:

    def __init__(self, name='Dummy Card', desc='This is a dummy card.'):
        self.name = name
        self.desc = desc
        self.tags = []
        self.types = []


class Slash(Card):

    def __init__(self):
        super().__init__('Slash', 'Deal 8 damage to an enemy.')
        self.damage = 8
        self.tags = ['targetable']
        self.types = ['attack']

    def effect(self, player, enemies, target):
        enemies[target].hp -= self.damage


class Block(Card):

    def __init__(self):
        super().__init__('Block', 'Gain 6 armour.')
        self.block = 6
        self.types = ['skill']

    def effect(self, player, enemies):
        player.block += self.block


class Cleave(Card):

    def __init__(self):
        super().__init__('Cleave', 'Deal 8 damage to all enemies.')
        self.damage = 8
        self.types = ['attack']

    def effect(self, player, enemies):
        for enemy in enemies:
            enemy.hp -= self.damage
