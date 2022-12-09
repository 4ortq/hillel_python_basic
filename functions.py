# 1.Створи функцію, яка приймає параметри start та end, підсумовує всі цілі числа від значення start до величини end включно. Якщо користувач задасть перше число більше, ніж друге, поміняй їх місцями
# 2. Створи функцію, яка відображає число секунд у вигляді дні:години:хвилини:секунди. Функція може прийняти число як рядок так і як ціле число.
# 3.Створи три функції, які обчислюють суму чисел у списку
# - з for-циклом
# - з while-циклом
# - з рекурсією
# Створи функцію яка обчислює числа Фібоначчі. Функція повертає число з послідовності за порядковим номером
# Надрукуй 4 рядки: помідор -> м'ясо -> сир -> хліб, умови:
# Створи 4 функції, кожна друкує свій шар
# Викликай лише одну функцію
# Використай синтаксис декораторів
# Очікуваний результат друку:
# помідор
# м'ясо
# сир
# хліб
# ##################################
# Start = int(input("give me start"))
# Stop = int(input("give me stop"))
# print(f"step = 1 default ")
# if Start > Stop:
#         a = Stop
#         b = Start
# else:
#         a = Start
#         b = Stop
# def sum_number(start, stop):
#     seq = range(start, stop+1)
#     summ = sum(seq)
#     return summ
# print(sum_number(a,b))
#########################################
# Second_data = input("write a second") # рахує як лічільник
# def day_in_year(seq):
#     seq = int(seq)
#     second_value = seq % 60
#     year_value = 0
#     day_value = 0
#     hour_value = 0
#     minutes_value = 0
#     while seq >= 60:
#         if seq >= 3153000:
#             year_value += 1
#             seq = seq - 3153000
#         elif seq >= 86400:
#             day_value += 1
#             seq = seq - 86400
#         elif seq >= 3600:
#             hour_value += 1
#             seq = seq - 3600
#         elif seq >=  60:
#             minutes_value += 1
#             seq = seq - 60
#     return  { "year" : year_value,
#               "day" :day_value,
#               "hour":hour_value,
#               "minutes":minutes_value,
#               "second":second_value }
# print(day_in_year(Second_data))
#######################################
# Second_data = input("write a second") # рахуй цілочислельним діленням та залишком від ділення
# def day_in_year(seq):
#     if type(seq) == str:
#         seq = int(seq)
#     else: pass
#     year_value = 0
#     day_value = 0
#     hour_value = 0
#     minutes_value = 0
#     second_value = seq % 60
#     seq = seq - second_value
#     while seq >= 60:
#         if seq >= 3153000:
#             year_value = seq // 3153000
#             seq = seq - (year_value * 3153000)
#         elif seq >= 86400:
#             day_value = seq // 86400
#             seq = seq - (day_value * 86400)
#         elif seq >= 3600:
#             hour_value = seq // 3600
#             seq = seq - (hour_value * 3600)
#         elif seq >=  60:
#             minutes_value = seq // 60
#             seq = seq - (minutes_value * 60)
#     return  { "year" : year_value,
#               "day" :day_value,
#               "hour":hour_value,
#               "minutes":minutes_value,
#               "second":second_value }
# print(day_in_year(Second_data))
###############################################################
data_list = []
for el in range(1,26):
    data_list.append(el)
print(data_list)
# def total_list_for(seq):
#     total = 0
#     for el in seq:
#         total = total + el
#     return total
# print(total_list_for(data_list))
# def total_list_while(seq):
#     total = 0
#     el = 0
#     while el < len(seq):
#         total = total + seq[el]
#         el = el + 1
#     return total
# print(total_list_while(data_list))
total = 0
def recursion(x):
    global total
    if x >= len(data_list):
       return
    total += data_list[x]
    recursion(x+1)
recursion(0)
print(total)
print(len(data_list))
###################################################################
numb = int(input("write a number for fibonachi"))
dict_fib = {0: 0, 1: 1}
def fib(n):
    if n in dict_fib:
        return dict_fib[n]
    dict_fib[n] = fib(n - 1) + fib(n - 2)
    return dict_fib[n]
print(fib(numb))