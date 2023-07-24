from cards.cards import SkillCard


class Block(SkillCard):

    def __init__(self):
        super().__init__('Block', 'Gain 6 armour.')
        self.armour = 6
        self.tags = []

    def effect(self, player, enemies, game_manager):
        print('The Player uses Block.')
        if game_manager.gain_armour(player, self.armour):
            return True
