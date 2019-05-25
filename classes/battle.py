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
        self.turns = 0
        self.current_fighter = None
        self.enemy_fighter = None

    def initiative(self):
        fighters = [self.player1, self.player2]
        self.current_fighter = random.choice(fighters)
        fighters.pop(fighters.index(self.first_fighter))
        self.enemy_fighter = fighters[0]

    def next_turn(self):
        self.turns += 1
        if self.turns % 2 == 0:
            self.current_fighter = self.enemy_fighter
            self.enemy_fighter = self.current_fighter

    def control_rounds(self):
        if self.player1.move != None and self.player2.move != None:
            self.rounds += 1
            self.player1.move = None
            self.player2.move = None

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
