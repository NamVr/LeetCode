class Solution {
public:
    bool parseBoolExpr(string expression) {
        stack<char> st;

        for (char c : expression) {
            if (c == ',' || c == '(') continue;
            if (c == 't' || c == 'f' || c == '!' || c == '|' || c == '&') {
                st.push(c); // push all base cases to stack.
            }

            else if (c == ')') {
                // evaluate at closing
                bool hasTrue = false, hasFalse = false;

                // base case, till it is either t of f
                while (st.top() != '!' && st.top() != '&' && st.top() != '|') {
                    char topVal = st.top();
                    st.pop();
                    if (topVal == 't') hasTrue = true;
                    if (topVal == 'f') hasFalse = true;
                }

                // now it will be an operator.
                char op = st.top();
                st.pop();

                if (op == '!') {
                    st.push(hasTrue ? 'f' : 't');
                } else if (op == '&') {
                    st.push(hasFalse ? 'f' : 't');
                } else { // op == '|'
                    st.push(hasTrue ? 't' : 'f');
                }
            }
        }

        return st.top() == 't';
    }
};
