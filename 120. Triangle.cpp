class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
    int** sumPath;
    int r, c, m = triangle.size();
    int min;
    int* triangleColSizes = (int*) malloc(sizeof(int*) * m);
    for (r = 0; r < m; r++)
        *(triangleColSizes + r) = triangle[r].size();
    sumPath = (int **) malloc(sizeof(int*) * m);
    for (r = 0; r < m; r++)
        sumPath[r] = (int*) malloc(sizeof(int) * *(triangleColSizes + r));
    for (r = 0; r < m; r++)
        for (c = 0; c < *(triangleColSizes + r); c++)
            sumPath[r][c] = 0;
    sumPath[0][0] = triangle[0][0];
    for (r = 1; r < m; r++)
        for (c = 0; c < *(triangleColSizes + r); c++){
            if (c == 0){
                sumPath[r][c] = sumPath[r - 1][c] + triangle[r][c];
            }else if (c == *(triangleColSizes + r) - 1){
                sumPath[r][c] = sumPath[r - 1][c - 1] + triangle[r][c];
            }
            else{
                if (sumPath[r - 1][c - 1] > sumPath[r - 1][c])
                    sumPath[r][c] = triangle[r][c] + sumPath[r - 1][c];
                else
                    sumPath[r][c] = triangle[r][c] + sumPath[r - 1][c - 1];
            }
        }
    min = sumPath[m - 1][0];
    for (c = 0; c < *(triangleColSizes + m - 1); c++)
        if (min > sumPath[m - 1][c])
            min = sumPath[m - 1][c];
    return min;
}
};
