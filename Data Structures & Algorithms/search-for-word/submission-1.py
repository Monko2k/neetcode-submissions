class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW_MAX = len(board)
        COL_MAX = len(board[0])

        def backtrack(x, y, i):
            if i == len(word):
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
                    and board[x_n][y_n] == word[i]
                ):
                    board[x_n][y_n] = "#"
                    if backtrack(x_n, y_n, i + 1):
                        return True
                    board[x_n][y_n] = word[i]
            return False

        for x, row in enumerate(board):
            for y, c in enumerate(row):
                if c == word[0]:
                    board[x][y] = "#"
                    if backtrack(x, y, 1):
                        return True
                    board[x][y] = c
        return False

