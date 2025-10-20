# 行と列を入力してください: 4 4
# 1 1 1 2
# 1 1 2 2
# 1 2 2 2
# 2 2 2 2

class Board:
    def __init__(self):
        self.H, self.W = map(int, input("行と列を入力してください: ").split())
        self.grid = self._read_board()

    def _read_board(self):
        """盤面の読み込み"""
        board = []
        for _ in range(self.H):
            board.append(list(map(int, input().split())))
        return board


class PathFinder:
    def __init__(self, board):
        self.board = board
        self.H = board.H
        self.W = board.W
        self.dp = [[0] * self.W for _ in range(self.H)]

    def compute_max_path_sum(self):
        """動的計画法で最大スコアを求める"""
        self.dp[0] = self.board.grid[0][:]

        for y in range(1, self.H):
            for x in range(self.W):
                candidates = []
                for dx in [-1, 0, 1]:
                    prev_x = x + dx
                    if 0 <= prev_x < self.W:
                        candidates.append(self.dp[y - 1][prev_x])
                self.dp[y][x] = self.board.grid[y][x] + max(candidates)

        return max(self.dp[-1])

    def display_dp_table(self):
        """DPテーブルを可視化"""
        print("\nDPテーブル:")
        for row in self.dp:
            print(*row)


def main():
    board = Board()
    path_finder = PathFinder(board)
    max_score = path_finder.compute_max_path_sum()
    print(f"\n最大スコア: {max_score}")
    path_finder.display_dp_table()


if __name__ == "__main__":
    main()