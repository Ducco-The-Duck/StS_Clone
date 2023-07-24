import enemies.normal as nmy
from game_manager import GameManager
from characters import TheJuggler


player = TheJuggler()
game_manager = GameManager(player)


while True:

    enemies = [nmy.Roostling(), nmy.Rooster(), nmy.Roostling()]

    game_manager.encounter(enemies)
    if player.hp <= 0:
        print('You have died.')
        break
