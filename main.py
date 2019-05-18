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
    #print("Received ", data)
    if not data:
        print("Disconnecting")
        break
    else:
        if data.ready:
            data.rounds()


#battle1 = Battle(player, enemy)

#battle1.rounds()
