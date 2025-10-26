# 2Dグリッド上で、どこからスタートしても良い
# DFSで最大合計値を求める

grid = [
    [5, 1, 3],
    [2, 9, 4],
    [6, 7, 8]
]

H, W = len(grid), len(grid[0])
directions = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(y, x, visited):
    total = grid[y][x]
    max_add = 0

    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W and (ny, nx) not in visited:
            add = dfs(ny, nx, visited | {(ny, nx)})
            max_add = max(max_add, add)

    return total + max_add

max_score = 0

for y in range(H):
    for x in range(W):
        score = dfs(y, x, {(y, x)})
        max_score = max(max_score, score)

print("最大合計:", max_score)
