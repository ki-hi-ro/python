from pprint import pprint

two_d_list = [
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]
            ]
pprint(two_d_list, width=20)

my_position = (2, 2) # (row, column)
print(two_d_list[my_position[0]][my_position[1]])

move_direction = (0, -1) # (row_change, column_change)
my_moved_position = tuple(x + y for x, y in zip(my_position, move_direction))
print(two_d_list[my_moved_position[0]][my_moved_position[1]])