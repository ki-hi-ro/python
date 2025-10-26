def smallest(num_list):
  smallest_num = num_list[0]
  for num in num_list:
    if num < smallest_num:
      smallest_num = num
  return smallest_num

num_list = [10, 5, 3, 20, 2, 100000000000, 1]
smallest_num = smallest(num_list)
print(smallest_num)
print(min(num_list))