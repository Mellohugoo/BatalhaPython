import random
import os
from time import sleep
from classes.utils import Color

class Battle:
    def __init__(self, battleId):
        self.player1 = None
        self.player2 = None
        self.battleId = battleId
        self.ready = False
        self.game_running = False
        self.rounds = 0
        self.first_fighter = None
        self.second_fighter = None

    def initiative(self):
        fighters = [self.player1, self.player2]
        self.first_fighter = random.choice(fighters)
        fighters.pop(fighters.index(self.first_fighter))
        self.second_fighter = fighters[0]

    def show_next_turn(self, round):
        round_number = round
        if round_number % 2 == 0:
            current_fighter = self.second_fighter
            enemy_fighter = self.first_fighter
        else:
            current_fighter = self.first_fighter
            enemy_fighter = self.second_fighter

        return current_fighter, enemy_fighter

    #def rounds(self):
        # Control the rounds of the game
        #first_fighter.show_attributes()
        #second_fighter.show_attributes()
        #print(f"{Color.BOLD}{Color.UNDERLINE}{Color.RED}{current_fighter.name.upper()}'s TURN{Color.ENDC}")
        #action = current_fighter.show_options()
        #if action == "1":
        #    damage_received = enemy_fighter.take_damage(current_fighter.generate_attack())
        #    print(f"{enemy_fighter.name} received {damage_received} damage.")
        #    sleep(3)
        #if current_fighter.move != None:
        #    action = current_fighter.move
        #    if action == "1":
        #        damage_received = enemy_fighter.take_damage(current_fighter.generate_attack())
        #        print(f"{enemy_fighter.name} received {damage_received} damage.")
        #        if not enemy_fighter.still_alive():
        #            print(f"{current_fighter.name} Wins")
        #            self.game_running = False
        #            break
        #    round_number += 1
        #else:
        #    print("Waiting for player action")
        #    sleep(5)
