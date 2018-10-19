class Solution {
public:
    int romanToInt(string s) {//use hash table
        if (!s.length())
            return 0; //check null string
        unordered_map<char, int> dict = {{'I', 1},{'V', 5},{'X', 10},{'L', 50},{'C', 100},{'D', 500},{'M', 1000}};
        int num = dict[s.back()], i = s.length() - 1;
        while (--i >= 0)
            num = num + (dict[s[i]] < dict[s[i + 1]] ? -dict[s[i]] : dict[s[i]]);
        return num;
    }
};
