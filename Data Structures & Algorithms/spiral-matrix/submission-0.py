class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        iMin = 0
        iMax = len(matrix)
        jMin = 0
        jMax = len(matrix[0])
        while len(res) < (len(matrix) * len(matrix[0])):
            for j in range(jMin, jMax):
                res.append(matrix[iMin][j])
            for i in range(iMin + 1, iMax):
                res.append(matrix[i][jMax - 1])
            if iMax - 1 != iMin:
                for j in range(jMax - 2, jMin - 1, - 1):
                    res.append(matrix[iMax - 1][j])
            if jMax - 1 != jMin:
                for i in range(iMax - 2, iMin, -1):
                    res.append(matrix[i][jMin])
            
            iMin += 1
            iMax -= 1
            jMin +=1
            jMax -= 1
        
        return res
        
        