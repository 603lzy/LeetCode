int uniquePaths(int m, int n) {
    int grid[m][n];
    int i, j;
    grid[0][0] = 0;
    if (m > 1 && n > 1){
        for (i = 1; i < m; i++)
            grid[i][0] = 1;
        for (j = 1; j < n; j++)
            grid[0][j] = 1;
        for (i = 1; i < m; i++)
            for (j = 1; j < n; j++)
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1];
        return grid[m - 1][n - 1];
    }else 
        return !(!m || !n); // m or n = 0, no path; m or n = 1, only 1 path   
}
