class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW_MAX = len(board)
        COL_MAX = len(board[0])

        starters = []
        for x, row in enumerate(board):
            for y, c in enumerate(row):
                if c == word[0]:
                    starters.append((x, y))
        def backtrack(x, y, used, w):
            print(x, y, w)
            if len(w) == 0:
                return True
            for x_n, y_n in [
                (x - 1, y),
                (x + 1, y),
                (x , y - 1),
                (x , y + 1),
            ]:
                if (
                    x_n >= 0
                    and x_n < ROW_MAX
                    and y_n >= 0 
                    and y_n < COL_MAX
                    and board[x_n][y_n] == w[0]
                    and used[x_n][y_n] == False
                ):
                    used[x_n][y_n] = True
                    if backtrack(x_n, y_n, used, w[1:]):
                        return True
                    used[x_n][y_n] = False
            return False

        for x, y in starters:
            used = [[False] * len(board[0]) for _ in range(len(board))]
            used[x][y] = True
            if backtrack(x, y, used, word[1:]):
                return True
        return False

