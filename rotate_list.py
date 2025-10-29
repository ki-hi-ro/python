conveyor_belt_sushi = [
    "サーモン",
    "マグロ",
    "いくら",
    "エビ",
    "タコ",
]

print(f'元の回転寿司リスト:' + '\n' + str(conveyor_belt_sushi))

def rotate_sushi_belt(sushi_belt, k, d):
    if d == '左':
        return sushi_belt[k:] + sushi_belt[:k]
    elif d == '右':
        return sushi_belt[-k:] + sushi_belt[:-k]

# Example usage:
k = 1
d = '左'
rotated_belt = rotate_sushi_belt(conveyor_belt_sushi, k, d)
print()
print(f'{d}方向に{k}回転した後のリスト:' + '\n' + str(rotated_belt))

d = '右'
rotated_belt = rotate_sushi_belt(conveyor_belt_sushi, k, d)
print()
print(f'{d}方向に{k}回転した後のリスト:' + '\n' + str(rotated_belt))