name_1 = input("Tell me your name")
import string
print(name_1)
name_2=str.strip(name_1)
print(name_2)
print("hello", str.capitalize(name_2))
print("hello", string.capwords(name_2))
print("length of string --> ", len(name_2))
print("reverse --> ", name_2[::-1])