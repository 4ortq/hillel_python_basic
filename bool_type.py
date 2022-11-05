result_1:bool=5 !=3
print(result_1)
result_2:bool=5 >= 5
print(result_2)
result_3:bool=5 <= 5
print(result_3)
result_4:bool=5 == 5
print(result_4)
is_true = True or True and False
print(is_true)
is_true= True and True or False
print(is_true)
is_true = True and True is not False
print(is_true)
is_true = True or True is not False
print(is_true)
is_true = True or True or False
print(is_true)
################################
bool_zero = bool(None)
bool_number = bool (7)
r_1 = bool_zero == bool_number
print (bool_zero) # None, 0, False and for any empty sequences
print (bool_number)
print(r_1)
################################
bool_empty = bool( )
bool_number_1 = bool (10-1)
r_2 = bool_empty == bool_number_1
print (bool_empty) # None, 0, False and for any empty sequences
print (bool_number_1)
print(r_2)
################################
bool_1 = bool(True or False)
print(bool_1)
res_3 = print("Have you ever been in Kiev") == bool_1
print(res_3)
################################
type_inf=type(None)
print(type_inf)
id_inf=id(None)
print(id_inf)
bool_type = bool(type(None))
bool_id = bool (id(None))
r_4 = bool_type == bool_id
print (bool_type) # None, 0, False and for any empty sequences
print (bool_id)
print(r_4)
################################