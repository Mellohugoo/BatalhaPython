import random
import os
from time import sleep
from classes.utils import Color

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
        round_number = 1
        while first_fighter.still_alive() or second_fighter.still_alive():
            os.system("clear")
            if round_number % 2 == 0:
                current_fighter = second_fighter
                enemy_fighter = first_fighter
            else:
                current_fighter = first_fighter
                enemy_fighter = second_fighter

            first_fighter.show_attributes()
            second_fighter.show_attributes()
            print(f"{Color.BOLD}{Color.UNDERLINE}{Color.RED}{current_fighter.name.upper()}'s TURN{Color.ENDC}")
            action = current_fighter.show_options()
            if action == "1":
                damage_received = enemy_fighter.take_damage(current_fighter.generate_attack())
                print(f"{enemy_fighter.name} received {damage_received} damage.")
                sleep(3)
            if not enemy_fighter.still_alive():
                print(f"{current_fighter.name} Wins")
                break
            round_number += 1
