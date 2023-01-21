import unittest


class TestBuiltins(unittest.TestCase):
    def setUp(self):
        self.digit = 404 - 500 + 200

    def test_sorted(self):
        self.assertEqual(sorted([3, 2, 1]), [1, 2, 3])
        self.assertEqual(sorted([-13, 0, -27]), [-27, -13, 0])

    def test_str(self):
        self.assertEqual(str(self.digit), "104")
        self.assertEqual(str(None), "None")

    def test_int(self):
        self.assertEqual(int("0"), 0)
        self.assertEqual(int(True), 1)
        with self.assertRaises(ValueError):
            int("1.0")

    @unittest.skip("bcs test is not correct")  # .skipIf(), .skipUnless()
    def test_float(self):
        self.assertIsNone(self.digit)

if __name__ == '__main__':
    unittest.main()

# import random
#
#
# class Warrior:
#
#     def __init__(self, name, attack, hp, armor):
#         self.name = name
#         self.attack = attack
#         self.hp = hp
#         self.max_hp = hp
#         self.armor = armor
#
#     def info(self):
#         return print(f"{self.hp=},"
#                      f"{self.max_hp=}"
#                      f"{self.armor=},"
#                      f"{self.attack=}")
#
#     def attack(self, enemy):
#         print(f' {self.name} "attack =>>" {enemy.name}')
#         print(f"({self.attack=})", "attack =>>", f"({enemy.armor=})")
#         print(f'{self.hp=}/{self.max_hp}     {enemy.hp=}/{enemy.max_hp}')
#         hit = self.attack/enemy.armor
#         enemy.hp -= hit
#         print(f'The enemy has taken damage {hit} and have {enemy.hp} hp')
#
#
# class Black(Warrior):
#     item_black = []
#     population = 0
#
#     def __init__(self, name, attack, hp, armor):
#         self.army = Black
#         self.name: str = name
#         self.attack = attack
#         self.hp = hp
#         self.max_hp = hp
#         self.armor = armor
#         Black.item_black.append(self)
#         Black.population += 1
#
#     def death(self):
#         if self.hp <= 0:
#             Black.item_black.remove(self)
#             White.population -= 1
#             print(f'The enemy was defeated {self.name}/{self.army}')
#
#
# class White(Warrior):
#     item_white = []
#     population = 0
#
#     def __init__(self, name, attack, hp, armor):
#         self.army = White
#         self.name: str = name
#         self.attack = attack
#         self.hp = hp
#         self.max_hp = hp
#         self.armor = armor
#         White.item_white.append(self)
#         White.population += 1
#
#     def death(self):
#         if self.hp <= 0:
#             White.item_white.remove(self)
#             White.population -= 1
#             print(f'the enemy was defeated {self.name}/{self.army}')
#
# Army = ['Black', 'White']
# unit_in_army = ['Knight', 'Archer', 'Mage']
# army = int(input(f"Enter the population of army's: "))
# print(f'Units will be randomly added to armys')
# check = 0
#
# while True:
#     choose = random.choice(Army)
#     unit_choice = random.choice(unit_in_army)
#     check += 1
#     if choose == 'Black':
#         if unit_choice == 'Knight':
#             Knight = Black('Knight', 10, 25, 4)
#             if check == army:
#                 break
#         elif unit_choice == 'Archer':
#             Archer = Black('Archer', 7, 15, 2)
#             if check == army:
#                 break
#         if unit_choice == 'Mage':
#             Mage = Black('Mage', 17, 10, 1)
#             if check == army:
#                 break
#     elif choose == 'White':
#         if unit_choice == 'Knight':
#             Knight = White('Knight', 10, 25, 4)
#             if check == army:
#                 break
#         elif unit_choice == 'Archer':
#             Archer = White('Archer', 7, 15, 2)
#             if check == army:
#                 break
#         elif unit_choice == 'Mage':
#             Mage = White('Mage', 17, 10, 1)
#             if check == army:
#                 break
#
# print(f'{White.item_white=} \n {White.population=}')
# print(f'{Black.item_black=} \n {Black.population=}')
#
# print(f'The battle begin!!!')
# War = True
# while War:
#     choose = random.choice(Army)
#     if choose == 'Black':
#         for el in Black.item_black:
#             enemy = random.choice(White.item_white)
#             el.attack(enemy)
#             enemy.death()
#             print(f'White team unit > {White.population}')
#             if White.population == 0:
#                 print(f'Black team WIN!!!')
#                 War = False
#                 break
#     else:
#         for el in White.item_white:
#             enemy = random.choice(Black.item_black)
#             el.attack(enemy)
#             enemy.death()
#             print(f'Black team unit > {Black.population}')
#             if Black.population == 0:
#                 print(f'White team WIN!!!')
#                 War = False
#                 break