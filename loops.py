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
noope = [ ]
glass = [ ]
for index, element in enumerate(object_for_enumerate):
    while element.isdigit():
        numbers += 1
        if numbers == 3:
            print(f"more > 3 numbers. FAIL")
            break
    else:
        if element == " ":
            noope.append(f'{index}')
            numbers = 0
        elif element.isalpha():
            if element == str.upper(element):
                collector_letters.append(f"{element}")
                numbers = 0
                if element in glass_abc:
                    glass.append(f"{element}")
            elif element in glass_abc:
                    glass.append(f"{element}")
        elif element in glass_abc:
                glass.append((f"{element}"))
                numbers = 0
print (f"jobe is done")
print(f"element upper >>> {collector_letters}")
print(f"probel {noope}")
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
#     if str.isdigit(numb_1) == True:
#             y = int(numb_1)
#     elif str.isdigit(numb_1) == False:
#             y = float(numb_1)
#     print("type operand 1 >>> ", type(y))
#     if str.isdigit(numb_2) == True:
#             z = int(numb_2)
#     elif str.isdigit(numb_2) == False:
#             z = float(numb_2)
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
#     if y == int and z == int:
#         result = int
#     elif y == float  and z == float:
#         result = float
#     print("result >>>", result)
#     print("type result>>>", type(result))
#     division_int_y = str(int(y))
#     print("orders numb_1 >>>", len(division_int_y))
#     division_int_z = str(int(z))
#     print("orders numb_2 >>>", len(division_int_z))
#     division_int_result = str(int(result))
#     print("orders result >>>", len(division_int_result))
#     print("comparing type operands operand1-operand2, operand2-result, operand1-result>>>", type(y) == type(z), type(z) == type(result), type(y))