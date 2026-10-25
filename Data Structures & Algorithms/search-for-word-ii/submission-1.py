class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        MAX_ROW = len(board) - 1
        MAX_COL = len(board[0]) - 1

        root = TrieNode()
        for i, word in enumerate(words):
            node = root
            for c in word:
                if c in node.children:
                    node = node.children[c]
                else:
                    newNode = TrieNode()
                    node.children[c] = newNode
                    node = newNode
            node.index = i

        res = []
        
        def dfs(i, j, node):
            if i < 0 or i > MAX_ROW or j < 0 or j > MAX_COL or board[i][j] == "*" or board[i][j] not in node.children: 
                return
            
            letter = board[i][j]
            newNode = node.children[letter]
            if newNode.index != -1:
                res.append(newNode.index)
                newNode.index = -1
            board[i][j] = "*"
            for di, dj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                dfs(di, dj, newNode)
            board[i][j] = letter
            if not newNode.children:
                del node.children[letter]

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root)

        return [words[i] for i in res]

        
            


        