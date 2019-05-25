from classes.game import rolar_dados
from classes.game import values_for_enemy
from classes.person import Person
from classes.battle import Battle
from classes.network import Network
from time import sleep

# print(rolar_dados(20))

easy = 10 # 3
medium = 15 # 5
hard = 25 # 15
extreme = 40 # 30
boss = 100 # 50


my_name = input("Enter your name: ")
#my_name = "Rafa"
player = Person(my_name,*values_for_enemy(easy))

#enemy = Person("Brutus",*values_for_enemy(easy))

n = Network()
while True:
    #print("Sending data")
    data = n.send(player)
    print("Received ", data)
    if data.game_running:
        current, enemy = data.show_next_turn(data.rounds)
        #if data.player1.playerId == player.playerId:
        if player.playerId == current.playerId:
            player.move(player.show_options())
        else:
            print("Waiting for enemy to make a move")
    #    print("I'm player1")
    #else:
    #    print("I'm player2")
    #if not data:
    #    print("Disconnecting")
    #    break
    #else:
    #    if data.ready:
    #        data.rounds()


#battle1 = Battle(0)
#battle1.player1 = player
#battle1.player2 = enemy

#battle1.rounds()
