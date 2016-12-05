class Solution {
public:
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
};
