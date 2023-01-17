import random
import time



class unit:

    def __init__(self,name, attack, hp, armor):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.max_hp = hp
        self.armor = armor

    def info(self):
        return print(f"{self.hp=},"
                     f"{self.max_hp=}"
                     f"{self.armor=},"
                     f"{self.attack=}")

    def do_attack(self, enemy):
        print(f' {self.name} "attack =>>" {enemy.name}')
        print(f"({self.attack=})", "attack =>>", f"({enemy.armor=})")
        print(f'{self.hp=}/{self.max_hp}     {enemy.hp=}/{enemy.max_hp}')
        hit = self.attack/enemy.armor
        enemy.hp -= hit
        print(f'The enemy has taken damage {hit} and have {enemy.hp} hp')

class Red(unit):
    item_red = []
    population = 0

    def __init__(self, name, attack, hp, armor):
        self.army = Red
        self.name: str = name
        self.attack = attack
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        Red.item_red.append(self)
        Red.population += 1

    def death(self):
        if self.hp <= 0:
            Red.item_red.remove(self)
            Blue.population -= 1
            print(f'the enemy was defeated {self.name}/{self.army}')

class Blue(unit):
    item_blue = []
    population = 0

    def __init__(self, name, attack, hp, armor):
        self.army = Blue
        self.name: str = name
        self.attack = attack
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        Blue.item_blue.append(self)
        Blue.population += 1

    def death(self):
        if self.hp <= 0:
            Blue.item_blue.remove(self)
            Blue.population -= 1
            print(f'the enemy was defeated {self.name}/{self.army}')

# Preparation for distribution/Підготовка до розподілення
Army = ['Red', 'Blue']
unit_army = ['Knight', 'Archer', 'Mage']
army = int(input(f"write how much unit are fighting in battle. Give me a number."))
print(f'unit will be distributed randomly')
check = 0
#Distribution by armies/Розподілення по війскам
while True:
        choise = random.choice(Army)
        unit_choise = random.choice(unit_army)
        check += 1
        if choise == 'Red':
            if unit_choise == 'Knight':
                Knight = Red ('Knight',100,300,75)
                if check == army:
                    break
            elif unit_choise == 'Archer':
                Archer = Red ('Archer',75,150,50)
                if check == army:
                    break
            if unit_choise == 'Mage':
                Mage = Red ('Mage',200,100,25)
                if check == army:
                    break
        elif choise == 'Blue':
            if unit_choise == 'Knight':
                Knight = Blue('Knight',100,300,75)
                if check == army:
                    break
            elif unit_choise == 'Archer':
                Archer = Blue('Archer',75, 150, 50)
                if check == army:
                    break
            elif unit_choise == 'Mage':
                Mage = Blue('Mage',200, 100, 25)
                if check == army:
                    break
#General statistics for the army/Загальна статистика по війску (Кількість та тип)
print(f'{Blue.item_blue=} \n {Blue.population=}')
print(f'{Red.item_red=} \n {Red.population=}')
#Battle cycle/Цикл бою
print(f'The start of the battle')
time.sleep(5)
War = True # внешний виключатель бесконечного цикла
while War:
        choice = random.choice(Army)
        if choice == 'Red':
            for el in Red.item_red:
                enemy = random.choice(Blue.item_blue)
                el.do_attack(enemy)
                enemy.death()
                print(f'Blue team unit > {Blue.population}')
                if Blue.population == 0:
                    print(f'Victori Red team')
                    War = False
                    break
        else:
            for el in Blue.item_blue:
                enemy = random.choice(Red.item_red)
                el.do_attack(enemy)
                enemy.death()
                print(f'Red team unit > {Red.population}')
                if Red.population == 0:
                    print(f'Victori Blue team')
                    War = False
                    break
##################################################################################################