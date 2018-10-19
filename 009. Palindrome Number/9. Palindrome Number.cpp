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
    //Another Solution inspired by one-liner python
    bool isPalindrome1(int x) {
        string s1 = to_string(x), s2 = s1;
        reverse(s1.begin(), s1.end());
        return s1 == s2;
};
