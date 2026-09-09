class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW_MAX = len(board)
        COL_MAX = len(board[0])

        def backtrack(x, y, i):
            if i == len(word):
                return True
            
            if (
                x < 0
                or x >= ROW_MAX
                or y < 0
                or y >= COL_MAX
                or board[x][y] != word[i]
            ):
                return False
            
            board[x][y] = '#'
            for x_n, y_n in [
                (x - 1, y),
                (x + 1, y),
                (x , y - 1),
                (x , y + 1),
            ]:
                if backtrack(x_n, y_n, i + 1):
                    return True
            board[x][y] = word[i]
            return False

        for x, row in enumerate(board):
            for y, c in enumerate(row):
                if c == word[0]:
                    if backtrack(x, y, 0):
                        return True
        return False

