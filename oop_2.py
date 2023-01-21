import random
import time
import logging
import unittest


def init_logger(name):
    logger = logging.getLogger(name)
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.ERROR)
    fh = logging.FileHandler(filename='work_log')
    fh.setFormatter(logging.Formatter(FORMAT))
    fh.setLevel(logging.INFO)
    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.debug('logger was initialized')


init_logger('root')


class TestBuiltins(unittest.TestCase):

    def test_Unit(self):
            self.assertEqual(Unit.population, Unit.population_red + Unit.population_blue)
            logging.info(f'Testing')

if __name__ == '__main__':
    unittest.main()


class Unit:
    population = 0
    population_red = 0
    population_blue = 0

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
        hit = self.attack-enemy.armor
        enemy.hp -= hit
        if self.name == 'Mage':
            self.attack -= 100
        print(f'The enemy has taken damage {hit} and have {enemy.hp} hp')

    def death(self, item):
        if self.hp <= 0:
            print(f'the enemy was defeated {self.name}')
            item.remove(self)
            Unit.population -= 1
            if item == red:
                Unit.population_red -= 1
            else:
                Unit.population_blue -= 1
            param = len(item)
            logging.info(f'unit defeated {self.name} in {item}')
            return param

    def war(item_1, item_2):
        forses = [item_1, item_2]
        print(f'The start of the battle')
        time.sleep(5)
        fight = True
        while fight:
            choice = random.choice(forses)
            if choice == item_1:
                for el in item_1:
                    if el.name == 'Mage':
                        Mage.fire(el)
                    enemy = random.choice(item_2)
                    el.do_attack(enemy)
                    enemy.death(item_2)
                    print(f'Blue team unit > {Unit.population_blue=}')
                    if len(item_2) == 0:
                        print(f'Victori Red team')
                        fight = False
                        logging.info(f'The war is over')
                        break
            else:
                for el in item_2:
                    enemy = random.choice(item_1)
                    el.do_attack(enemy)
                    enemy.death(item_1)
                    print(f'Red team unit > {Unit.population_red=}')
                    if len(item_1) == 0:
                        print(f'Victori Blue team')
                        fight = False
                        logging.info(f'The war is over')
                        break

    def kaput(army, item_1, item_2):
        forse = [item_1, item_2]
        unit = ['Knight', 'Archer', 'Mage']
        left = 0
        while True:
            if left == army:
                logging.info(f'unit sorting is finished')
                break
            else:
                choise = random.choice(forse)
                unit_choise = random.choice(unit)
                left += 1
                if choise == item_1:
                    Unit.population_red += 1
                    if unit_choise == 'Knight':
                        item_1.append(Knight('Knight', 100, 300, 75))
                        logging.info(f'in red team unit Knight was created')
                    elif unit_choise == 'Archer':
                        item_1.append(Archer('Archer', 75, 150, 50))
                        logging.info(f'in red team unit Archer was created')
                    else:
                        item_1.append(Mage('Mage', 200, 100, 25, 1000))
                        logging.info(f'in red team unit Mage was created')
                elif choise == item_2:
                    Unit.population_blue += 1
                    if unit_choise == 'Knight':
                        item_2.append(Knight('Knight', 100, 300, 75))
                        logging.info(f'In blue team unit Knight was created')
                    elif unit_choise == 'Archer':
                        item_2.append(Archer('Archer', 75, 150, 50))
                        logging.info(f'in blue team unit Archer was created')
                    else:
                        item_2.append(Mage('Mage', 200, 100, 25, 1000))
                        logging.info(f'in blue team unit Mage was created')
        print(f'{item_1=}')
        print(f'{item_2=}')
        return item_1, item_2


class Knight(Unit):
    population = 0

    def __init__(self, name, attack, hp, armor):
        self.name: str = name
        self.attack = attack
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        Knight.population += 1
        Unit.population += 1


class Archer(Unit):
    population = 0

    def __init__(self, name, attack, hp, armor):
        self.name: str = name
        self.attack = attack
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        Archer.population += 1
        Unit.population += 1


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
        Unit.population += 1

    def fire(self):
        if self.mana <= 100:
            print(f'U need more mana')
            pass
        else:
            print(f'Mage use fireball')
            bonus_at = 100
            self.mana -= 100
            self.attack = self.attack + bonus_at


red = []
blue = []
battel = int(input(f'write how much unit are fighting in battle. Give me a number.'))
Unit.kaput(battel, red, blue)
population_red = len(red)
population_blue = len(blue)
print(f'{red=} \n',
      f'{blue=} \n',
      f'{population_red=} \n',
      f'{population_blue=} \n',
      f'{Unit.population=}')
Unit.war(red, blue)
