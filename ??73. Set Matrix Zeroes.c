void setZeroes(int** matrix, int matrixRowSize, int matrixColSize) {
    int row[matrixRowSize];
    int col[matrixColSize];
    int i, j;
    for (i = 0; i < matrixRowSize; i++)
        row[matrixRowSize] = 0;
    for (j = 0; j < matrixColSize; j++)
        col[matrixColSize] = 0;
    for (i = 0; i < matrixRowSize; i++)
        for (j = 0; j < matrixRowSize; j++)
            if (matrix[i][j] == 0){
                row[i] = 1;
                col[j] = 1;
            }
    for (i = 0; i < matrixRowSize; i++)
        for (j = 0; j < matrixColSize; j++)
            if (row[i] == 1 || col[j] == 1)
                matrix[i][j] = 0;
}
