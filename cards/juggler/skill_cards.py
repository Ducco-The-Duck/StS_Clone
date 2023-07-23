from cards.cards import SkillCard


class Block(SkillCard):

    def __init__(self):
        super().__init__('Block', 'Gain 6 armour.')
        self.armour = 6

    def effect(self, player, enemies):
        print('The Juggler uses Block.')
        player.armour += self.armour


class JuggleKnives(SkillCard):
    
    def __init__(self):
        super().__init__('Juggle Knives', 'Your next 3 attacks toss a knife, dealing 3 damage to a random enemy.')

    def effect(self, player, enemies):
        player.knives += 3
