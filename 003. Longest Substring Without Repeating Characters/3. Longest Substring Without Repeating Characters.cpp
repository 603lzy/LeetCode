class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int sLen = s.size(), subStrLen = 0, p1 = 0, p2 = 1;
        if (sLen <= 1)
            return sLen;
        string subStr;
        while (p2 < sLen && subStrLen < 95){
            for (p2 = p1; p2 < sLen; p2++){
                subStr.assign(s, p1, p2 - p1); //substr is s[p1:p2]
                if (subStr.find(s[p2]) != -1) // s[p2] in substr
                    break;
            }
            subStrLen = max(p2 - p1, subStrLen);
            p1++;
        }
        return subStrLen;
    };
};
