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
        print(f"Nome: {self.name}, forca: {self.strenght}, habilidade: {self.ability}, constituicao: {self.constitution}")
        print("Estatisticas do Personagem:")
        print(f"{self.atk} de ataque.")
        print(f"{self.defesa} de defesa.")
        print(f"{self.hp} de HP.")
        print(f"{self.mp} de MP.")
        print(f"{self.luck} de sorte.")

    def take_damage(self, dmg):
        total_damage = dmg - self.defesa
        if total_damage <= 0:
            total_damage = 1
        self.hp -= total_damage

    def generate_attack(self):
        return self.atk + self.weapon_dmg

    def still_alive(self):
        if self.hp <= 0:
            self.deaths += 1
            return False
        return True

    def show_options(self):
        print("1. Atacar")
        print("2.Ver Inventário")
        choice = input("Escolha sua acao: ")
        return choice
