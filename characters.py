import inspect
from unit import Unit
import cards.base.attack_cards
import cards.base.skill_cards
import cards.juggler.attack_cards
import cards.juggler.skill_cards


class Player(Unit):

    def __init__(self, name, hp, cards_folder, deck):
        super().__init__(name, hp)
        self.cards = self._gen_cards(cards_folder)
        self.deck = deck
        self.mana = 3

    @staticmethod
    def _gen_cards(cards_folder):
        cards_list = []
        for n, ob in inspect.getmembers(cards_folder.attack_cards):
            if inspect.isclass(ob) and n != 'AttackCard':
                cards_list.append(ob)
        for n, ob in inspect.getmembers(cards_folder.skill_cards):
            if inspect.isclass(ob) and n != 'SkillCard':
                cards_list.append(ob)
        return cards_list

    def print_status(self):
        print('You have ' + str(self.mana) + ' mana.')
        super().print_status()


class TheJuggler(Player):

    def __init__(self):
        super().__init__('The Juggler', 72, cards.juggler,
                         [
                             cards.juggler.attack_cards.KnifeToss,
                             cards.juggler.attack_cards.KnifeToss,
                             cards.juggler.attack_cards.KnifeToss,
                             cards.juggler.attack_cards.KnifeToss,
                             cards.juggler.skill_cards.Block,
                             cards.juggler.skill_cards.Block,
                             cards.juggler.skill_cards.Block,
                             cards.juggler.skill_cards.Block,
                             cards.juggler.skill_cards.JuggleKnives
                         ])


class TheHighPriestess(Player):

    def __init__(self):
        super().__init__('The High Priestess', 66)


class TheHierophant(Player):

    def __init__(self):
        super().__init__('The Hierophant', 80)


class TheLovers(Player):

    def __init__(self):
        super().__init__('The Lovers', 45)
        self.lover_hp = 45


class TheHangedMan(Player):

    def __init__(self):
        super().__init__('The Hanged Man', 1)


class TheTower(Player):

    def __init__(self):
        super().__init__('The Tower', 88)


class TheFool(Player):

    def __init__(self):
        super().__init__('The Fool', 72)