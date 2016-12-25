class Solution {
public:
    bool isValid(string s) {
        stack<char> p;
        for (char& c : s)
            if (!p.empty())
                if (c == p.top() + 2 || c == p.top() + 1)
                    p.pop();
                else
                    p.push(c);
            else
                p.push(c);
        return p.empty();
    }
};
