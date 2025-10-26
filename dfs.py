grid = [
    [1, 5],
    [0, 9]
]

H, W = len(grid), len(grid[0])
directions = [(1,0), (-1,0), (0,1), (0,-1)]

max_score = 0
best_path = []

print("=== 全パターン ===")
for y in range(H):
    for x in range(W):
        start = grid[y][x]
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W:
                score = start + grid[ny][nx]
                path = [(y, x), (ny, nx)]
                print(f"{path} → 合計={score}")
                if score > max_score:
                    max_score = score
                    best_path = path

print("\n🏆 最大合計:", max_score)
print("通った座標:", best_path)