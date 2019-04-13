from classes.game import rolar_dados
from classes.game import values_for_enemy
from classes.person import Person
from classes.battle import Battle

# print(rolar_dados(20))

easy = 10 # 3
medium = 15 # 5
hard = 25 # 15
extreme = 40 # 30
boss = 100 # 50


player = Person("Jose Oswaldo",*values_for_enemy(easy))

enemy = Person("Brutus",*values_for_enemy(easy))

battle1 = Battle(player, enemy)

battle1.rounds()
