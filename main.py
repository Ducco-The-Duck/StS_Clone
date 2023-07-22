import numpy as np
import enemies as nmy
from game_manager import GameManager
from characters import Player


player = Player()
game_manager = GameManager(player)
enemy_list = [nmy.Rooster]


while True:

    enemy_type = enemy_list[np.random.randint(len(enemy_list))]
    num_enemies = np.random.randint(3) + 1

    enemies = []
    for _ in range(num_enemies):
        enemies.append(enemy_type())

    game_manager.encounter(enemies)
    if player.hp <= 0:
        print('You have died.')
        break
