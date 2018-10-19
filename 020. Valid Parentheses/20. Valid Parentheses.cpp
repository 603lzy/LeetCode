class Solution {
public:
    bool isValid(string s) {
        stack<char> p;
        for (char& c : s)
            p.empty() ? p.push(c) : (c == p.top() + 2 || c == p.top() + 1 ? p.pop() : p.push(c));
        return p.empty();
    }
};
