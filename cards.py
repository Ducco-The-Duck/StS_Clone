
class Card:

    def __init__(self, name='Dummy Card', desc='This is a dummy card.'):
        self.name = name
        self.desc = desc
        self.tags = []


class AttackCard(Card):

    def __init__(self, name='Dummy Attack Card', desc='This is a dummy attack card.'):
        super().__init__(name, desc)
        self.tags = []


class SkillCard(Card):

    def __init__(self, name='Dummy Skill Card', desc='This is a dummy skill card.'):
        super().__init__(name, desc)
        self.tags = []






