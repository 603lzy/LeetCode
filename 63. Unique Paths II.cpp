class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
	    int** cntPath;
	    int r, c;
	    int blogged = 0;  // flag 0 not block;1 blocked
	    cntPath = (int**) malloc(sizeof(int*) * m); // m row
	    for (r = 0; r < m; r++) // n col
		    cntPath[r] = (int*) malloc(sizeof(int*) * n);
	
	    if (obstacleGrid[0][0] == 1)
		    return 0;
	    else if (!m || !n)
		    return 0;
	    else if (m == 1 && n == 1)
		    return 1 - obstacleGrid[0][0];
	    else if (m > 1 && n > 1) {
		    for (r = 0; r < m; r++) {
			    if (blogged == 0 && obstacleGrid[r][0] == 0)
				    cntPath[r][0] = 1;
			    else {
				    cntPath[r][0] = 0;
				    blogged = 1;
			    }
		    }
		    blogged = 0;
		    for (c = 1; c < n; c++) {
			    if (blogged == 0 && obstacleGrid[0][c] == 0)
				    cntPath[0][c] = 1;
			    else {
				    blogged = 1;
				    cntPath[0][c] = 0;
			    }
		    }
		    for (r = 1; r < m; r++)
			    for (c = 1; c < n; c++) {
				    if (!obstacleGrid[r][c])
					    cntPath[r][c] = cntPath[r - 1][c] + cntPath[r][c - 1];
				    else
					    cntPath[r][c] = 0;
			    }
		    return cntPath[m - 1][n - 1];
	    }
	    else if (m == 1) {
		    for (c = 0; c < n; c++)
			    if (obstacleGrid[0][c] == 1)
				    return 0;
	    }
	    else if (n == 1) {
		    for (r = 0; r < m; r++)
			    if (obstacleGrid[r][0] == 1)
				    return 0;
	    }
	    return 1; 
    }
};
