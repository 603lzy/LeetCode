int findComplement(int num) {
    int cnt = 0, n = num;
    while (num > 0){
        cnt++;
        num >>= 1;
    } // calculate the digit number of binary num
    return pow(2, cnt) - n - 1; //return 2 ^ cnt - num - 1
}
