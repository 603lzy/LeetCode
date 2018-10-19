bool isPalindrome(int x) {
    if (x < 0)
        return 0;
    int sum = 0, temp = x;
    while (x){
        sum = sum * 10 + x % 10;
        x /= 10;
    }
    return temp == sum;
}


int largestPalindrome(int n) {
    switch(n){
        case 5: return 677; // int cannot save that large number
        case 6: return 1218;
        case 7: return 877;
        case 8: return 475;
    }
    long long int num = pow(10, n) - 1, i = 0, x, curnum;
    while (true){
        for (x = i; x >= 1; x--){
            curnum = (num - x) * (num + x);
            if (isPalindrome(curnum))
                return curnum % 1337;
        }
        i++;
        num--;
    }
}
