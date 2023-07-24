from unit import Unit


class Enemy(Unit):

    def __init__(self, name, hp):
        super().__init__(name, hp)


class NormalEnemy(Enemy):

    def __init__(self, name, hp):
        super().__init__(name, hp)
