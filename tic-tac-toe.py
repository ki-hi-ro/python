# プレイヤーを表すクラス
class Player:
    def __init__(self, symbol):
        self.symbol = symbol  # 'X' または 'O'

# 盤面を表示する関数
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

# マスにマークを置く関数
def make_move(board, row, col, symbol):
    if board[row][col] == " ":
        board[row][col] = symbol
        return True
    return False

# 勝者を判定する関数
def check_winner(board, symbol):
    win_conditions = [
        # 横
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # 縦
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        # 斜め
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]
    for condition in win_conditions:
        if all(board[r][c] == symbol for r, c in condition):
            return True
    return False

# 引き分け（満杯）を判定
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# メイン処理
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]  # 空の盤面
    player_x = Player("X")
    player_o = Player("O")
    current_player = player_x

    while True:
        display_board(board)
        print(f"{current_player.symbol}'s turn")

        try:
            row = int(input("Row (0-2): "))
            col = int(input("Col (0-2): "))
        except ValueError:
            print("数字を入力してください。")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("範囲外です。0〜2の数字を入力してください。")
            continue

        if not make_move(board, row, col, current_player.symbol):
            print("そのマスはすでに埋まっています。")
            continue

        if check_winner(board, current_player.symbol):
            display_board(board)
            print(f"{current_player.symbol} wins!")
            break

        if is_full(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = player_o if current_player == player_x else player_x

if __name__ == "__main__":
    main()
