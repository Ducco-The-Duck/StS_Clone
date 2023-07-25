from unit import Unit


class Enemy(Unit):

    def __init__(self, name, hp):
        super().__init__(name, hp)

    def take_action(self, combat_manager):
        pass
