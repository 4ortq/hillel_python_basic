import random
import time


class Unit:
    population = 0

    def __init__(self, name, attack, hp, armor):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        Unit.population += 1

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
        if self.name == 'Mage':
            self.attack -= 100

    def death(self, item, population):
        if self.hp <= 0:
            item.remove(self)
            Unit.population -= 1
            population -= 1
            print(f'the enemy was defeated {self.name}/{item}')

    def War(item_1, item_2, population_1, population_2):
        forses = [item_1, item_2]
        print(f'The start of the battle')
        time.sleep(5)
        fight = True  # внешний виключатель бесконечного цикла
        while fight:
            choice = random.choice(forses)
            if choice == item_1:
                for el in item_1:
                    enemy = random.choice(item_2)
                    el.do_attack(enemy)
                    enemy.death()
                    print(f'Blue team unit > {population_2=}')
                    if population_2 == 0:
                        print(f'Victori Red team')
                        fight = False
                        break
            else:
                for el in item_2:
                    enemy = random.choice(item_1)
                    el.do_attack(enemy)
                    enemy.death()
                    print(f'Red team unit > {population_1=}')
                    if population_1 == 0:
                        print(f'Victori Blue team')
                        fight = False
                        break


class Knight(Unit):
    population = 0

    def __init__(self, name, attack, hp, armor):
        self.name: str = name
        self.attack = attack
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        Knight.population += 1


class Archer(Unit):
    population = 0

    def __init__(self, name, attack, hp, armor):
        self.name: str = name
        self.attack = attack
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        Archer.population += 1



class Mage(Unit):
    population = 0

    def __init__(self, name, attack, hp, armor, mana):
        self.name: str = name
        self.attack = attack
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        self.mana = mana
        Mage.population += 1

    def fire(self):
        if self.mana <= 100:
            pass
        else:
            bonus_at = 100
            self.mana -= 100
            self.attack = self.attack + bonus_at


def kaput(army, item_1, item_2, pop_1, pop_2):

    forse = [item_1, item_2]
    unit = ['Knight', 'Archer', 'Mage']
    left = 0

    while True:
        choise = random.choice(forse)
        unit_choise = random.choice(unit)
        left += 1
        if choise == item_1:
            if unit_choise == 'Knight':
                item_1.append(Knight('Knight', 100, 300, 75))
                pop_1 += 1
                if left == army:
                    break
            elif unit_choise == 'Archer':
                item_1.append(Archer('Archer', 75, 150, 50))
                pop_1 += 1
                if left == army:
                    break
            if unit_choise == 'Mage':
                item_1.append(Mage('Mage', 200, 100, 25, 1000))
                pop_1 += 1
                if left == army:
                    break
        elif choise == item_2:
            if unit_choise == 'Knight':
                item_2.append(Knight('Knight', 100, 300, 75))
                pop_2 += 1
                if left == army:
                    break
            elif unit_choise == 'Archer':
                item_2.append(Archer('Archer', 75, 150, 50))
                pop_2 += 1
                if left == army:
                    break
            elif unit_choise == 'Mage':
                item_2.append(Mage('Mage', 200, 100, 25, 1000))
                pop_2 += 1
                if left == army:
                    break
    print(f'{item_1=} \n {pop_1=}')
    print(f'{item_2=} \n {pop_2=}')


red = []
blue = []
population_red = 0
population_blue = 0
battel = int(input(f'write how much unit are fighting in battle. Give me a number.'))
kaput(battel, red, blue, population_red, population_blue)
print(  f'{red=} \n',
        f'{blue=} \n',
        f'{population_red=} \n',
        f'{population_blue=} \n',
        f'{Unit.population=}')
