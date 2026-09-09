class Solution:
    def solve(self, board: List[List[str]]) -> None:
        MAX_ROW = len(board) - 1
        MAX_COL = len(board[0]) - 1

        def dfs(x, y):
            if board[x][y] == 'O':
                board[x][y] = '#'
            else:
                return
            for x_n, y_n in [
                (x - 1, y),
                (x + 1, y),
                (x, y + 1),
                (x, y - 1)
            ]:
                if (
                    x_n >= 0 
                    and y_n >= 0
                    and x_n <= MAX_ROW
                    and y_n <= MAX_COL
                ):
                    dfs(x_n, y_n)
        
        for x, row in enumerate(board):
            for y, val in enumerate(row):
                if val == 'O' and (
                    x == 0 or y == 0 or x == MAX_ROW or y == MAX_COL
                ):
                    dfs(x, y)

        for x, row in enumerate(board):
            for y, val in enumerate(row):
                if val == 'O':
                    board[x][y] = 'X'
                if val == '#':
                    board[x][y] = 'O'



        

        