class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        for each grid: the length means 4-(number of 1 around it)
        be care of the grid on the border, it is around by 0
        """
        nrow = len(grid)
        ncol = len(grid[0])

        if nrow == 1 and ncol == 1:
            return 4 * grid[0][0]
        elif nrow == 1 and ncol != 1:
            length = 0
            length += grid[0][0] * (4 - grid[0][1]) + grid[0][ncol - 1] * (4 - grid[0][ncol - 2])
            for c in range(1, ncol - 1):
                length += grid[0][c] * (4 - grid[0][c - 1] - grid[0][c + 1])
            return length
        elif nrow != 1 and ncol == 1:
            length = 0
            length += grid[0][0] * (4 - grid[1][0]) + grid[nrow - 1][0] * (4 - grid[nrow - 2][0])
            for r in range(1, nrow - 1):
                length += grid[r][0] * (4 - grid[r - 1][0] - grid[r + 1][0])
            return length

        length = 0
        length += (grid[0][0] * (4 - grid[0][1] - grid[1][0])) # grid[0][0]
        for c in range(1, ncol - 1): # grid[0][1] ~ grid[0][ncol-1]
            length += (grid[0][c] * (4 - grid[0][c - 1] - grid[0][c+ 1] - grid[1][c]))
        length += (grid[0][ncol - 1] * (4 - grid[0][ncol - 2] - grid[1][ncol - 1])) # grid[0][ncol]

        for r in range(1, nrow - 1):
            length += (grid[r][0] * (4 - grid[r - 1][0] - grid[r + 1][0] - grid[r][1])) #grid[i][0]
            for c in range(1, ncol - 1): #grid[r][1] ~ grid[r][ncol-1]
                length += (grid[r][c] * (4 - grid[r - 1][c] - grid[r][c - 1] - grid[r][c + 1] - grid[r+1][c]))
            length += (grid[r][ncol - 1] * (4 - grid[r - 1][ncol - 1] - grid[r + 1][ncol - 1] - grid[r][ncol - 2])) #grid[r][ncol]

        length += (grid[nrow - 1][0] * (4 - grid[nrow - 2][0] - grid[nrow - 1][1])) # grid[nrow][0]
        for c in range(1, ncol - 1):
            length += (grid[nrow - 1][c] * (4 - grid[nrow - 1][c - 1] - grid[nrow - 1][c + 1] - grid[nrow - 2][c])) #grid[nrow][1]~grid[nrow][ncol - 1]
        length += (grid[nrow - 1][ncol - 1] * (4 - grid[nrow - 2][ncol - 1] - grid[nrow - 1][ncol - 2]))
        return length
