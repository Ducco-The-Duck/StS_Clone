A Slay the Spire Clone on the Terminal

glossary/card_library.md contains the library of all cards.  
glossary/enemy_library.md contains the library of all enemies.

Current Functionality:
1. Combat has 4 phases; start of turn, turn, end of turn and enemy turn.
1. Players can use cards for various effects.
2. Players have a deck, and have a functional draw pile, hand, discard pile and purge pile during combat.
3. Some cards allow tutoring via type, and can shuffle cards into your deck during combat.
4. Players have a mana pool, and cards cost mana.
4. Enemies can deal damage and apply debuffs to the player.
5. Players and enemies can die, ending encounters and starting next ones. The state of the player (i.e. hp) is preserved between combats.
6. Checks for death happen after all damage instances now, rather than at the end of each combat phase.
7. Cards are divided into two types, have tags such as 'targetable' and each character has an associated list of cards.
7. There is one playable character: The Juggler.
8. Knives and Juggling are mechanics associated with the Juggler.

Features to be added:
1. ~~Hand size limit (important)~~
2. ~~Viewing deck, discard pile, draw pile etc. (important)~~
3. Non combat elements of the game
4. More cards
5. More characters
6. More enemies

## Mechanics
### Blocking with Armour
Units can gain armour, which takes damage before their hp. Units lose armour at the end of their turns.

### Vulnerability and Strength
Vulnerable units take 50% more damage from attacks. Strength grants added damage to the unit's attacks.

### Discarding Cards
Discarding a card removes it from its pile and puts it at the top of the discard pile.

### Purging Cards
Purging a card removes it from the combat. It enters the purge pile.

### Manifesting Cards
Manifesting a card adds a card to your draw pile, hand or discard pile.

### Knives and Juggling
Knives are 0 mana attacks which deal damage, draw a card and purge. When a knife is drawn, it is discarded and a card is drawn.
When an attack is played, knives trigger from the discard pile, dealing damage to a random enemy. Knife damage counts as attack damage, even if triggered.

Juggling once moves a knife from the draw pile to the discard pile.