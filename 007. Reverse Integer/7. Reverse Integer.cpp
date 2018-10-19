class Solution {
public:
    int reverse(int x) {
        long long y = 0;
        while (x) {
            y = y * 10 + x % 10;
            x /= 10;
        }
        return y < INT_MIN || y > INT_MAX ? 0 : y;
    }
};
