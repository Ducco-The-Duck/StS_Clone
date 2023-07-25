import enemies.normal as nmy
from combat_manager import CombatManager
from characters import TheJuggler


player = TheJuggler()
combat_manager = CombatManager(player)


while True:

    enemies = [nmy.Roostling(), nmy.Rooster()]

    combat_manager.encounter(enemies)
    if player.hp <= 0:
        print('You have died.')
        break
