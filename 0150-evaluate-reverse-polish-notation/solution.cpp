class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        unordered_set<string> ops = {"+", "-", "/", "*"};

        for (int i = 0; i < tokens.size(); i++) {
            if (ops.find(tokens[i]) == ops.end()) {
                // it is a digit, push to stack
                s.push(stoi(tokens[i]));
            } else {
                // it is an operator, pop 2 elements from stack and do operation
                int val2 = s.top();
                s.pop();
                int val1 = s.top();
                s.pop();
                
                switch(tokens[i][0]) {
                    case '+':
                    s.push(val1 + val2);
                    break;

                    case '-':
                    s.push(val1 - val2);
                    break;

                    case '*':
                    s.push(val1 * val2);
                    break;

                    case '/':
                    s.push(val1 / val2);
                    break;
                }
            }
        }
        return s.top();
    }
};
