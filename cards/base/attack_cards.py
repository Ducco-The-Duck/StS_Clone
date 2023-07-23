from cards.cards import AttackCard


class Slash(AttackCard):

    def __init__(self):
        super().__init__('Slash', 'Deal 8 damage to an enemy.')
        self.damage = 8
        self.tags = ['targetable']

    def effect(self, player, enemies, target):
        print('The Juggler uses Slash.')
        player.deal_damage(enemies[target], self.damage)


class Cleave(AttackCard):

    def __init__(self):
        super().__init__('Cleave', 'Deal 8 damage to all enemies.')
        self.damage = 8

    def effect(self, player, enemies):
        print('The Juggler uses Cleave.')
        for enemy in enemies:
            player.deal_damage(enemy, self.damage)
