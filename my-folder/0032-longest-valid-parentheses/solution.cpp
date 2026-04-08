class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> stack = {-1};
        int res = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                stack.push_back(i);
            } else {
                stack.pop_back();

                if (stack.size() == 0) {
                    stack.push_back(i); // new marker
                } else {
                    res = max(res, i - stack[stack.size() - 1]);
                }
            }
        }

        return res; 
    }
};
