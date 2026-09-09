class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squareSet = [set() for _ in range(9)]
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                if char != ".":
                    if char in rowSet[i]:
                        return False
                    if char in colSet[j]:
                        return False
                    idx = (i // 3) * 3 + (j // 3)
                    if char in squareSet[idx]:
                        return False
                    rowSet[i].add(char)
                    colSet[j].add(char)
                    squareSet[idx].add(char)
        return True





        