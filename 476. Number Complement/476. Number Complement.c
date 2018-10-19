int findComplement(int num) {
    int cnt = 1, n = num;
    while (num >>= 1) // left shift while there is 1 in num
        cnt++; // count the digit of num
    return pow(2, cnt) - n - 1; 
}
