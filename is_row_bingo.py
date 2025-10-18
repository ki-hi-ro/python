card = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
drawn_numbers = {1, 8, 9}

for row_index, row_value in enumerate(card):
    for col in row_value:
        if col in drawn_numbers:
            card[row_index][row_value.index(col)] = "X"

def is_row_bingo(card):
    is_row_bingo = False
    for r in range(len(card)):
        if all(card[r][c] == "X" for c in range(len(card))): is_row_bingo = True
    return is_row_bingo

print(is_row_bingo(card))
