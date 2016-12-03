int numSquares(int n) {
    int i, j;
    while (n % 4 == 0)
        n /= 4;
    if (n % 8 == 7)
        return 4;
    for (i = 0; i * i <= n; i++){
        j = sqrt(n - i * i);
        if (i * i + j * j == n)
            return !!i + !!j;
    }
    return 3;
}
