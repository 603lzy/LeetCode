class Solution {
public:
    int findComplement(int num) {
        int cnt = 1, n = num;
        while (num >>= 1)
            cnt++;
        return pow(2, cnt) - n - 1; 
    }
};
