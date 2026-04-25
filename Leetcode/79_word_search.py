class Solution(object):
    def findMatch(self, mat, word, x, y, wIdx):
        wLen = len(word)
        n = len(mat)
        m = len(mat[0])
        if wIdx == wLen:
            return True
        if x < 0 or y < 0 or x >= n or y >= m:
            return False
        if mat[x][y] == word[wIdx]:
            temp = mat[x][y]
            mat[x][y] = '#'
            res = (self.findMatch(mat, word, x-1, y, wIdx+1) or
            self.findMatch(mat, word, x+1, y, wIdx+1) or
            self.findMatch(mat, word, x, y-1, wIdx+1) or
            self.findMatch(mat, word, x, y+1, wIdx+1))
            mat[x][y] = temp
            return res
        return False

    def exist(self, mat, word):
        wLen = len(word)
        n = len(mat)
        m = len(mat[0])
        if wLen > n*m:
            return False
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0]:
                    if self.findMatch(mat, word, i, j, 0):
                        return True
        return False