class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows <= 1 || numRows >= s.length())
            return s;
        string result = "";
        int maxStep = numRows * 2 - 2;
        for (int i = 1; i <= numRows; i++){
            int j = i - 1;
            int step = (i < numRows) ? (numRows - i) * 2 : maxStep;
            while (j < s.length()) {
                result += s[j];
                if (result.length() == s.length())
                    return result;
                j += step;
                if (step < maxStep) {
                    step = maxStep - step;
                }
            }
        }
        return result;
    }
};
