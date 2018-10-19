class Solution {
public:
    int myAtoi(string s) {
        int i = 0, sign, MAX = 0;
        long long val = 0;
        for (i = 0; isspace(s[i]); i++);
        sign = (s[i] == '-' ? -1 : 1);
        if (s[i] == '+' || s[i] == '-')
            i++;
        for (val = 0; isdigit(s[i]); i++){
            val = 10 * val + (s[i] - '0');
            if (val > INT_MAX)
                return (sign == 1 ? INT_MAX : INT_MIN);
        }
        return val * sign;
    }
};
