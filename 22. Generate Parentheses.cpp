class Solution { //https://discuss.leetcode.com/topic/26309/my-0ms-c-solution-without-recursion-and-dfs
public:
    vector<string> generateParenthesis(int n) {
        vector<string> parenTable;
        if (n == 0)
            return parenTable;
        string s;
        int pl = n, pr = n;
        for (int i = 0; i < n; i++) s += "(";
        for (int i = 0; i < n; i++) s += ")";  //s = "(((...()...)))"
        while (s != ""){
            parenTable.push_back(s);
            while (s != "" && (s.back() == ')' || pl - 1 <  pr + 1)){
                s.back() == ')' ? pr-- : pl --;
                s.pop_back();
            }
            if (s != ""){
                s.back() = ')';
                pl--, pr++;
                while (pl < n){
                    s += '(';
                    pl++;
                }
                while (pr < n){
                    s += ')';
                    pr++;
                }
            }
        }
        return parenTable;
    }
};
