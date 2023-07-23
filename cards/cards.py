
class Card:

    def __init__(self, name='Dummy Card', desc='This is a dummy card.', cost=0):
        self.name = name
        self.desc = desc
        self.cost = cost
        self.tags = []


class AttackCard(Card):

    def __init__(self, name='Dummy Attack Card', desc='This is a dummy attack card.', cost=0):
        super().__init__(name, desc, cost)


class SkillCard(Card):

    def __init__(self, name='Dummy Skill Card', desc='This is a dummy skill card.', cost=0):
        super().__init__(name, desc, cost)






