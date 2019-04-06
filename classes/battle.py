import random

class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def initiative(self):
        fighters = [self.player1, self.player2]
        first = random.choice(fighters)
        fighters.pop(fighters.index(first))
        second = fighters[0]
        return first, second

    def rounds(self):
        first_fighter, second_fighter = self.initiative()
        while first_fighter.still_alive() or second_fighter.still_alive():

            print(f"{first_fighter.name}'s turn")
            action1 = first_fighter.show_options()
            if action1 == "1":
                second_fighter.take_damage(first_fighter.generate_attack())

            print(f"{second_fighter.name}'s turn")
            action2 = second_fighter.show_options()
            if action2 == "1":
                first_fighter.take_damage(second_fighter.generate_attack())
