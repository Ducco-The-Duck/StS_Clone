import inspect
import cards.base
import cards.juggler


class Player:

    def __init__(self, name, hp, cards_folder):
        self.name = name
        self.hp = hp
        self.armour = 0
        self.vuln_turns = 0
        self.cards = self._gen_cards(cards_folder)

    @staticmethod
    def _gen_cards(cards_folder):
        cards_list = []
        for name, obj in inspect.getmembers(cards_folder):
            if name == 'attack_cards' or name == 'skill_cards':
                for n, ob in inspect.getmembers(obj):
                    if inspect.isclass(ob) and n != 'AttackCard' and n != 'SkillCard':
                        cards_list.append(ob)
        return cards_list


class TheJuggler(Player):

    def __init__(self):
        super().__init__('The Juggler', 72, cards.juggler)
        print(self.cards)


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