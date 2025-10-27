grid = [
    [1, 5],
    [0, 9]
]

H, W = len(grid), len(grid[0])
directions = [(1,0), (-1,0), (0,1), (0,-1)]

max_score = 0
best_path = []

def dfs(y, x, visited, total, path):
    global max_score, best_path
    # 現在の状態を出力
    print(f"{path} → 合計={total}")

    # 最大値の更新
    if total > max_score:
        max_score = total
        best_path = path[:]

    # 4方向へ探索
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W and (ny, nx) not in visited:
            dfs(ny, nx, visited | {(ny, nx)}, total + grid[ny][nx], path + [(ny, nx)])


print("=== 再帰的DFSで全パターン探索 ===")
for y in range(H):
    for x in range(W):
        start_val = grid[y][x]
        dfs(y, x, {(y, x)}, start_val, [(y, x)])

print("\n🏆 最大合計:", max_score)
print("通った座標:", best_path)