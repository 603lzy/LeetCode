class Solution {
public:
    string longestPalindrome(string s) {
        int sLen = s.length(), maxLen = 0, maxStart = 0;
        int pi = 0, pl = 0, pr = 0, subLen = 0;
        while (pi <= sLen - maxLen / 2){
            pl = pr = pi;
            while (pr < sLen - 1 && s[pr + 1] == s[pr])
                pr++;
            pi = pr + 1;
            while (pl > 0 && pr < sLen - 1 && s[pr + 1] == s[pl - 1]){
                pl--;
                pr++;
            }
            subLen = pr - pl + 1;
            if (maxLen < subLen){
                maxLen = subLen;
                maxStart = pl;
            }
        }
        return s.substr(maxStart, maxLen);
    }
};
