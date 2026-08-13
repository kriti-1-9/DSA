class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def is_magic_square(i, j):
            # Check all numbers are 1-9 and distinct
            seen = set()
            for x in range(3):
                for y in range(3):
                    num = grid[i + x][j + y]
                    if num < 1 or num > 9 or num in seen:
                        return False
                    seen.add(num)
            
            # Magic constant must be 15 for 1-9 distinct
            MAGIC = 15
            
            # Check all rows
            for x in range(3):
                if (grid[i + x][j] + grid[i + x][j + 1] + grid[i + x][j + 2]) != MAGIC:
                    return False
            
            # Check all columns
            for y in range(3):
                if (grid[i][j + y] + grid[i + 1][j + y] + grid[i + 2][j + y]) != MAGIC:
                    return False
            
            # Check both diagonals
            if (grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]) != MAGIC:
                return False
            if (grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2]) != MAGIC:
                return False
            
            return True
        
        # Check all possible 3x3 subgrids
        for i in range(rows - 2):
            for j in range(cols - 2):
                if is_magic_square(i, j):
                    count += 1
        
        return count