from unit import Unit


class Enemy(Unit):

    def __init__(self, name, hp):
        super().__init__(name, hp)

    def on_start_turn(self, combat_manager):
        pass

    def take_action(self, combat_manager):
        pass

    def on_player_action(self, combat_manager):
        pass

    def on_end_turn(self, combat_manager):
        self.vuln_turns = self.vuln_turns - 1 if self.vuln_turns > 0 else 0
        self.weak_turns = self.weak_turns - 1 if self.weak_turns > 0 else 0
        self.frail_turns = self.frail_turns - 1 if self.frail_turns > 0 else 0
        self.armour = 0