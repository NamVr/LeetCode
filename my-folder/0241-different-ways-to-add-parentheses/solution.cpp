class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        vector<int> result;

        for (int i = 0; i < expression.size(); i++) {
            char c = expression[i];

            if (c == '+' || c == '-' || c == '*') {
                vector<int> left = diffWaysToCompute(expression.substr(0,i));
                vector<int> right = diffWaysToCompute(expression.substr(i+1));

                // merge l + r
                for (int l : left) {
                    for (int r : right) {
                        if (c == '+') {
                            result.push_back(l+r);
                        } else if (c == '-') {
                            result.push_back(l-r);
                        } else if (c == '*') {
                            result.push_back(l*r);
                        }
                    }
                }
            }
        }

        // base case
        if (result.empty()) {
            result.push_back(stoi(expression));
        }

        return result;
    }
};
