# 深さ優先探索 (DFS) の実装例
# 2次元グリッド上での移動を考え、指定された移動回数内で最大の合計値を求める

board = [
    [5, 1],
    [2, 9]
]

H, W = len(board), len(board[0])
directions = [(1,0), (-1,0), (0,1), (0,-1)] # 下、上、右、左

def dfs(y, x, moves_left, visited, depth=0):
    indent = "  " * depth
    total = board[y][x]
    print(f"{indent}▶ 深さ{depth}: dfs({y},{x}), 残り={moves_left}, total={total}")

    # 移動回数が0なら終了
    if moves_left == 0:
        print(f"{indent}  ↩ 戻る: dfs({y},{x}) → return {total}")
        return total

    best = 0
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W and (ny, nx) not in visited:
            value = dfs(ny, nx, moves_left - 1, visited | {(ny, nx)}, depth + 1)
            print(f"{indent}  [比較中] ({y},{x})→({ny},{nx}) value={value}, best={best}")
            best = max(best, value)
            print(f"{indent}  [更新後] best={best}")

    result = total + best
    print(f"{indent}↩ 戻る: dfs({y},{x}) → total({total}) + best({best}) = {result}")
    return result

print("\n=== 実行開始 ===")
result = dfs(0, 0, 2, {(0, 0)})
print(f"\n最終結果: {result}")