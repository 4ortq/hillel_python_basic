numb_1 = input ("give me number")
y=0
if str.isdigit(numb_1):
        y = int(numb_1)
else:    y = float(numb_1)
print("type operand 1 >>> ", type(y))
numb_2 = input ("give me number")
z = 0
if str.isdigit(numb_2):
        z = int(numb_2)
else:   z = float(numb_2)
print("type operand 2 >>> ", type(z))
work_process = input("what i have to do * / + - **")
if work_process in "*":
        result = y * z
elif work_process in "/":
        result = y / z
elif work_process in "+":
        result = y + z
elif work_process in "-":
        result = y - z
elif work_process in "**":
        result = y ** z
else:  raise Exception("ALARM!!! incorect enter")
division_int_y = str(round(y))
division_int_z = str(round(z))
division_int_result = str(round(result))
print(f" order result >>> {len(division_int_result)} \n "
      f"order z >>> {len(division_int_z)} \n order y >>> {len(division_int_y)}")
print("result >>>", result)
print("type result>>>", type(result))
# division_int_y = str(int(y))
# print("orders numb_1 >>>", len(division_int_y))
# division_int_z = str(int(z))
# print("orders numb_2 >>>", len(division_int_z))
# division_int_result = str(int(result))
# print("orders result >>>", len(division_int_result))
print("comparing type operands operand1-operand2, operand2-result, operand1-result>>>",\
      type(y) == type(z), type(z) == type(result), type(y) == type(result))
#######################################################
