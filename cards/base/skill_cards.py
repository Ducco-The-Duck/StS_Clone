from cards.cards import SkillCard


class Block(SkillCard):

    def __init__(self):
        super().__init__('Block', 'Gain 6 armour.')
        self.armour = 6

    def effect(self, player, enemies):
        print('The Player uses Block.')
        player.armour += self.armour
