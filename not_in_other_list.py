a_list = ['apple', 'banana', 'cherry', 'date']
b_list = ['banana', 'date', 'fig', 'grape']

not_in_b_list = [item for item in a_list if item not in b_list]
print("Items in a_list not in b_list:", not_in_b_list)