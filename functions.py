# 1.Створи функцію, яка приймає параметри start та end, підсумовує всі цілі числа від значення start до величини end включно. Якщо користувач задасть перше число більше, ніж друге, поміняй їх місцями
# 2. Створи функцію, яка відображає число секунд у вигляді дні:години:хвилини:секунди. Функція може прийняти число як рядок так і як ціле число.
# 3.Створи три функції, які обчислюють суму чисел у списку
# - з for-циклом
# - з while-циклом
# ##################################
start = int(input("give me start"))
stop = int(input("give me stop"))
def sum_number(start, stop):
    print(f"step = 1 default ")
    if start > stop:
        a = stop
        b = start
    else:
        a = start
        b = stop
    seq = sum(range(a, b+1))
    return seq
print(sum_number(start,stop))
#########################################
second_data = int(input("write a second")) # рахуй цілочислельним діленням та залишком від ділення


def day_in_year(seq):
    second_value = seq % 60
    seq = seq - second_value
    while seq >= 60:
        if seq >= 86400:
            day_value = seq // 86400
            seq = seq - (day_value * 86400)
        if seq >= 3600:
            hour_value = seq // 3600
            seq = seq - (hour_value * 3600)
        if seq >= 60:
            minutes_value = seq // 60
            seq = seq - (minutes_value * 60)
        else: break
    return print(f'{day_value}:{hour_value}:{minutes_value}:{second_value}')


print(day_in_year(second_data))
###############################################################
data_list = []
for el in range(1,26):
    data_list.append(el)
print(data_list)


def total_list_for(seq):
    total = 0
    for el in seq:
        total = total + el
    return total
print(total_list_for(data_list))


def total_list_while(list):
    total = 0
    while len(list) > 0:
        total += list.pop()
    return total


print(total_list_while(data_list))


# def recursion(number, index=0):
#     if index >= len(number):
#         return 0
#     else:
#         return number[index] + recursion(number, index+1)
#
#
# print(recursion(data_list))
# ###################################################################
# numb = int(input("write a number for fibonachi"))
# dict_fib = {0: 0, 1: 1}
#
#
# def fib(n):
#     if n in dict_fib:
#         return dict_fib[n]
#     dict_fib[n] = fib(n - 1) + fib(n - 2)
#     return dict_fib[n]
# print(fib(numb))
##################################################################
def main_decor_sandwich(func):
    print(f'Decorating function')


def decorator_tomatos():
    print(f"Помідор")


def decorator_meat():
    print(f"м'ясо")


def decorator_chees():
    print(f"Сир")


def decorator_bread():
    print(f"Хліб")



@main_decor_sandwich
def main_func():
    return None
