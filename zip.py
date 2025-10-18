num_list = [(1, 'one'), (2, 'two'), (3, 'three')]
for number in zip(*num_list):
    print(number)