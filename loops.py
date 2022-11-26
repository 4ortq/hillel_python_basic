# Створи послідовність інструкцій, у вигляді 1 циклу. Цикл працює один раз. Відповіді виводяться у рядок, у консолі буде роздруковано 3 рядки. Вимоги до кода:
# Приймає від користувача рядок будь-яких символів, наприклад S f-FaGA a
# Друкує усі літери з рядку, які у верхньому регістрі, у прикладі вище це SFGA
# Друкує індекси усіх пробілів, якщо вони є, у прикладі вище це  1, 8
# Друкує усі гласні букви з рядка, у прикладі вище це  aAa
# Якщо у рядку буде послідовність з трьох цифр, наприклад ab-c474f g - цикл переривається та друкується повідомлення про цю подію. Інакше друкується повідомлення про коректне завершення циклу
##############################################################################
object_for_enumerate = input("write somesthing")
collector_letters = [ ]
numbers = 0
glass_abc = "aiouyeAIOYUE"
none = [ ]
glass = [ ]
for index, element in enumerate(object_for_enumerate):
    while element.isdigit():
        numbers += 1
        if numbers == 3:
            print(f"more 3 numbers. WHILE BREAK")
            break
    else:
        if element == " ":
            none.append(f'{index}')
            numbers = 0
        elif element in glass_abc:
            if element.isupper():
                collector_letters.append(f"{element}")
                glass.append(f"{element}")
            else: glass.append(f"{element}")
            numbers = 0
        elif element.isupper():
            collector_letters.append(f"{element}")
            numbers = 0
print (f"jobe is done")
print(f"element upper >>> {collector_letters}")
print(f"probel {none}")
print(f"element glasss >>> {glass}")
############################################################################
# numb_1 = input ("give me number")
# numb_2 = input ("give me number")
# work_process = input("what i have to do * / + - **")
# y=0
# z = 0
# while numb_1 or numb_2 or work_process == "exit":
#     print(f"you are exit")
#     break
# else:
#     if str.isdigit(numb_1):
#             y = int(numb_1)
#     else:   y = float(numb_1)
#     print("type operand 1 >>> ", type(y))
#     if str.isdigit(numb_2):
#             z = int(numb_2)
#     else:   z = float(numb_2)
#     print("type operand 2 >>> ", type(z))
#     if work_process in "*":
#             result = y * z
#     elif work_process in "/":
#             result = y / z
#     elif work_process in "+":
#             result = y + z
#     elif work_process in "-":
#             result = y - z
#     elif work_process in "**":
#             result = y ** z
#     else:  raise Exception("ALARM!!! incorect enter")
#     # if y == int and z == int:
#     #     result = int
#     # elif y == float  and z == float:
#     #     result = float
#     print("result >>>", result)
#     print("type result>>>", type(result))
#     division_int_y = str(int(y))
#     print("orders numb_1 >>>", len(division_int_y))
#     division_int_z = str(int(z))
#     print("orders numb_2 >>>", len(division_int_z))
#     division_int_result = str(int(result))
#     print("orders result >>>", len(division_int_result))
#     print("comparing type operands operand1-operand2, operand2-result, operand1-result>>>", type(y) == type(z), type(z) == type(result), type(y))