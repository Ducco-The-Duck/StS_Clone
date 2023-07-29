from typing import List, Any, AnyStr


class Card:
    name: str
    desc: str
    cost: int
    tags: List[Any]
    types: List[Any]
    keywords: List[Any]
    rarity: AnyStr

    def __init__(self, name='Card', desc='This is a dummy card.', cost=0):
        self.name = name
        self.desc = desc
        self.cost = cost
        self.tags = []
        self.types = []
        self.keywords = []
        self.rarity = ''

    def on_play(self, combat_manager):
        pass

    def on_draw(self, combat_manager):
        pass

    def on_discard(self, combat_manager):
        pass

    def on_purge(self, combat_manager):
        pass

    def on_manifest(self, combat_manager):
        pass


class TargetableCard(Card):

    def __init__(self, name='Targetable Card', desc='This is a dummy targetable card.', cost=0):
        super().__init__(name, desc, cost)

    @staticmethod
    def pick_target(combat_manager):
        if len(combat_manager.enemies) > 1:
            print('Choose a target')
            target = input('')
            while target not in map(lambda x: str(x), range(len(combat_manager.enemies) + 1)[1:]):
                print('Please choose a valid target (enter 1, 2, 3 ...)')
                target = input('')
            return int(target) - 1
        elif len(combat_manager.enemies) == 1:
            return 0


class KnifeCard(TargetableCard):

    def __init__(self, name='Knife Card', desc='This is a dummy knife card.', cost=0):
        super().__init__(name, desc, cost)
        self.damage = 3
        self.tags = ['targetable', 'token']
        self.types = ['attack']
        self.keywords = ['purge']
        self.rarity = 'token'

    def on_draw(self, combat_manager):
        if combat_manager.mm.discard(-1):
            return True
        if combat_manager.mm.draw():
            return True

    def on_trigger(self, combat_manager):
        pass
