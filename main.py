import numpy as np
import cards
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
    print('Your foe is ' + str(num_enemies) + ' ' + enemies[0].name)
    encounter_ongoing = True

    while encounter_ongoing:
        game_manager.configure_enemy(enemies)
        game_manager.print_stats()
        game_manager.take_action()
        game_manager.end_turn()
        game_manager.enemies_turn()
        encounter_ongoing = False
        for enemy in enemies:
            encounter_ongoing = encounter_ongoing or enemy.hp > 0

