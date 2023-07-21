import numpy as np


class Enemy:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class Rooster(Enemy):

    def __init__(self):
        super().__init__('Rooster', 40 + np.random.randint(6))

