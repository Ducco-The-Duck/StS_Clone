A Slay the Spire Clone on the Terminal

Current Functionality:
1. Players can use cards for various effects.
2. Players have a deck, and have a functional draw pile, hand, discard pile and purge pile during combat.
3. Some cards allow tutoring via type, and can shuffle cards into your deck during combat.
4. Players have a mana pool, and cards cost mana.
4. Enemies can deal damage and apply debuffs to the player.
5. Players and enemies can die, ending encounters and starting next ones. The state of the player (i.e. hp) is preserved between combats.
6. Cards are divided into two types, have tags such as 'targetable' and each character has an associated list of cards.
7. There is one playable character: The Juggler.
8. Knives and Juggling are mechanics associated with the Juggler.

## Mechanics
### Blocking with Armour
Units can gain armour, which takes damage before their hp. Units lose armour at the end of their turns.

### Vulnerability and Strength
Vulnerable units take 50% more damage from attacks. Strength grants added damage to the unit's attacks.

### Knives and Juggling
Knives are 0 mana attacks which deal 3 damage, draw a card and purge. When a knife is drawn, it is discarded and a card is drawn.
When an attack is played, knives trigger from the discard pile, dealing 3 damage to a random enemy. Knife damage counts as attack damage, even if triggered.

Juggling once draws and discards a knife.