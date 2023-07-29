import enemies.normal as normal
import enemies.elite as elite
from combat_manager import CombatManager
from characters import TheJuggler


player = TheJuggler()
combat_manager = CombatManager(player)


while True:

    enemies = [elite.MutantBrawler()]

    combat_manager.encounter(enemies)
    if player.hp <= 0:
        print('You have died.')
        break
