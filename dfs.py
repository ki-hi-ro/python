# 二次元配列（例）
board = [
    [5, 1, 3],
    [2, 9, 4],
    [6, 7, 8]
]

H, W = len(board), len(board[0])
directions = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(y, x, moves_left, visited):
    # 現在地の値
    total = board[y][x]
    if moves_left == 0:
        return total
    
    best = 0
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W and (ny, nx) not in visited:
            best = max(best, dfs(ny, nx, moves_left - 1, visited | {(ny, nx)}))
    return total + best

max_sum = 0
for i in range(H):
    for j in range(W):
        max_sum = max(max_sum, dfs(i, j, 3, {(i, j)}))

print("最大合計:", max_sum)