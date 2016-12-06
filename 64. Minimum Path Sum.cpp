class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int i, j, ret = 0;
        int gridRowSize = grid.size(), gridColSize = grid[0].size();
        int S[gridRowSize][gridColSize];
        if (gridRowSize == 1){
            for (j = 0; j < gridColSize; j++)
                ret += grid[0][j];
            return ret;
        }else if(gridColSize == 1){
            for (i = 0; i < gridRowSize; i++)
                ret += grid[i][0];
            return ret;
        }else{// m > 1 and n > 1
            S[0][0] = grid[0][0];
            for (i = 1; i < gridRowSize; i++)
                S[i][0] = S[i - 1][0] + grid[i][0];
            for (j = 1; j < gridColSize; j++)
                S[0][j] = S[0][j - 1] + grid[0][j];
            for (i = 1; i < gridRowSize; i++)
                for (j = 1; j < gridColSize; j++)
                S[i][j] = grid[i][j] + min(S[i - 1][j],S[i][j - 1]);
            return S[gridRowSize - 1][gridColSize - 1];
        } 
    }
};
