from classes.utils import Color

class Person:
    def __init__(self, name, forca, hab, constit):
        self.name = name
        self.strenght = forca
        self.ability = hab
        self.constitution = constit
        self.luck = 10
        self.weapon_dmg = 0
        self.armour_def = 0
        self.deaths = 0
        self.wins = 0
        self.calculate_attributes()

    def calculate_attributes(self):
        self.atk = self.strenght * self.ability
        self.defesa = self.constitution + self.armour_def
        self.hp = self.constitution * self.strenght
        self.max_hp = self.constitution * self.strenght
        self.mp = self.ability * (self.luck // 2)
        self.max_mp = self.ability * (self.luck // 2)

    def show_attributes(self):
        print(f"NAME: {Color.YELLOW}{self.name}{Color.ENDC}")
        print(f"STRENGHT: {self.strenght}| ABILITY: {self.ability}| CONSTITUTION: {self.constitution}")
        print(f"ATK: {self.atk} | DEF: {self.defesa} | LUCK: {self.luck}")
        bar_total_size = 30
        hp_bar_life = round((self.hp / self.max_hp) * bar_total_size)
        hp_bar_dmg = bar_total_size - hp_bar_life
        bar_hp_total = ("█" * hp_bar_life) + (" " * hp_bar_dmg)
        bar_mp = "█" * (self.mp // self.max_mp) * bar_total_size
        print(f"HP: {self.hp}/{self.max_hp} |{Color.GREEN}{bar_hp_total}{Color.ENDC}| MP: {self.mp}/{self.max_mp} |{Color.BLUE}{bar_mp}{Color.ENDC}|")
        print("")

    def take_damage(self, dmg):
        total_damage = dmg - self.defesa
        if total_damage <= 0:
            total_damage = 1
        self.hp -= total_damage
        return total_damage

    def generate_attack(self):
        return self.atk + self.weapon_dmg

    def still_alive(self):
        if self.hp <= 0:
            self.deaths += 1
            return False
        return True

    def show_options(self):
        print(f"{Color.BOLD}1.{Color.ENDC} Atacar    |{Color.BOLD}2.{Color.ENDC} Ver Inventário")
        choice = input("Escolha sua acao: ")
        return choice
