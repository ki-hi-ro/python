def print_ints(int_iterable):
    for x in int_iterable:
        print(x)
    print("消費された後のリスト:", list(int_iterable))

str_list = ['1', '2', '3', '4', '5']

int_map = map(int, str_list)
print_ints(int_map)

int_list = [int(x) for x in str_list]
print_ints(int_list)



