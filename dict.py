# alphabet = {chr(i): i for i in range (1,127)}
# print(alphabet)
#############################################################################
dict_1 = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}
step = 4
ecrypted = []
letter = list(input("write a letter"))
for el in letter:
    ecrypted.append(dict_1.get(el))
data_ecrypted = ""
for el in ecrypted:
    if el + step > 25:
        for key, value in dict_1.items():
            if el + step - 26 == value:
                data_ecrypted += key
    else:
        for key, value in dict_1.items():
            if el + step == value:
                   data_ecrypted += key
print(ecrypted)
print(data_ecrypted)
#########################################################################
# alphabet = '' ###############################  не домашка ( експерименти) >>>>>>>>>>>>
# for i in range(ord('a'), ord('z')+1):
#     alphabet += chr(i)
# alphabet_dict = {alphabet.index(i): i for i in alphabet}
# print(alphabet_dict)
# print(alphabet)
# letter = list(input("write a letter") )
# ecrypted = []
# for el in letter:
#     if el == alphabet_dict.values():
#         ecrypted.append(alphabet_dict.key)
# print(ecrypted)
# data_ecrypt = ""
# for el in ecrypted:
#     if el > 25:
#         for key, value in alphabet.items():
#             if el == key:
#                 data_ecrypt += alphabet.keys()
#     else:
#         for ket, value in alphabet.items():
#             if el == key:
#                 data_ecrypt += alphabet.keys()
# print(data_ecrypt)
##############################################################################
