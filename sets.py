data_analysis_1 = input('write first data for analys')
data_analysis_2 = input('write second data for analys')
analys_letters_set_1 = {el for el in data_analysis_1 if el.isalpha() and el.isupper() or el.islower()}
analys_letters_set_2 = {el for el in data_analysis_2 if el.isalpha() and el.isupper() or el.islower()}
matches_letter_set = analys_letters_set_1 & analys_letters_set_2
analys_number_set_1 = {el for el in data_analysis_1 if el.isdigit()}
analys_number_set_2 = {el for el in data_analysis_2 if el.isdigit()}
difference_number_set = analys_number_set_1 ^ analys_number_set_2
print(f"match letter in data {matches_letter_set}")
print(f"difference number in data {difference_number_set}")
######################################################################################################
# set_a = {1,2,3,4,5}
# set_b = {4,5,6,7,8}
# set_c = {7,8,9,10}
# set_a -= set_b | set_c
# print(set_a)
# set_a |= set_b | set_c
# print(set_a)
# set_a &= set_b & set_c
# print(set_a)
# set_a ^= set_b
# print(set_a)
#####################################################################################################






